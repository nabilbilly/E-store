from django.contrib import admin
from .models import *
from base.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
# admin.site.register(BaseModel)


