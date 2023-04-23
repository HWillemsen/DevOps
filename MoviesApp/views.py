from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# additional imports
from .forms import CriticForm
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
        # Add in a QuerySet of all the books
        context['critic_list'] = Critic.objects.filter(movie = movie.id)
        return context

# List one movie and create critics
def movie_detail(request, movie_id):

    movie = get_object_or_404(Movie, id = movie_id)
    critic_list = Critic.objects.filter(movie = movie.id)

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
