from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogForm
from django.utils.text import slugify



# URL patterns for dashboard routes

@login_required(login_url='login')
def dashboard(request):
    blog_count = Blog.objects.all().count()
    category_count = Category.objects.all().count()

    context = {
        'blog_count': blog_count,
        'category_count': category_count
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
def manage_categories(request):
    categories = Category.objects.all()
    context = {
        'category': categories,
    }
    return render(request, 'dashboard/category.html', context)

@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard/category')
    else:
        form = CategoryForm()

    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)



@login_required(login_url='login')
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard/category')
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)


@login_required(login_url='login')
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()

    return redirect('dashboard/category')

def manage_blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'dashboard/blogs.html', context)


from django.utils.text import slugify

@login_required(login_url='login')
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.slug = slugify(blog.title)
            blog.save()
            return redirect("{% url 'dashboard/blogs/' %}")
        else:
            print(f'Form errors: {form.errors}')
    else:
        form = BlogForm()

    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_blog.html', context)

def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('dashboard/blogs')
    else:
        form = BlogForm(instance=blog)

    context = {
        'form': form,
        'blog': blog,
    }
    return render(request, 'dashboard/edit_blog.html', context)

def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()

    return redirect('dashboard/blogs')