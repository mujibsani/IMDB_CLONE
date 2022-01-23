from .models import Movie


def slider_movies(request):
    movies = Movie.objects.last()
    return {'slider_movies': movies}