from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150, null=True, blank=True)
    website = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField()
    storyline = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title











# class Movies(models.Model):
#     name = models.CharField(max_length=20)
#     year = models.IntegerField()
#     description = models.CharField(max_length=500)
#     active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True)

#     class Meta:
#         ordering = ['created_at']

#     def __str__(self):
#         return self.name