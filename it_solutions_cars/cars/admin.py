from django.contrib import admin

from .models import Car, Comment


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'make', 'model', 'year', 'description', 'created_at', 'updated_at', 'owner')
    search_fields = ('make', 'model',)
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at',)
    empty_value_display = '-пусто-'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'content', 'created_at',)
    search_fields = ('author', 'content',)
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'

admin.site.register(Car, CarAdmin)
admin.site.register(Comment, CommentAdmin)