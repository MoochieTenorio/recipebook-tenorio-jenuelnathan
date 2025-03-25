from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Recipe, RecipeImage


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


class RecipeImageInline(admin.TabularInline):  # Shows RecipeImages inline in RecipeAdmin
    model = RecipeImage
    extra = 1  # Allows adding images directly from the Recipe page


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInline]  # Attach RecipeImage inline to RecipeAdmin


# Register models in Django admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)  # Register Recipe with inline images
admin.site.register(RecipeImage)  # Register RecipeImage separately
