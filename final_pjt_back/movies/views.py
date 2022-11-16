from django.shortcuts import render
from .models import Movie, Genre
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def movies_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    pass

    #     if request.method == 'GET':
    #     # articles = Article.objects.all()
    #     articles = get_list_or_404(Article)
    #     serializer = ArticleListSerializer(articles, many=True)
    #     return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = ArticleSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         # serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
