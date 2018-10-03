from django.urls import path
from .views import (
    PostDetailView,
    PostUpdateView,
    PostListView,
    PostCreateView,
    PostDeleteView,
                    )

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<slug>/', PostDetailView.as_view(), name='post-detail'),
    path('<slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<slug>/delete/', PostDeleteView.as_view(), name='post-delete'),

]