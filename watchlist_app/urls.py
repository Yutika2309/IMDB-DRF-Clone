from django.urls import path, include
from watchlist_app.views import *

urlpatterns = [
    path('list/', MovieListAPIView.as_view(), name='movie-list'),
    path('list/<int:pk>', MovieDetailsAPIView.as_view(), name='movie-detail'),
]