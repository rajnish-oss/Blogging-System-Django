from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from . models import Category, Blog, Comment
from . forms import CommentForm


# Create your views here.
def post_by_category(request, category_name):
    # Check if category exists, if not raise 404
    category = get_object_or_404(Category, name=category_name)
    blogs = Blog.objects.filter(category=category, status=1).order_by('-created_at')
    categories = Category.objects.all()

    context = {
        'blogs': blogs,
        'categories': categories,
        'category_name': category_name
    }

    return render(request, 'post_by_category.html', context)

def get_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status=1)
    categories = Category.objects.all()
    comments = Comment.objects.filter(blog__slug = slug)
    form = CommentForm()
    comment = Comment.objects.first()
    print(f"Comments: {comment}") # Print the comments (comments.first())

    context = {
        'blog': blog,
        'categories': categories,
        'comments': comments,
        'form': form,
    }

    return render(request, 'blog.html', context)

def search_blog(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter(Q(title__icontains = keyword) | Q(description__icontains = keyword) | Q(content__icontains = keyword) | Q(author__username__icontains = keyword) | Q(status = 1))

    context = {
        'blogs':blogs
    }

    return render(request,'search_result.html',context)

def add_comment(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', slug=slug)
    return redirect('blog_detail', slug=slug)