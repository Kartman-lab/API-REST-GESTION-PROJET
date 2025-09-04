"""
URL configuration for api_rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers

from gestion_projet import views

router = routers.SimpleRouter()
router.register('project', views.ProjectViewSet, basename='project')

# Nested router pour les projets
projects_router = routers.NestedSimpleRouter(router, 'project', lookup='project')
projects_router.register('contributors', views.ContributorViewSet, basename='project-contributors')
projects_router.register('issue', views.IssueViewSet, basename='project-issue')

# Nested router pour les commentaires, parent = 'issue' (nom de route enregistré dans projects_router)
issues_router = routers.NestedSimpleRouter(projects_router, 'issue', lookup='issue')
issues_router.register('comments', views.CommentViewSet, basename='issue-comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),           # /api/project/
    path('api/', include(projects_router.urls)),  # /api/project/<project_pk>/contributors/ et /issues/
    path('api/', include(issues_router.urls)),    # /api/project/<project_pk>/issue/<issue_pk>/comments/
]