from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'published')
    list_display_links = ['text']
    search_fields = ('text', 'published')


admin.site.register(Post, PostAdmin)