from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    notes=models.TextField()
    books=ManyToManyField(Book,related_name="authors")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
