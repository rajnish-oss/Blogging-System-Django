from django.shortcuts import render
from blogs.models import Category,Blog

def home(request):
    categories = Category.objects.all()
    featured_blog = Blog.objects.filter(is_featured=True, status=1).order_by('-created_at')
    blog = Blog.objects.filter(status=1).order_by('-created_at').first()

    print(blog)

    context = {
        'categories': categories,
        'featured_blog': featured_blog,
        'blog': blog
    }

    return render(request, 'home.html', context)