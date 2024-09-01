from rest_framework import serializers
from watchlist_app.models import *


class MovieSerializer(serializers.ModelSerializer):

    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = '__all__'
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
