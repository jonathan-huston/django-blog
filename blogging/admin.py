from django.contrib import admin
from blogging.models import Post, Category


class CategoryInLine(admin.TabularInline):
    model = Post.categories.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
    ]
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
