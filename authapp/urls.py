from django.urls import path
from .views import UserProfileView, UserSignupView

urlpatterns = [
    path('signup', UserSignupView.as_view()),
    path('profile', UserProfileView.as_view()),
]