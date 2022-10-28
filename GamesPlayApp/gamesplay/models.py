from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Profile(models.Model):
    MAX_LEN_PASS = 30
    MAX_LEN_NAME = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=MinValueValidator(12),
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_PASS,
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LEN_NAME,
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LEN_NAME,
    )

    profile_picture_url = models.URLField(
        blank=True,
        null=True,
    )


class Game(models.Model):
    MAX_LEN_TITLE = 30
    MAX_LEN_CATEGORY = 15
    CATEGORY_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    title = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_TITLE,
        unique=True,
    )

    category = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_CATEGORY,
        choces=CATEGORY_CHOICES,
    )