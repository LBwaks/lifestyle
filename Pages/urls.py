from django.urls import path 
from .views import About,ContactView

urlpatterns = [
    path('about',About.as_view(),name='about'),
    path('contact',ContactView,name='contact')
]
