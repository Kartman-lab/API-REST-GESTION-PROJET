from rest_framework.serializers import ModelSerializer

from gestion_projet.models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class ContributorSerializer(ModelSerializer):
    class Meta: 
        model = Contributor
        fields = '__all__'

class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'