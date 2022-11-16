from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=70, default='')

class Movie(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_id = models.IntegerField() # 영화 id
    title = models.CharField(max_length=100) # 제목
    adult = models.BooleanField()
    genre_ids = models.ManyToManyField(Genre)
    poster_path = models.TextField()
    overview = models.TextField() # 줄거리
    popularity = models.FloatField()
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    

'''
'adult': False,
'movie_id': 20982,
'title': '나루토 질풍전 극장판 1기 - 나루토의 죽음',
'genre_ids': [16, 28, 14],
'poster_path': 'https://image.tmdb.org/t/p/w500/vaEX9f8ud7iF0G7EoyGxAyRNV1p.jpg',
'overview': '미래 예언과 마귀 봉인 능력을 지닌 원령나라의 무녀가 부활한 마귀의 표적으로 지목되자 나루토와 '
            '친구들은 무녀를 지키기 위해 길을 떠난다. 그러나 원령나라에 도착한 일행에게 무녀는 나루토의 '
            '죽음을 예언하고 이에 모두들 충격에 휩싸이는데...',
'popularity': 217.402,
'release_date': '2007-08-04',
'vote_average': 7.3,
'vote_count': 519},
'''