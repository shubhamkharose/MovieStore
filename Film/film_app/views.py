from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from .decorators import validate_request_data
from .models import Movie
from .serializers import MovieSerializer


#FilmId FilmName Genre Studio Director Producer LeadActor

class ListCreateMovieView(generics.ListCreateAPIView):
    """
    GET movies/
    POST movies/
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_movie = Movie.objects.create(
            FilmId=request.data["FilmId"],
            FilmName=request.data["FilmName"],
            Genre=request.data["Genre"],
            Studio=request.data["Studio"],
            Director=request.data["Director"],
            Producer=request.data["Producer"],
            LeadActor=request.data["LeadActor"]
        )
        return Response(
            data=MovieSerializer(a_movie).data,
            status=status.HTTP_201_CREATED
        )


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET movies/:id/
    PUT movies/:id/
    DELETE movies/:id/
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_movie = self.queryset.get(FilmId=kwargs["pk"])
            return Response(MovieSerializer(a_movie).data)
        except Movie.DoesNotExist:
            return Response(
                data={
                    "message": "Movie with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_movie = self.queryset.get(FilmId=kwargs["pk"])
            serializer = MovieSerializer()
            updated_movie = serializer.update(a_movie, request.data)
            return Response(MovieSerializer(updated_movie).data)
        except Movie.DoesNotExist:
            return Response(
                data={
                    "message": "Movie with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_movie = self.queryset.get(FilmId=kwargs["pk"])
            a_movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response(
                data={
                    "message": "Movie with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
