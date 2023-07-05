from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.BookListAPIView.as_view()),
    path("author/", views.AuthorListAPIView.as_view())
]