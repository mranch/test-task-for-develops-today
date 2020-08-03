from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from rest_framework.decorators import api_view
from . import models, serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer


# Create your views here.
class PostListView(ListView):
    model = models.Post


class PostDetailView(DetailView):
    model = models.Post


class PostCreateView(CreateView):
    model = models.Post
    fields = ['title', 'link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCommentListView(ListView):
    model = models.Comment
    template_name = 'news/post_comments.html'

    def get_queryset(self):
        post = get_object_or_404(models.Post, id=self.kwargs.get('pk'))
        return models.Comment.objects.filter(post_id=post)


class CommentCreateView(CreateView):
    model = models.Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.post_id = models.Post.objects.get(id=self.request.pk)
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = models.Post
    success_url = '/'
