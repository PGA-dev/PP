from django.db import models

# Create your models here.
class Grocery(models.Model):
    groc_item_title = models.CharField(max_length=70, blank=False, default='')
    groc_category = models.CharField(max_length=70, blank=False, default='')
    groc_item_price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    total_budget = models.DecimalField(max_digits=8, decimal_places=2, blank=False, default='')
    grocery_item_budget = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    grocery_url = models.CharField(max_length=200, blank=False, default='')
    image_path = models.CharField(max_length=150, blank=True, null=True) 
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)