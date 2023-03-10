from django.urls import path
from .views import UserProfileView,ProfileUpdateView

urlpatterns = [
    path('profile/<slug>',UserProfileView.as_view(),name='user-profile'),
    path('update-profile/<slug>',ProfileUpdateView.as_view(),name="update-profile")
    
]
