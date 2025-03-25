from django.urls import path
from .views import recipe_list, recipe_detail, AddRecipeImageView

urlpatterns = [
    path("recipes/list/", recipe_list, name="recipe_list"),
    path("recipe/<int:recipe_id>/", recipe_detail, name="recipe_detail"),
    path("recipe/<int:pk>/add_image/", AddRecipeImageView.as_view(), name="add_recipe_image"),
]
