
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Review,Category,Recipe, Ingredient, Instruction,  RecipePhoto
   

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password']) 
        user.save()
        return user



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']




class RecipePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipePhoto
        fields = ['id', 'recipe', 'image']



class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity', 'metric']  


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['id','step_number', 'description', 'duration']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField( queryset=Ingredient.objects.all())
    instructions= serializers.PrimaryKeyRelatedField( queryset=Instruction.objects.all())
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'ingredients', 'instructions', 'category', 
                  'prep_time', 'cook_time', 'servings', 'created_date', 'user', 
                  'loaded_images', 'calculated_average_rating']

   


class ReviewSerializer(serializers.ModelSerializer):
     class Meta:
        model = Review
        fields = ['id', 'recipe', 'user', 'rating', 'comment', 'created_at']
