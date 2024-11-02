from django.contrib import admin
from .models import ClothPosts,Comment,Review,BuyNow
# Register your models here.

admin.site.register(ClothPosts)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(BuyNow)
