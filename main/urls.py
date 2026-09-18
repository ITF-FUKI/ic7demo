from django.urls import path

from . import views

urlpatterns = [
    path("", views.authors, name="authors"),
    path("author/<int:author_id>/", views.books, name="books"),
]