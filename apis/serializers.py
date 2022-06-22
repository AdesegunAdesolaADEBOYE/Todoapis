from django.utils import timezone
from rest_framework import serializers

from todos import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'deadline',
            'priority',
            'is_done',
            'reminders_ids',
            'comments_ids',
        )
        read_only_fields = ('id', 'reminders_ids', 'comments_ids')
        model = models.Todo
        

    def validate_deadline(self, value):
        if (timezone.now() > value):
            raise serializers.ValidationError('deadline must be in the future.')
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = models.Todo
        fields = ('id', 'url', 'todo', 'comment')
        read_only_fields = ('id',)


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = models.Todo
        fields = ('id', 'url', 'todo', 'date')
        read_only_fields = ('id',)

    def validate_date(self, value):
        if (timezone.now() > value):
            raise serializers.ValidationError('date must be in the future.')
        return value

