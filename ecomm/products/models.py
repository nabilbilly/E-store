from django.db import models

from base.models import *
from .PhotoResize import compress_image, save_image

class Category(BaseModel):
    category_name= models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True )
    category_image= models.ImageField( upload_to="categories")
    
    
    def save(self, *args, **kwargs):
        self.category_image = compress_image(self.category_image)
        super(Category, self).save(*args, **kwargs)
    
    
    
class Product(BaseModel):
    product_name = models.CharField( max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True )
    Category = models.ForeignKey( Category, on_delete= models.CASCADE, related_name= "product")
    price = models.IntegerField()
    project_description = models.TextField()


    
class ProductImage(BaseModel):
    Product = models.ForeignKey( Product, on_delete= models.CASCADE, related_name= "Product")
    image = models.ImageField(upload_to="Product")

    def save(self, *args, **kwargs):
        save_image(self, *args, **kwargs)