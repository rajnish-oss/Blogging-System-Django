from django.urls import path
from . import views

# URL patterns for category routes
urlpatterns = [
    path('<str:category_name>/', views.post_by_category, name='category')
]
