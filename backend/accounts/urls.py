# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # 회원가입 URL 추가
    path('profile_setup/', views.profile_setup, name='profile_setup'),
    path('investment_analysis/', views.investment_analysis, name='investment_analysis'),
    path('set_alert/', views.set_alert, name='set_alert'),
]
