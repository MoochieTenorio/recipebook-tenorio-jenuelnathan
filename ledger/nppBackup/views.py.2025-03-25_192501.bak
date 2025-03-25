from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, RecipeImage  
from .forms import RecipeForm, RecipeImageForm  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

@login_required(login_url="/accounts/login/")
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})

@login_required(login_url="/accounts/login/")
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  
            recipe.save()
            return redirect("recipe_detail", recipe_id=recipe.id)  
    else:
        form = RecipeForm()
    return render(request, "ledger/recipe_form.html", {"form": form})

class AddRecipeImageView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "ledger/add_recipe_image.html"

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']  
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"recipe_id": self.kwargs['pk']})
