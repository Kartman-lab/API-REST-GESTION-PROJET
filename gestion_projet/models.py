from django.db import models
from django.conf import settings

from authenticate.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Contributor',
        related_name='projects'
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def finish_project(self):
        if self.active == False:
            return
        self.active = False
        self.save()
    


class Contributor(models.Model):
    AUTHOR = 'author'
    CONTRIBUTOR = 'contributor'

    ROLE_CHOICES = (
        (AUTHOR, 'Author'),
        (CONTRIBUTOR, 'Contributor'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributors_details')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user} - {self.project} ({self.role})"


class Issue(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    BUG = 'bug'
    TASK = 'task'
    IMPROVEMENT = 'improvement'

    TAG_CHOICES = (
        (BUG, 'Bug'),
        (TASK, 'Task'),
        (IMPROVEMENT, 'Improvement'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues_details')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issues_created')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='issues_assigned')
    tag = models.CharField(max_length=20, choices=TAG_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, default='to_do')

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comment_details')
    author = models.ForeignKey(Contributor, on_delete=models.CASCADE, null=True )
