from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import recipe_list, recipe_detail, custom_login, profile_view

urlpatterns = [
    path("recipes/list", recipe_list, name="recipe_list"),
    path("recipe/<int:recipe_id>", recipe_detail, name="recipe_detail"),

    # Authentication Routes
    path("login/", custom_login, name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),

    # Profile Route (optional)
    path("profile/", profile_view, name="profile"),
]
