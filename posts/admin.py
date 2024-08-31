from django.contrib import admin

from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at', 'views')
    list_filter = ('category', 'created_at', 'author', 'tags')
    search_fields = ('title', 'content', 'author__username', 'tags__name')
    readonly_fields = ('created_at', 'updated_at', 'views')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {'fields': ('title', 'content', 'author', 'category', 'tags', 'image', 'views')}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )

    def save_model(self, request, obj, form, change):
        # Optionally, handle additional processing before saving
        super().save_model(request, obj, form, change)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)
