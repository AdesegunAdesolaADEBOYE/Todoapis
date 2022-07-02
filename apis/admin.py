from django.contrib import admin

from . import models

# Register your models here.
######### TODO ADMIN #########
@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'deadline',
                    'priority', 'is_done', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


######### COMMENT ADMIN #########
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['todo', 'comment', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


######### REMINDER ADMIN #########
@admin.register(models.Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['todo', 'date', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']

