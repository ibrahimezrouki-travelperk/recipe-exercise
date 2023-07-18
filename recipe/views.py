from django.shortcuts import render
from rest_framework import viewsets

from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        recipe_name = self.request.query_params.get("name")

        if recipe_name is not None:
            # change queryset to filter by recipe name
            queryset = queryset.filter(name__contains=recipe_name)

        return queryset
