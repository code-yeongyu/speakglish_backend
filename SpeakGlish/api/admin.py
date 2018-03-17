from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin) :
    list_display = ('created', 'writer', 'doneAt', 'content', 'timer', 'timerLeft')
    search_fields = ['created', 'writer', 'doneAt', 'content', 'timer', 'timerLeft']

admin.site.register(Article, ArticleAdmin)