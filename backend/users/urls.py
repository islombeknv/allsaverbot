from django.urls import path

from .views import *

urlpatterns = [
    path('user/register/', TelegramRegistrationView.as_view()),
    path('user/<int:pk>/', UserListAPIView.as_view()),
    path('users/list/', UserListAPIView.as_view()),
    path('users/', ReportUserListAPIView.as_view()),
    ]
