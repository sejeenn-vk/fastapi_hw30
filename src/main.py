from typing import List

import uvicorn
from fastapi import FastAPI

from src.database import add_data, add_recipe, all_recipes, detail_recipe
from src.models import IngredientsInRecipe, Recipe
from src.schemas import RecipeDetail, RecipeIn, RecipeOut

app = FastAPI()


@app.get("/")
def main_page():
    return {"msg": "Main page"}


@app.get("/recipes", response_model=List[RecipeOut])
async def get_all_recipes():
    result = await all_recipes()
    return result.scalars().all()


@app.get("/recipes/{recipe_id}", response_model=List[RecipeDetail])
async def get_recipe_details(recipe_id):
    recipe_with_ingredients = await detail_recipe(recipe_id)
    return recipe_with_ingredients


@app.post("/recipes", response_model=RecipeIn)
async def add_new_recipe(recipe: RecipeIn):
    new_recipe = Recipe(
        recipe_name=recipe.recipe_name,
        cooking_time=recipe.cooking_time,
        recipe_description=recipe.recipe_description,
    )
    ingredients = recipe.ingredients
    new_recipe_id = await add_recipe(new_recipe)
    ingredients_in_recipe = [
        IngredientsInRecipe(
            recipe_id=new_recipe_id,
            ingredient_id=i.ingredient_id,
            quantity=i.quantity,
        )
        for i in ingredients
    ]
    if new_recipe_id:
        await add_data(ingredients_in_recipe)
        return recipe


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
