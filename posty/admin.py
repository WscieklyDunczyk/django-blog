from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'status', 'autor', 'data_dodania', 'data_edytowania')
    list_filter = ('data_dodania',)
    prepopulated_fields = {'slug': ('tytul',)}


# Register your models here.
admin.site.register(Post, PostAdmin)
