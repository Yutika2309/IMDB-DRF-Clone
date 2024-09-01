from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.serializers import *
from watchlist_app.models import *
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class MovieListAPIView(APIView):

    def get(self, request):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MovieDetailsAPIView(APIView):

    def get(self, request, pk):
        try:
            movie = Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Response({'error':'Movie does not exist for this ID'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = Movies.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = Movies.objects.get(pk=pk)
        movie.delete()
        return Response({"message":"Data has been deleted"}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movies.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):

#     if request.method == 'GET':
#         try:
#             movie = Movies.objects.get(pk=pk)
#         except Movies.DoesNotExist:
#             return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movies.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         movie = Movies.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
