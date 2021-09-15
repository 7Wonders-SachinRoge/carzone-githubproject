from django.db import models

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=126)
    last_name = models.CharField(max_length=126)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    designation = models.CharField(max_length=256)
    facebook = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    linkedIn = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
