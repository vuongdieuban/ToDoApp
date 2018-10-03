
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import PostModelForm
from .models import Post


class PostListView(ListView):
    template_name = 'post/post_list.html'
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    template_name = 'post/post_detail.html'

    def get_object(self, queryset=None):
        slug_= self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug_)


class PostCreateView(CreateView):
    template_name = 'post/post_create.html'
    form_class = PostModelForm
    queryset = Post.objects.all()
    success_url = reverse_lazy('post:post-list')

    def form_valid(self, form):
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    template_name = 'post/post_update.html'
    form_class = PostModelForm
    queryset = Post.objects.all()
    success_url = reverse_lazy('post:post-list')

    def get_object(self, queryset=None):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    template_name = 'post/post_delete.html'

    def get_object(self):
        slug_= self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug_)

    def get_success_url(self):
        return reverse('post:post-list')