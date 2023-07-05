from django.shortcuts import render
from . import serializer
from rest_framework.generics import ListAPIView
from . import models
from rest_framework.filters import SearchFilter


class BookListAPIView(ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("title",)


class AuthorListAPIView(ListAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializer.AuthorSerialezer
    filter_backends = (SearchFilter,)
    search_fields = ("full_name",)

