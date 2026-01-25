from django.contrib import admin
from .models import Category,Blog

class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','status','is_featured','category__name','author__username')
    search_fields = ('id','title','category__name','author__username')


# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,blogAdmin)