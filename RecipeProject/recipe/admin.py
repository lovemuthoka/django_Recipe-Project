from django.contrib import admin
from .models import Recipe

admin.site.register(Recipe)

from django.contrib import admin
from .models import Ingredient



@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'metric')
