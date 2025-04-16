from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'created_date')
    list_filter = ('completed', 'created_date', 'user')
    search_fields = ('title', 'description')
    ordering = ('-created_date',)
