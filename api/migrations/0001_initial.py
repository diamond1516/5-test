# Generated by Django 4.2.3 on 2023-07-05 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='full_name')),
                ('website', models.URLField(verbose_name='site_url')),
                ('photo', models.ImageField(upload_to='author/', verbose_name='photo')),
                ('about', models.TextField(verbose_name='about')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('author', models.CharField(max_length=50, verbose_name='author')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
