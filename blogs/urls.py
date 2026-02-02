from django.urls import path
from . import views

# URL patterns for blog detail routes
urlpatterns = [
    path('<slug:slug>/', views.get_blog, name='blog_detail'),
    path('add_comment/<slug:slug>/', views.add_comment, name='add_comment')
]
