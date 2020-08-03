from django.urls import path, include
from news.views import PostDeleteView, CommentCreateView, PostCommentListView, PostListView, PostCreateView, PostDetailView
from .router import router

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/submit/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comments/', PostCommentListView.as_view(), name='post-comments'),
    path('post/<int:pk>/comments/submit', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('api/', include(router.urls))
]
