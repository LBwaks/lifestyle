from django.urls import path
from .views import BlogListView , BlogDetailView,BlogCreateView,BlogUpdateView,DeleteBlog
urlpatterns = [
    path('',BlogListView.as_view(),name='blogs'),
    path('<slug>/',BlogDetailView.as_view(),name ='blog-detail'),
    path('add-blog',BlogCreateView.as_view(),name='add_blog',),
    path('edit-blog/<slug>',BlogUpdateView.as_view(),name='edit-blog'),
    path('delete-blog/<slug>',DeleteBlog, name='delete-blog')
]
