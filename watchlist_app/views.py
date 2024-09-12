from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.serializers import *
from watchlist_app.models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
# Create your views here.

'''
description: API Views for Watchlist
'''
class WatchListAPIView(APIView):

    def get(self, request):
        content = WatchList.objects.all()
        serializer = WatchlistSerializer(content, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchListDetailsAPIView(APIView):

    def get(self, request, pk):
        try:
            content = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Content does not exist for this ID'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchlistSerializer(content)
        return Response(serializer.data)
    
    def put(self, request, pk):
        content = WatchList.objects.get(pk=pk)
        serializer = WatchlistSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        content = WatchList.objects.get(pk=pk)
        content.delete()
        return Response({"message":"Data has been deleted"}, status=status.HTTP_204_NO_CONTENT)


'''
description: API Views for Streaming platform
'''
class StreamPlatformAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        platform = StreamPlatform.objects.all()
        # serializer = StreamPlatformSerializer(platform, many=True, context={"request": request}) #context is required for hyperlink model serializer
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Streaming platform does not exist for this ID'}, status=status.HTTP_404_NOT_FOUND)
        
        # serializer = StreamPlatformSerializer(platform, many=True, context={"request": request}) #context is required for hyperlink model serializer
        serializer = StreamPlatformSerializer(stream_platform, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk, *args, **kwargs):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        stream_platform.delete()
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
