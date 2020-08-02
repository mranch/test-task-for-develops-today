from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from rest_framework.decorators import api_view
from . import models, serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer


# Create your views here.
@api_view(["GET"])
def home(request):
    posts = models.Post.objects.all()
    serializer = serializers.PostSerializer(posts, many=True)
    return JsonResponse({"posts": serializer.data}, status=status.HTTP_200_OK)


class PostListView(ListView):
    model = models.Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class ListPosts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'news/post_list.html'

    def get(self, request):
        posts = models.Post.objects.all()
        s = [serializers.PostSerializer(p).data for p in posts]
        return Response({"object_list": posts})
