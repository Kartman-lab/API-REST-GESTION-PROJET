from rest_framework.permissions import BasePermission, SAFE_METHODS
from gestion_projet.models import Project, Contributor, Issue, Comment

class IsAuthorOrReadOnly(BasePermission):
    message = "Vous devez être l'auteur du projet pour effectuer cette action."
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user 

class IsCollaboratorOrReadOnly(BasePermission):
        message = "Vous devez être collaborateur au projet pour effectuer cette action."
        def has_permission(self, request, view):
            if request.method in SAFE_METHODS:
                return True
            
            if view.action in ["create", "list", "retrieve"]:
                return True
        
            project_id = request.data.get("project")
            if not project_id:
                return False
            
            project = Project.objects.get(id=project_id)
            return project.contributors.filter(user=request.user).exists()
    
        def has_object_permission(self, request, view, obj):
             if request.method in SAFE_METHODS:
                  return True 
             return obj.contributors.filter(user=request.user).exists()
                
            
        