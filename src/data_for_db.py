from src.models import Recipe, IngredientsInRecipe, Ingredient


ingredients = [
    Ingredient(
        ingredient_name="ingredient_1", ingredient_description="description"
    ),
    Ingredient(
        ingredient_name="ingredient_2", ingredient_description="description"
    ),
    Ingredient(
        ingredient_name="ingredient_3", ingredient_description="description"
    ),
]
recipe = [Recipe(recipe_name="Блины постные", cooking_time=20), ]
recipe_ingredients = [
    IngredientsInRecipe(recipe_id=1, ingredient_id=1, quantity="quantity_1"),
    IngredientsInRecipe(recipe_id=1, ingredient_id=2, quantity="quantity_2"),
    IngredientsInRecipe(recipe_id=1, ingredient_id=3, quantity="quantity_3"),
]
