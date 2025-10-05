from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from gestion_projet.models import Project, Contributor, Issue, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ContributorSerializer(ModelSerializer):
    class Meta: 
        model = Contributor
        fields = '__all__'

class IssueSerializer(ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['author', 'project']

    def create(self, validated_data):
        user = self.context['request'].user
        project = self.context.get('project')

        return Issue.objects.create(
            author=user,
            project=project,
            **validated_data
        )
    
    def get_comments(self, obj):
        request = self.context.get('request')
        project = obj.project

        if not request or not request.user.is_authenticated:
            return []
        
        author_or_contrib = (
            project.author == request.user or 
            project.contributors.filter(user=request.user).exists()
        )
        
        if author_or_contrib:
            return CommentSerializer(obj.comment_details.all(), many=True).data
        
        return []


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name"]


class ProjectDetailsSerializer(ModelSerializer):

    contributors = ContributorSerializer(source="contributors_details", many=True)
    issues = IssueSerializer(source='issues_details', many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'contributors', 'issues']
