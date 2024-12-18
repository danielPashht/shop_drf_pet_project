from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	search_fields = ('name', 'slug')


admin.site.register(Category, CategoryAdmin)
