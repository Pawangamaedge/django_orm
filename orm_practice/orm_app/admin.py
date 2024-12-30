from django.contrib import admin
from .models import Musician
from .models import Book
# Register your models here.
admin.site.register(Musician)
admin.site.register(Book)