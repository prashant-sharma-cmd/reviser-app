from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

from taggit.managers import TaggableManager

class Decks(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    description = models.TextField(max_length=500, validators=[MinLengthValidator(10)])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

CARD_CHOICES = [
    ("1", "Basic"),
    ("2", "Reverse"),
    ("3", "Basic and Reverse "),
    ("4", "Type in Answer"),
]

class Cards(models.Model):
    deck = models.ForeignKey('Decks', on_delete=models.CASCADE, null=False)
    type = models.CharField(max_length=2, choices=CARD_CHOICES, default="1")
    front = models.CharField(max_length=1000, validators=[MinLengthValidator(3)])
    back = models.CharField(max_length=1000, validators=[MinLengthValidator(3)])
    detailed_info = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    def __str__(self):
        return f"{self.front} | {self.back}"