import requests
import json
import copy
from pprint import pprint

file_path_popular_movie = 'popular_movie.json'
file_path_genre = 'genre.json'

def TMDBapi():
    result = []
    idx = 0
    pages = 10

    for page in range(1,pages+1):
        URL = 'https://api.themoviedb.org/3/movie/popular?api_key=a41ba99ef968eda4eec19375d33b98ec&language=ko-KR&page='+str(page)
        response = requests.get(URL).json()['results']
        for i in range(len(response)):
            del response[i]["backdrop_path"]
            del response[i]["original_title"]
            del response[i]["original_language"]
            del response[i]["video"]
            del response[i]["vote_count"]
            response[i]["tmdb_id"] = response[i]["id"]
            del response[i]["id"]
            response[i]["poster_path"] = 'https://image.tmdb.org/t/p/w500'+response[i]["poster_path"]
            templates = {
                "model": "movieapi.movie",
                "pk": 0,
                "fields": {
                }
            }
            idx += 1
            templates["pk"] = idx
            templates["fields"] = response[i]
            result.append(templates)
    return result

def TMDBapiGenre():
    URL = 'https://api.themoviedb.org/3/genre/movie/list?api_key=a41ba99ef968eda4eec19375d33b98ec&language=ko-KR'
    response = requests.get(URL).json()['genres']

    for genre in response:
        temp= copy.deepcopy(genre)
        del genre['id']
        del genre['name']
        genre['model'] = 'movieapi.genre'
        genre['fields'] = temp

    return response


with open(file_path_popular_movie, 'w') as f:
    json.dump(TMDBapi(),f,ensure_ascii=False,indent=4)
 
with open(file_path_genre, 'w') as f:
    json.dump(TMDBapiGenre(),f,ensure_ascii=False,indent=4)