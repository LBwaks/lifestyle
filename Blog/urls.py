from django.urls import path

from .views import (
    BlogCreateView,
    BlogDetailView,
    BlogListView,
    BlogTagsListView,
    BlogUpdateView,
    DeleteBlog,
    MyBlogsListView,
    SearchListView,
    UsersListView,
    CategoryListView,
    add_bookmark,
    BlogBookmarks,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="blogs"),
    path("my-blogs/", MyBlogsListView.as_view(), name="my-blogs"),
    path("search/", SearchListView.as_view(), name="search"),
    path("<slug>/", BlogDetailView.as_view(), name="blog-detail"),
    path(
        "add-blog",
        BlogCreateView.as_view(),
        name="add_blog",
    ),
    path("edit-blog/<slug>", BlogUpdateView.as_view(), name="edit-blog"),
    path("delete-blog/<slug>", DeleteBlog, name="delete-blog"),
    path("user-blog/<username>", UsersListView.as_view(), name="user-blog"),
    path("tags/<name>", BlogTagsListView.as_view(), name="tags"),
    path('categories/<name>',CategoryListView.as_view(),name='categories'),
    path('bookmark/<slug>',add_bookmark,name='bookmark'),
    path('bookmarks',BlogBookmarks.as_view(),name='bookmarks')
]
