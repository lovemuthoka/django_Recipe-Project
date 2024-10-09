from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, IngredientViewSet, InstructionViewSet, ReviewViewSet, UserViewSet
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('recipes', RecipeViewSet, basename='recipe')
router.register('ingredients', IngredientViewSet, basename='ingredient')
router.register('instructions', InstructionViewSet, basename='instruction')
router.register('users', UserViewSet, basename='user')
router.register('reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),  
    
]
