from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=20)
    year = models.IntegerField()
    description = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name