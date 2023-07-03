from . import views
from django.urls import path, include

# additional for media urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.MovieListView.as_view(), name='movielist'),
#    path('movie/<int:pk>', views.MovieDetailView.as_view(template_name = 'movie_detail.html'), name='moviedetail'),
    path("movie/<int:movie_id>/", views.movie_detail, name="moviedetail"),
    path("movie/import/", views.movie_import, name="movieimport"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)