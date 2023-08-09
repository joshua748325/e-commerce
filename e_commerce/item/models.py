from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering=['name']
        verbose_name_plural="Categories"

    def __str__(self):
        return f"{self.name}"

class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=32,decimal_places=2)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)

    class Meta:
        ordering=['-created_by']
    
    def __str__(self):
        return f"{self.name}"