from rest_framework import serializers
from watchlist_app.models import *


class WatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):

    # watchlist = WatchlistSerializer(many=True, read_only=True) # shows the queryset for the whole model (all fields essentially)

    #different types of relations include - StringRelatedField (shows only string fields), PrimaryKeyRelatedField (shows only pk)
    #the following is a hyperlinked field, which will redirect us to the endpoint (possibly with pk) directly.
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='watchlist-detail'
    )  

    class Meta:
        model = StreamPlatform
        fields = '__all__'



# class MovieSerializer(serializers.ModelSerializer):

    # len_name = serializers.SerializerMethodField()

    # class Meta:
    #     model = WatchList
    #     fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['created_at', 'updated_at']

    # def get_len_name(self, instance):
    #     length = len(instance.name)
    #     return length

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
    
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Movie Name and Description cannot be the same")
    #     else:
    #         return data 
