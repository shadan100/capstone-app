from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass

class Recipe(models.Model):

    CATEGORY = (('Breakfast', 'Breakfast'),
                ('Lunch', 'Lunch'),
                ('Dinner', 'Dinner'),
                ('Desserts', 'Desserts'),
                ('Beverages', 'Beverages'),
                ('Salads', 'Salads')
               )

    ingredients = models.TextField(max_length=40000, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    title = models.CharField(max_length=200, null=True)
    img_url = models.URLField(max_length=256)
    description = models.CharField(max_length=256)
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    method = models.TextField(max_length=40000, null=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)

class Favourite(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)