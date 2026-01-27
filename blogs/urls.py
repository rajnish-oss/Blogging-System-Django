from django.urls import path
from . import views

# URL patterns for blog detail routes
urlpatterns = [
    path('<slug:slug>/', views.get_blog, name='blog_detail')
]
