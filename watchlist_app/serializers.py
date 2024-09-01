from rest_framework import serializers
from watchlist_app.models import *


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = "__all__"

# def name_length(value):
#     if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#     else:
#         return value
    
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     year = serializers.IntegerField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movies.objects.create(**validated_data) 
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data('name', instance.name)
#         instance.year = validated_data('year', instance.year)
#         instance.description = validated_data('description', instance.description)
#         instance.active = validated_data('active', instance.active)

#         instance.save()
#         return instance

#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return value
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Movie Name and Description cannot be the same")
#         else:
#             return data 