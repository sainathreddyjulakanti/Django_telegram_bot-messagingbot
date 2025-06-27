from django.urls import path
from .views.login_register_views import RegisterView, CustomLoginView
from .views.home_view import HomeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/',HomeView.as_view())
]
