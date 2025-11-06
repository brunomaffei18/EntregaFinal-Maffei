from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "priority", "deadline", "user")
    search_fields = ("title", "category", "description", "user__username")
    list_filter = ("deadline", "category")
