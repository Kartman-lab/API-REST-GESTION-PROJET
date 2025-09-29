from rest_framework.serializers import ModelSerializer

from gestion_projet.models import Project, Contributor, Issue, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

        def create(self, validated_data):
            pass

class ContributorSerializer(ModelSerializer):
    class Meta: 
        model = Contributor
        fields = '__all__'

class IssueSerializer(ModelSerializer):

    comments = CommentSerializer(source='comment_details', many=True)

    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['author', 'project']

        def create(self, validated_data):
            user = self.context['request'].user
            project = self.context.get('project')

            return Issue.object.create(
                author=user,
                project=project,
                **validated_data
            )


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
