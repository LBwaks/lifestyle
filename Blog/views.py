from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from hitcount.views import HitCountDetailView

from .forms import BlogForm,  EditBlogForm,CommentForm
from .models import Blog,Comment

# Create your views here.


class BlogListView(ListView):
    model = Blog
    template_name = "blogs/blog-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all()
        return context


class BlogDetailView(HitCountDetailView):
    model = Blog
    template_name = "blogs/blog-details.html"
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["popular_blogs"] = (
            Blog.objects.order_by("-hit_count_generic__hits")[:5],
        )
        context["comments"] = Comment.objects.filter(blog=self.get_object())
        # context['comment_count'] = comments.count()
        context["form"] = CommentForm()

        return context

    def post(self, request,slug, *args, **kwargs):
        if self.request.method == "POST":
            form = CommentForm(self.request.POST)
            if form.is_valid():
                comment = form.cleaned_data["comment"]
                try:
                    parent = form.cleaned_data["parent"]
                except:
                    parent = None

                new_comment = form.save(commit=False)
                # new_comment.user = self.request.user
                # new_comment.blog=self.get_object()
                # new_comment.comment= comment
                # new_comment.parent= parent
                new_comment = Comment(
                    comment=comment,
                    user=self.request.user,
                    blog=self.get_object(),
                    parent=parent,
                )
                new_comment.save()
            return redirect(self.request.path_info)
            # blog= get_object_or_404(Blog,slug=slug) 
            # context={
            #     'blog':blog,'form':form,
            # }
            # return render (request,'blogs/blog-details.html',context)


class BlogCreateView(CreateView):
    model = Blog
    template_name = "blogs/add-blog.html"
    form_class = BlogForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        return super(BlogCreateView, self).form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blogs/edit-blog.html"
    form_class = EditBlogForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        return super(BlogUpdateView, self).form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    # template_name = "TEMPLATE_NAME"
    success_url = reverse_lazy("blogs")


class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

    status_code = 200


def DeleteBlog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == "DELETE":
        blog.delete()
    return HTTPResponseHXRedirect(redirect_to=reverse_lazy("blogs"))
