from django.shortcuts import render

from .models import Author


def authors(request):
    authors = Author.objects.prefetch_related("books").order_by("name")
    return render(request, "main/authors.html", {"authors": authors})


def books(request, author_id):
    author = Author.objects.prefetch_related("books").get(pk=author_id)
    return render(request, "main/books.html", {"author": author})