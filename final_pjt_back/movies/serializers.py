from rest_framework import serializers
from .models import Movie,Comment

#### 영화리스트
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title','poster_path')

#### 단일영화+리뷰리스트
class CommentTitleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'title','grade','movie')

class MovieDetailSerializer(serializers.ModelSerializer):
    comments = CommentTitleListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'


#### 단일리뷰
class OneMovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

class OneCommentSerializer(serializers.ModelSerializer):
    movie = OneMovieTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('movie',)## 이게 참조로들고온 movie인가? 위에서 readonly해준거랑 이거랑 다른걸까?같으면 언제readonlyt?

class CommentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'    
        read_only_fields = ('movie',)


