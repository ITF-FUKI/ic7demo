from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
