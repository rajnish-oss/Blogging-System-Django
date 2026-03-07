from django.contrib import admin
from .models import Category, Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'title',
        'category',
        'status',
        'is_featured',
        'category_name',
        'author_username',
    )
    search_fields = (
        'id',
        'title',
        'category__name',     # allowed here
        'author__username',   # allowed here
    )

    def category_name(self, obj):
        return obj.category.name
    category_name.short_description = 'Category'
    category_name.admin_order_field = 'category__name'

    def author_username(self, obj):
        return obj.author.username
    author_username.short_description = 'Author'
    author_username.admin_order_field = 'author__username'


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)