from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.dashboard, name='dashboard/home'),
    # Category URLs
    path('category/', views.manage_categories, name='dashboard/category'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
    # Blog URLs
    path('blogs/', views.manage_blogs, name='dashboard/blogs'),
    path('blogs/add/', views.add_blog, name='add_blog'),
    path('blogs/edit/<int:pk>/', views.edit_blog, name='edit_blog'),
    path('blogs/delete/<int:pk>/', views.delete_blog, name='delete_blog'),

]