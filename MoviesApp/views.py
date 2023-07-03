from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
import requests

# additional imports
from .forms import CriticForm, MovieNameForm
from .models import Movie, Critic

# display views
from django.views.generic import ListView, DetailView

# Create your views here.
# List all Movies
class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'alldata'

# List one movie
class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        movie = context['object']
        # Add in a QuerySet of all the critics
        context['critic_list'] = Critic.objects.filter(movie = movie.id)
        return context

# List one movie and create critics
def movie_detail(request, movie_id):

    movie = get_object_or_404(Movie, id = movie_id)
    critic_list = Critic.objects.filter(movie = movie.id)

    # check if user is logged in
    if request.user.is_active:

        if request.method == "POST":
            critic_form = CriticForm(request.POST)

            if critic_form.is_valid():
                critic = critic_form.save(commit=False)
                critic.movie = movie
                critic.author = request.user
                critic.save()
                return redirect(request.path_info)

        else:
            critic_form = CriticForm()

    else:
        critic_form = None

    return render(request, "movie_detail.html", {"object": movie, "critic_form": critic_form, "critic_list" : critic_list})

# import new movie
#def movie_import(request):
#    return render(request, "movie_import.html")

def movie_import(request):

    # check if user is admin
    if request.user.is_superuser:

        if request.method == "POST":
            movie_form = MovieNameForm(request.POST)

            if movie_form.is_valid():
                # check if already exist
                if Movie.objects.filter(imdbID = movie_form.cleaned_data["MovieID"]).exists():
                    MovieMessage = "IMDb ID " + movie_form.cleaned_data["MovieID"] + " already imported"
                    messages.info(request, MovieMessage)
                else:
                    # read IMdb
                    payload = {'i': movie_form.cleaned_data["MovieID"], 'apikey': 'f2f74e25'}
                    r = requests.get('http://www.omdbapi.com/', params = payload)
                    # check if MovieID is valid
                    if r.status_code != 200 or r.json()["Response"] != 'True':
                        MovieMessage = "IMDb ID " + movie_form.cleaned_data["MovieID"] + " does not exist: " + r.text
                        messages.error(request, MovieMessage)
                    else:
                        # request is blocked by the whitelist used by pythonanywhere
#                        # get the poster file
#                        poster = requests.get(r.json()["Poster"])
#                        if poster.status_code:
#                            posterFile = r.json()["imdbID"] + 'jpeg'
#                            fp = open(posterFile, 'wb')
#                            fp.write(poster.content)

#                            fp.close()
                        # import new move
                        newMovie = Movie(imdbID = r.json()["imdbID"],
                                    title = r.json()["Title"],
                                    year = int(r.json()["Year"]),
                                    director = r.json()["Director"],
                                    plot = r.json()["Plot"],
                                    imdbRating = r.json()["imdbRating"])
#                                    moviePic = posterFile
                        newMovie.save()
                        MovieMessage = "IMDb ID " + movie_form.cleaned_data["MovieID"] + " imported successfully"
                        messages.success(request, MovieMessage)

            return redirect(request.path_info)

        else:
            movie_form = MovieNameForm()

    else:
        movie_form = None

    return render(request, "movie_import.html", {"movie_form": movie_form})

