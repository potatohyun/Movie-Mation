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

@api_view(['GET'])
def movies_detail(request,movies_pk):
    movie = get_object_or_404(Movie,pk=movies_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)
