from django.db import models


# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
