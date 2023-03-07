from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView,ListView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import BlogForm, EditBlogForm
from .models import Blog

# Create your views here.


class BlogListView(ListView):
    model = Blog
    template_name = "blogs/blog-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/blog-details.html"


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
    success_url = reverse_lazy('blogs')
    
class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

    status_code = 200

def DeleteBlog(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    if request.method =="DELETE":
        blog.delete()
    return HTTPResponseHXRedirect(redirect_to =reverse_lazy('blogs')
)
        