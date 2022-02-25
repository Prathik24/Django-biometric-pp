from django.db import models

# Create your models here.
class todo(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
