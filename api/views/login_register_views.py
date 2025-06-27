from rest_framework import generics, status
from rest_framework.response import Response
from ..serializer.login_serializers import RegisterSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializer.login_serializers import CustomTokenObtainPairSerializer
User = get_user_model()

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from ..serializer.login_serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from ..tasks import send_email_task  

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        send_email_task.delay(
            subject="Registration Successful",
            message="Hi {}, your registration was successful!".format(user.email),
            user_email=user.email
        )

        refresh = RefreshToken.for_user(user)
        data = {
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(data, status=status.HTTP_201_CREATED)



class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

