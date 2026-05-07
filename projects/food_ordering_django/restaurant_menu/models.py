from django.db import models
from django.contrib.auth.models import User



meal_type=(
    ("starters","Starters"),
    ("salads","Salads"),
    ("main_dishes","Main_dishes"),
    ("desserts","Desserts")
)
STATUS=(
    (0,"Unavailable"),
    (1,"Available")
)
# Create your models here.
class Item(models.Model):
    db_table = "restaurant_menu_items"
    meal=models.CharField(max_length=1000,unique=True)
    description=models.CharField(max_length=2000)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    meal_type=models.CharField(max_length=200,choices=meal_type)
    author=models.ForeignKey(User,on_delete=models.PROTECT)
    status=models.IntegerField(choices=STATUS,default=1)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.meal
