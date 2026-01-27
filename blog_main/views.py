from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from django.forms import formset_factory
from blog_main.form import Register
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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


MyFormSet = formset_factory(Register, extra=1)

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = Register()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')