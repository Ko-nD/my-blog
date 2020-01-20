from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text',  'published_date', 'author')
    search_fields = ('text',)
    list_filter = ('published_date',)
    empty_value_display = '-пусто-'

admin.site.register(Post, PostAdmin)



# Register your models here.
