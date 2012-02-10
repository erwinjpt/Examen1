from django.contrib import admin
from main.models import Author, Article, Comment, Labels

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'last_name', 'birthday',)
	search_fields = ('last_name',)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'body', 'created_at',)
	search_fields = ('title',)

class CommentAdmin(admin.ModelAdmin):
	list_display = ( 'article','name', 'text', 'created_at',)
	search_fields = ('name',)

class LabelsAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Labels, LabelsAdmin)

