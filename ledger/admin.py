from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profiles"

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

# Register Profile with User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created_on", "updated_on")  
    list_filter = ("author", "created_on")  
    search_fields = ("name", "author__username")  
    inlines = [RecipeIngredientInline]

admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
