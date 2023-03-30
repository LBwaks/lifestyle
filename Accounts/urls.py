from django.urls import path
from .views import UserProfileView,ProfileUpdateView,BloggerDetailView

urlpatterns = [
    path('profile/<slug>',UserProfileView.as_view(),name='user-profile'),
    path('update-profile/<slug>',ProfileUpdateView.as_view(),name="update-profile"),
    path('blogger-profile/<username>',BloggerDetailView.as_view(),name="blogger-profile")
    
]
