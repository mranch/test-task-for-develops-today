from news.viewsets import PostViewSet, CommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
