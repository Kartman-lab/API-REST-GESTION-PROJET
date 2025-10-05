from django.contrib import admin
from .models import Project, Contributor, Issue, Comment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'issue', 'author']

@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'role']
    list_filter = ['role']
    search_fields = ['user__username', 'project__name']


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'author', 'assignee', 'priority', 'tag', 'status']
    list_filter = ['priority', 'tag', 'status']
    search_fields = ['title', 'project__name', 'author__username', 'assignee__username']
