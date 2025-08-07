from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Blog,BlogImage,BlogParagraph
from django.views.generic import ListView
from django.views.generic import DetailView


class BlogListView(ListView):
    model = Blog
    template_name = "blog_list.html"
    paginate_by = 3


class BlogDetailView(DetailView):
    model = Blog
    template_name = "detail_blog.html"
    context_object_name = "blog"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()

        blog_paragraphs = BlogParagraph.objects.filter(blog=blog)
        blog_images = BlogImage.objects.filter(blog=blog)
        
        context['combined_data'] = list(zip(blog_paragraphs, blog_images))
        return context
