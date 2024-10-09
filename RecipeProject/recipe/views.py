from django.db.models import Avg  
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status, filters
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from .models import Recipe, Ingredient, Instruction, Review, User
from .serializers import RecipeSerializer, IngredientSerializer, InstructionSerializer, ReviewSerializer, UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'category__name', 'ingredients__name', 'prep_time']
    filterset_fields = ['cook_time', 'servings', 'prep_time']


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]


class InstructionViewSet(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer  
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  


class PopularRecipesView(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Recipe.objects.annotate(average_rating=Avg('reviews__rating')).order_by('-average_rating')




