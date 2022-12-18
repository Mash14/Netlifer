from django.shortcuts import render
import requests
from decouple import config

api_key = config('API_KEY')
youtube_api_key=config('YOUTUBE_API_KEY')
# Create your views here.


def home(request):
    # Trending Movies And Tv Shows 
    trending_url = f'https://api.themoviedb.org/3/trending/all/day?api_key={api_key}'
    response = requests.get(trending_url)
    data = response.json()
    trending_movies_shows = data['results']

    # Trending Movies 
    trending_movies_url = f'https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}'
    response = requests.get(trending_movies_url)
    data = response.json()
    trending_movies = data['results']

    # Trending Tv Shows 
    trending_tv_shows_url = f'https://api.themoviedb.org/3/trending/tv/day?api_key={api_key}'
    response = requests.get(trending_tv_shows_url)
    data = response.json()
    trending_tv_shows = data['results']

    return render(request,'home.html',{'trending_movies_shows':trending_movies_shows,'trending_movies':trending_movies,'trending_tv_shows':trending_tv_shows})


def movies(request):
    # In Cinema Movies 
    cinema_url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1'
    response = requests.get(cinema_url)
    data = response.json()
    cinema_movies = data['results']
    
    # Popular Movies 
    popular_url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(popular_url)
    data = response.json()
    popular_movies = data['results']

    # Top Rated
    top_rated_url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1'
    response = requests.get(top_rated_url)
    data = response.json()
    top_rated_movies = data['results']

    # Upcoming
    upcoming_url = f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=en-US&page=1'
    response = requests.get(upcoming_url)
    data = response.json()
    upcoming_movies = data['results']

    title = 'Movies'

    return render(request,'movies.html',{'cinema_movies':cinema_movies,'popular_movies':popular_movies,'top_rated_movies':top_rated_movies,'upcoming_movies':upcoming_movies,'title':title})


def tv_shows(request):
    # Trending tv_shows 
    trending_url = f'https://api.themoviedb.org/3/trending/tv/day?api_key={api_key}'
    response = requests.get(trending_url)
    data = response.json()
    trending_tv_shows = data['results']

    # Airing Today tv_shows 
    # airing_today_url = f'https://api.themoviedb.org/3/tv/airing_today?api_key={api_key}&language=en-US&page=1'
    # response = requests.get(airing_today_url)
    # data = response.json()
    # airing_today_tv_shows = data['results']
    airing_today_tv_shows = ''

    # On Air tv_shows 
    on_air_url = f'https://api.themoviedb.org/3/tv/on_the_air?api_key={api_key}&language=en-US&page=1'
    response = requests.get(on_air_url)
    data = response.json()
    on_air_tv_shows = data['results']

    # Popular tv_shows 
    popular_url = f'https://api.themoviedb.org/3/tv/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(popular_url)
    data = response.json()
    popular_tv_shows = data['results']

    # Top Rated tv_shows 
    top_rated_url = f'https://api.themoviedb.org/3/tv/top_rated?api_key={api_key}&language=en-US&page=1'
    response = requests.get(top_rated_url)
    data = response.json()
    top_rated_tv_shows = data['results']

    title = 'Tv Shows'

    return render(request,'tv_shows.html',{'trending_tv_shows':trending_tv_shows,'airing_today_tv_shows':airing_today_tv_shows,'on_air_tv_shows':on_air_tv_shows,'popular_tv_shows':popular_tv_shows,'top_rated_tv_shows':top_rated_tv_shows,'title':title})


def single_movie(request,movie_id):
    movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    response = requests.get(movie_url)
    movie = response.json()
    # movie = data['results']

    # Similar movies
    similar_movies_url = f'https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key={api_key}&language=en-US&page=1'
    response = requests.get(similar_movies_url)
    data = response.json()
    similar_movies = data['results']

    #Youtube videos
    youtube_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part' : 'snippet',
        'key' : youtube_api_key,
        'maxRsults' : 1,
        'q' :  movie['original_title'] + ' official trailer',
    }

    response = requests.get(youtube_url,params=params)
    data = response.json()
    
    id = data['items'][0]['id']['videoId']
    url = f'https://www.youtube.com/embed/{id}'

    title = f"{movie['original_title']}"
    
    return render(request, 'movie.html', {'movie':movie,'similar_movies':similar_movies,'url':url,'title':title})


def single_tv_show(request,tv_show_id):
    tv_show_url = f'https://api.themoviedb.org/3/tv/{tv_show_id}?api_key={api_key}&language=en-US'
    response = requests.get(tv_show_url)
    tv_show = response.json()
    # movie = data['results']

    # Similar movies
    similar_tv_shows_url = f'https://api.themoviedb.org/3/tv/{tv_show_id}/similar?api_key={api_key}&language=en-US&page=1'
    response = requests.get(similar_tv_shows_url)
    data = response.json()
    similar_tv_shows = data['results']

    #Youtube videos
    youtube_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part' : 'snippet',
        'key' : youtube_api_key,
        'maxRsults' : 1,
        'q' : tv_show['original_name'] + 'official trailer',
    }

    response = requests.get(youtube_url,params=params)
    data = response.json()
    id = data['items'][0]['id']['videoId']
    url = f'https://www.youtube.com/embed/{id}'

    title = f"{tv_show['original_name']}"
    
    return render(request, 'tv_show.html', {'tv_show':tv_show,'similar_tv_shows':similar_tv_shows,'url':url,'title':title})


def search(request):
    search_term = request.GET.get('search_term')
    movies = []
    
    # Page 1
    search_url = f'https://api.themoviedb.org/3/search/multi?api_key={api_key}&language=en-US&query={search_term}&page=1&include_adult=false'
    response = requests.get(search_url)
    data = response.json()
    searched_movies = data['results']
        
    for m in searched_movies:
        if m['media_type'] == 'tv' or m['media_type'] == 'movie':
            movies.append(m)

    # Page 2
    search_url = f'https://api.themoviedb.org/3/search/multi?api_key={api_key}&language=en-US&query={search_term}&page=2&include_adult=false'
    response = requests.get(search_url)
    data = response.json()
    searched_movies = data['results']
        
    for m in searched_movies:
        if m['media_type'] == 'tv' or m['media_type'] == 'movie':
            movies.append(m)

    # Page 3
    search_url = f'https://api.themoviedb.org/3/search/multi?api_key={api_key}&language=en-US&query={search_term}&page=3&include_adult=false'
    response = requests.get(search_url)
    data = response.json()
    searched_movies = data['results']
        
    for m in searched_movies:
        if m['media_type'] == 'tv' or m['media_type'] == 'movie':
            movies.append(m)

    # Page 4
    search_url = f'https://api.themoviedb.org/3/search/multi?api_key={api_key}&language=en-US&query={search_term}&page=4&include_adult=false'
    response = requests.get(search_url)
    data = response.json()
    searched_movies = data['results']
        
    for m in searched_movies:
        if m['media_type'] == 'tv' or m['media_type'] == 'movie':
            movies.append(m)

    title = f"Search '{search_term}'"
    

    return render(request,'search.html',{'movies':movies,'search_term':search_term,'title':title})


def error_404_view(request,exception):

    return render(request,'404.html')