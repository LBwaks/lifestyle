import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.postgres.search import (
    SearchHeadline,
    SearchQuery,
    SearchRank,
    SearchVector,
)
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from hitcount.views import HitCountDetailView
from taggit.models import Tag

from .forms import BlogForm, CommentForm, EditBlogForm
from .models import Blog, Category, Comment

# Create your views here.


class BlogListView(ListView):
    model = Blog
    template_name = "blogs/blog-list.html"
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["blogs"] = Blog.objects.all()
    #     return context


class BlogDetailView(HitCountDetailView):
    model = Blog
    template_name = "blogs/blog-details.html"
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = get_object_or_404(Blog, slug=self.kwargs.get("slug"))
        similar_blogs = blog.tags.similar_objects()[:5]

        # similar_blogs = random.choice(similar_blogs)
        context["similar_blogs"] = similar_blogs
        popular_blogs = Blog.objects.order_by("-hit_count_generic__hits")[:5]

        context["popular_blogs"] = popular_blogs
        context["comments"] = Comment.objects.filter(blog=self.get_object())
        # context['comment_count'] = comments.count()
        context["form"] = CommentForm()

        return context

    def post(self, request, slug, *args, **kwargs):
        if self.request.method == "POST":
            form = CommentForm(self.request.POST)
            if form.is_valid():
                comment = form.cleaned_data["comment"]
                try:
                    parent = form.cleaned_data["parent"]
                except:
                    parent = None

                new_comment = form.save(commit=False)

                new_comment = Comment(
                    comment=comment,
                    user=self.request.user,
                    blog=self.get_object(),
                    parent=parent,
                )
                new_comment.save()
            return redirect(self.request.path_info)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blogs/add-blog.html"
    form_class = BlogForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        return super(BlogCreateView, self).form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "blogs/edit-blog.html"
    form_class = EditBlogForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        return super(BlogUpdateView, self).form_valid(form)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    # template_name = "TEMPLATE_NAME"
    success_url = reverse_lazy("blogs")


class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

    status_code = 200


@login_required
def DeleteBlog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == "DELETE":
        blog.delete()
    return HTTPResponseHXRedirect(redirect_to=reverse_lazy("blogs"))


class BlogTagsListView(ListView):
    model = Blog
    template_name = "blogs/tag-blogs.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(Tag, name=self.kwargs.get("name"))
        blogs = Blog.objects.filter(tags=tag)
        context["blogs"] = blogs
        return context


class CategoryListView(ListView):
    model = Category
    template_name = "blogs/category-blogs.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, name=self.kwargs.get("name"))
        context["blogs"] = Blog.objects.filter(category=category)
        category_most_viewed = Blog.objects.filter(category=category).order_by(
            "-hit_count_generic__hits"
        )[:5]
        context["category_most_viewed"] = category_most_viewed
        return context


class UsersListView(ListView):
    model = Blog
    template_name = "blogs/user-blogs.html"

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        blog_by = get_object_or_404(User, username=self.kwargs.get("username"))
        blogs = Blog.objects.filter(user=blog_by)

        page_num = self.request.GET.get("page", 1)
        paginator = Paginator(blogs, 2)
        try:
            blogs = paginator.page(page_num)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        context = {
            "blogs": blogs,
        }
        return context


class MyBlogsListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "blogs/my-blogs.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_blogs = Blog.objects.filter(user=self.request.user)
        context["my_blogs"] = my_blogs

        page_num = self.request.GET.get("page", 1)
        paginator = Paginator(my_blogs, 2)
        try:
            my_blogs = paginator.page(page_num)
        except PageNotAnInteger:
            my_blogs = paginator.page(1)
        except EmptyPage:
            my_blogs = paginator.page(paginator.num_pages)
        context = {
            "my_blogs": my_blogs,
        }
        return context


class SearchListView(ListView):
    model = Blog
    template_name = "pages/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        search_vector = (
            SearchVector("title", weight="A")
            + SearchVector("content", weight="B")
            + SearchVector("tags", weight="B")
        )
        search_query = SearchQuery(query)
        search_headline = SearchHeadline("title", search_query)
        return (
            Blog.objects.annotate(
                search=search_vector, rank=SearchRank(search_vector, search_query)
            )
            .annotate(headline=search_headline)
            .filter(rank__gte=0.3)
            .order_by("-rank")
        )
