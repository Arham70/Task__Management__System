from django.contrib import admin
from .models import ProjectModel, TaskModel


@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ProjectDescription', 'ProjectCreated_at')


@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'title', 'TaskDescription', 'status', 'TaskCreated_at')

# Register your models here.
