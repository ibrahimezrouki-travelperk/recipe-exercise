from django.test import TestCase

from recipe.models import Recipe, Ingredient


class RecipeModelTests(TestCase):

    def test_string_of_recipe_name_returned(self):
        recipe = Recipe.objects.create(name='A recipe name', description='Some descriptive description')
        self.assertEqual(str(recipe), recipe.name)

    def test_string_of_ingredient_name_returned(self):
        recipe = Recipe.objects.create(name='A recipe name', description='Some descriptive description')
        ingredient = Ingredient.objects.create(name='cheese', recipe=recipe)
        self.assertEqual(str(ingredient), ingredient.name)
