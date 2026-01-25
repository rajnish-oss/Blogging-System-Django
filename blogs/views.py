from django.shortcuts import render
from . models import Category, Blog

# Create your views here.
def post_by_category(request, category_name):
    blogs = Blog.objects.filter(category__name=category_name, status=1).order_by('-created_at')
    categories = Category.objects.all()

    context = {
        'blogs': blogs,
        'categories': categories,
        'category_name': category_name
    }

    return render(request, 'post_by_category.html', context)