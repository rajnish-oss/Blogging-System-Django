from django.urls import path
from . import views

urlpatterns = [
    path('<str:category_name>/',views.post_by_category)
]