from django.shortcuts import render
from .models import Movie, Genre, Comment
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer,MovieDetailSerializer,OneCommentSerializer,CommentPostSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

##############<<< 영화(게시글) >>>>#################

###영화전제
@api_view(['GET'])
def movies_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

### 단일영화(+해당영화 리뷰들)
@api_view(['GET'])
def movies_detail(request,movies_pk):
    movie = get_object_or_404(Movie,pk=movies_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

##############<<< 댓글 >>>>#################

### 단일 댓글
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):    
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = OneCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = OneCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movies_pk):
    movie = get_object_or_404(Movie, pk=movies_pk)
    serializer = CommentPostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie) # 로그인정보 병합되면 삭제
        # serializer.save(movie=movie,user = request.user)  # 로그인한사람들 user정보 자동으로 집어넣어주게하는 코드
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# def like(request,comment_pk):
#     comment = get_object_or_404(Comment, pk = comment_pk)
#     if comment.like_users.filter(pk=request.user.pk).exists():
#         comment.like_users.remove(request.user)
#     else:
#         comment.like_users.add(request.user)
#     serializer = OneCommentSerializer(comment)
#     return Response(serializer.data)