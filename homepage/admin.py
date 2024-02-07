from django.contrib import admin
from .models import HomePage
from django.utils.html import format_html


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_preview', 'display_image')  # Customize the fields displayed in the list view

    def content_preview(self, obj):
        # Display a preview of content (e.g., first 50 characters)
        return obj.main_text[:50] + '...' if len(obj.main_text) > 50 else obj.main_text

    content_preview.short_description = 'Content Preview'  # Customize the column header

    def display_image(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" style="max-width:100px; max-height:100px;" />', obj.main_image.url)
        else:
            return 'No Image'
    
    display_image.allow_tags = True
    def has_add_permission(self, request):
        return False  # Disables the ability to add new objects

admin.site.register(HomePage, HomePageAdmin)