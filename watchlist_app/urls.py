from django.urls import path, include
from watchlist_app.views import *

urlpatterns = [
    path('list/', WatchListAPIView.as_view(), name='watchlist-list'),
    path('list/<int:pk>', WatchListDetailsAPIView.as_view(), name='watchlist-detail'),
    path('stream/', StreamPlatformAPIView.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailApiView.as_view(), name='stream-detail')
]