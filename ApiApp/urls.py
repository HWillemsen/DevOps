from . import views
from django.urls import path, include

# define patterns
urlpatterns = [
    path('critic/', views.CriticsByID.as_view()),
    path('critic/<int:pk>', views.CriticsByMovie.as_view()),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]