from django.contrib import admin

# Register your models here.
from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category_id', 'created_at', 'updated_at', 'is_public')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_public',)
    list_filter = ('is_public', 'category_id')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')
    list_display_links = ('id', 'name_category')
    search_fields = ('name_category',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
