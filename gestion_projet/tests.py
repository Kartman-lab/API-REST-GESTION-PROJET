from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

from gestion_projet.models import Project
from gestion_projet.permissions import IsAuthorOrReadOnly


User = get_user_model()


class ProjectPermissionTests(APITestCase):
    def setUp(self):
        # Utilisateurs
        self.author = User.objects.create_user(username='author', password='pass123')
        self.other = User.objects.create_user(username='other', password='pass123')
        self.admin = User.objects.create_superuser(username='admin', password='pass123')

        # Projet
        self.project = Project.objects.create(name='Test Project', author=self.author)

        # Factory pour tests unitaires de permission
        self.factory = APIRequestFactory()

    # ---------- Tests unitaires de la permission ----------
    def test_permission_non_athenticated_user(self):
         request = self.factory.put(f'/projects/{self.project.id}/', {}, format='json')
         request.user = None 
         perm = IsAuthorOrReadOnly()
         self.assertFalse(perm.has_object_permission(request, None, self.project))
         
    def test_permission_author(self):
        request = self.factory.put(f'/projects/{self.project.id}/', {}, format='json')
        request.user = self.author
        perm = IsAuthorOrReadOnly()
        self.assertTrue(perm.has_object_permission(request, None, self.project))

    def test_permission_non_author(self):
        request = self.factory.put(f'/projects/{self.project.id}/', {}, format='json')
        request.user = self.other
        perm = IsAuthorOrReadOnly()
        self.assertFalse(perm.has_object_permission(request, None, self.project))

    def test_update_project_non_author(self):
        request = self.factory.put(f'/projects/{self.project.id}/finsih', {}, format='json')
        request.user = self.other
        perm = IsAuthorOrReadOnly()
        self.assertFalse(perm.has_object_permission(request, None, self.project))

        project_status = self.project.active

        if perm.has_object_permission(request, None, self.project):
            self.project.finish_project()

        self.project.refresh_from_db()
        self.assertEqual(self.project.active, project_status)
