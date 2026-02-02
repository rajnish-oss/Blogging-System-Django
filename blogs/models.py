from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class StatusChoices(models.IntegerChoices):
        DRAFT = 0, "Draft"
        PUBLISH = 1, "Publish"
        
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) #auth.User(max_length=255)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    description = models.TextField(max_length=255)
    status = models.IntegerField(choices=StatusChoices, default=StatusChoices.DRAFT)
    is_featured = models.BooleanField(default=False)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     
     