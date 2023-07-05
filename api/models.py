from django.db import models


class Book (models.Model):
    title = models.CharField(max_length=50, verbose_name="title")
    description = models.TextField(verbose_name="description")
    author = models.CharField(max_length=50, verbose_name="author")
    created_at = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="full_name")
    website = models.URLField(verbose_name="site_url")
    photo = models.ImageField(upload_to="author/", verbose_name="photo")
    about = models.TextField(verbose_name="about")
    created_at = models.DateTimeField(auto_now_add=True)
