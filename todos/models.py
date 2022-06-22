from django.db import models
from datetime import datetime, timezone

# Create your models here.

class Todo(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    PRIORITY_CHOICES = ((LOW, 'Low'), (MEDIUM, 'Medium'), (HIGH, 'High'))

    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<todo: {self.title}>'
    
    class Meta:
        ordering = ('-priority',)
        verbose_name = 'todo'
        verbose_name_plural = 'todos'


class Reminder(models.Model):
    todo = models.ForeignKey('Todo', related_name='reminders_ids', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<reminder: {self.date}>'

    class Meta:
        ordering = ('-date',)
        verbose_name = 'reminder'
        verbose_name_plural = 'reminders'


class Comment(models.Model):
    todo = models.ForeignKey('Todo', related_name='comments_ids', on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<comment: {self.comment}>'

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

