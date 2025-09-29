from django.shortcuts import render
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from gestion_projet.models import Project, Contributor, Issue, Comment
from gestion_projet.serializers import ProjectListSerializer, ProjectDetailsSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from gestion_projet.permissions import IsAuthorOrReadOnly, IsCollaboratorOrReadOnly


# Create your views here.

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailsSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsCollaboratorOrReadOnly]

    def get_queryset(self):
        return Project.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    @action(detail=True, methods=['post'])
    def finish_project(self, request, pk):
        project = self.get_object()
        project.finish_project()
        return Response(status=status.HTTP_200_OK)
    
        
class MyProjectsViewSet(ModelViewSet):
    serializer_class = ProjectListSerializer
    permission_classes =[IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Project.objects.filter(author=self.request.user)
    
class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Contributor.objects.filter(project_id=project_id)
    
    @action(detail=True, methods=['post'])  
    def add_contributor(self, request, pk):
        project = self.get_object()
        serializer = ContributorSerializer(data=request.data,  context={'request': request, 'project': project})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
 

class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsCollaboratorOrReadOnly]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Issue.objects.filter(project_id=project_id)
    
    
class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsCollaboratorOrReadOnly]

    def get_queryset(self):
        issue_id = self.kwargs.get('issue_pk')
        return Comment.objects.filter(issue_id = issue_id)
    
def home_view(request):
    return render(request, 'gestion_projet/home.html')