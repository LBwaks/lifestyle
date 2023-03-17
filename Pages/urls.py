from django.urls import path 
from .views import About,ContactCreateView

urlpatterns = [
    path('about',About.as_view(),name='about'),
    path('contact',ContactCreateView.as_view(),name='contact')
]
