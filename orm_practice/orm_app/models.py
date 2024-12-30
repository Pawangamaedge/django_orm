from django.db import models

# Create your models here.

class Musician(models.Model):
     first_name =  models.CharField(max_length=200)
     last_name = models.CharField(max_length=200)
     instrument = models.CharField(max_length=200)
     place = models.CharField(max_length=200)
     charges = models.IntegerField()

     def __str__(self):
          return f"first name: {self.first_name} and {self.last_name}"

class Book(models.Model):
     title = models.CharField(max_length=200)
     auther_name =  models.CharField(unique=True)
     published_date = models.DateTimeField(auto_now_add=True)
     isbn_no = models.CharField(max_length=20, unique=True)

     def __str__(self):
          return f"book title name is: {self.title}"
