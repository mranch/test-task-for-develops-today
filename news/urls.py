from django.urls import path, include
# from news import views
from news.views import PostListView, ListPosts
from .router import router

urlpatterns = [
    path('', ListPosts.as_view(), name='post-list'),
    path('api/', include(router.urls))
]
