from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from gestion_projet.models import Project, Contributor, Issue, Comment

from gestion_projet.serializers import ProjectListSerializer, ProjectDetailsSerializer, ContributorSerializer, IssueSerializer, CommentSerializer




# Create your views here.

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailsSerializer

    def get_queryset(self):
        return Project.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
    
class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Contributor.objects.filter(project_id=project_id)

class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Issue.objects.filter(project_id=project_id)
    
class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        issue_id = self.kwargs.get('issue_pk')
        return Comment.objects.filter(issue_id = issue_id)
