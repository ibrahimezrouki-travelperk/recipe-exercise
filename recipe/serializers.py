from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from recipe.models import Recipe, Ingredient


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'ingredients']
        read_only_fields = ['id']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        # could do validate this way, but I wonder if utilizing validate method is more 'pythonic'
        # if not ingredients_data:
        #     raise ValidationError("A recipe needs at least one ingredient")
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient)
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        # if not ingredients_data:
        #     raise ValidationError("A recipe needs at least one ingredient")
        instance.ingredients.all().delete()
        for ingredient in ingredients_data:
            Ingredient.objects.create(recipe=instance, **ingredient)

        instance = super().update(instance, validated_data)
        return instance

    def validate(self, attrs):
        ingredients = attrs.get('ingredients', [])
        if not ingredients and self.context['request'].method == 'PUT':
            raise ValidationError("A recipe needs at least one ingredient")
        if not ingredients and self.context['request'].method == 'POST':
            raise ValidationError("A recipe needs at least one ingredient")
        return attrs

