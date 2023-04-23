from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import criticSerializers
from MoviesApp.models import Movie, Critic

from rest_framework import permissions

# Create your views here.

# endpoint /critic/<pk>
class CriticsByMovie(APIView):

# read all request
    def get(self, request, pk):

        movie = get_object_or_404(Movie, id = pk)
        critics = Critic.objects.filter(movie = movie.id)
        serialize = criticSerializers(critics, many = True)

        return Response(serialize.data)

class CriticsByID(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# create request
    def post(self, request):

        serialize_obj = criticSerializers(data = request.data)

        if serialize_obj.is_valid():
            serialize_obj.save(author = self.request.user)
            return Response(serialize_obj.data, status = status.HTTP_201_CREATED)

        return Response(serialize_obj.errors, status = status.HTTP_400_BAD_REQUEST)
