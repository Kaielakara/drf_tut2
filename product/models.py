from django.db import models

# Create your models here.
class Item(models.Model):

    ITEM_CATEGORY_CHOICES = (
    ('GN', "General"),
    ('EL', "Electronics"),
    ('HK', "Home & Kitchen"),
    ('FC', "Fashion & Clothing"),
    ('BP', "Beauty & Personal Care"),
    ('SO', "Sports & Outdoors"),
    ('BM', "Books & Media"),
    ('TG', "Toys & Games"),
    ('AU', "Automotive"),
)
    
    name = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length=200)
    price = models.DecimalField(default=1.00, decimal_places=2, max_digits=12)
    category= models.CharField(
        max_length=2,
        choices=ITEM_CATEGORY_CHOICES,
        default='GN',
    )

    def __str__(self):
        return self.name
