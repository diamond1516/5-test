from rest_framework.serializers import ModelSerializer
from . import models


class BookSerializer(ModelSerializer):

    class Meta:
        model = models.Book
        fields = ("id", "title", "author", "created_at")


class AuthorSerialezer(ModelSerializer):

    class Meta:
        model = models.Author
        fields = ("id", "photo", "full_name", "created_at")
