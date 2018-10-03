from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import ArticleModelForm
from .models import Article


class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'article/article_detail.html'

    def get_object(self, queryset=None):
        slug_= self.kwargs.get("slug")
        return get_object_or_404(Article, slug=slug_)


class ArticleCreateView(CreateView):
    template_name = 'article/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    success_url = reverse_lazy('article:article-list')

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'article/article_update.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    success_url = reverse_lazy('article:article-list')

    def get_object(self, queryset=None):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Article, slug=slug_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'article/article_delete.html'

    def get_object(self):
        slug_= self.kwargs.get("slug")
        return get_object_or_404(Article, slug=slug_)

    def get_success_url(self):
        return reverse('article:article-list')