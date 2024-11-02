from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class ClothPosts(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content= models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='cloth_post/uploads/', blank=True, null= True)
    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    cloths = models.ForeignKey(ClothPosts, on_delete= models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f'Comment by{self.name}'
    

STAR_CHOICES=[
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete= models.CASCADE)
    cloth = models.ForeignKey(ClothPosts, on_delete= models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length=50)

    def __str__(self):
        return f'Review by {self.reviewer.user.first_name} for {self.cloth.title}'


class BuyNow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cloth = models.ForeignKey(ClothPosts, on_delete=models.CASCADE)
    buy_date = models.DateTimeField(auto_now_add=True)