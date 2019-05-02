from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=200)
    first2lines = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    author = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.title


    
