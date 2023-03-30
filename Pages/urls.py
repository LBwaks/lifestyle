from django.urls import path 
from .views import About,ContactView,Home

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('about',About.as_view(),name='about'),
    path('contact',ContactView,name='contact')
]
