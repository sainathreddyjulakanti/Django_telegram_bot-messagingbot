from django.urls import path
from .views import TelegramUserView
urlpatterns = [
    path('api/userdetails/', TelegramUserView.as_view()),
    
]