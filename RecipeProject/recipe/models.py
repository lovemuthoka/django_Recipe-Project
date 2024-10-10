from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255)

    PREDEFINED_CATEGORIES = [
        ('Appetizers', 'Appetizers'),
        ('Main Dishes', 'Main Dishes'),
        ('Breads', 'Baked Goods'),
        ('Desserts', 'Desserts'),
        ('Salads', 'Sides'),
        ('Pasta', 'Pasta'),
        ('Healthy Option', 'Healthy Option'),
        ('Not Specified', 'Not Specified'),
    ]

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name

    @receiver(post_migrate)
    def check_categories(sender, **kwargs):
        if sender.name == 'recipe': 
            if Category.objects.count() == 0:
                for category_code, category_name in Category.PREDEFINED_CATEGORIES:
                    Category.objects.get_or_create(name=category_name)

class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=False)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description if self.description else f"Image {self.id}"

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)
    metric = models.CharField(max_length=20, choices=[
        ('GRAMS', 'Grams'),
        ('KILOGRAMS', 'Kilograms'),
        ('MILLILITERS', 'Milliliters'),
        ('LITERS', 'Liters'),
        ('TEASPOONS', 'Teaspoons'),
        ('TABLESPOONS', 'Tablespoons'),
        ('CUPS', 'Cups'),
        ('OUNCES', 'Ounces'),
        ('POUNDS', 'Pounds'),
        ('PIECES', 'Pieces'),
        ('DEFAULT', 'Not Specified'),
    ], default='DEFAULT')

    def __str__(self):
        return f"{self.quantity} {self.get_metric_display()} of {self.name}"
    
   


class Instruction(models.Model):
    step_number = models.PositiveIntegerField()
    description = models.TextField()
    duration = models.DurationField(null=True, blank=True)

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.description}"

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE,related_name='recipes',null=True)   
    instructions = models.ForeignKey(Instruction,on_delete=models.CASCADE,related_name='recipes',null=True)  
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prep_time = models.PositiveIntegerField(help_text="Preparation time in minutes")
    cook_time = models.PositiveIntegerField(help_text="Cooking time in minutes")
    servings = models.PositiveIntegerField(help_text="Number of servings")
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    loaded_images = models.ManyToManyField(Image, blank=True, related_name='recipes')
    calculated_average_rating = models.FloatField(default=0)  

    def __str__(self):
        return self.title

class RecipePhoto(models.Model):
    image = models.ImageField(upload_to='recipe_photos')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description if self.description else f"Photo {self.id}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ( 'user')

    def __str__(self):
        return f"{self.user.username} - {self.rating})"
