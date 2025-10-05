import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_rest.settings")
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
from gestion_projet.models import Project, Contributor, Issue, Comment


def run():
    # --- Nettoyage (facultatif si tu veux repartir à zéro) ---
    Comment.objects.all().delete()
    Issue.objects.all().delete()
    Contributor.objects.all().delete()
    Project.objects.all().delete()
    User.objects.all().delete()

    # --- Création d'utilisateurs ---
    u1 = User.objects.create_user(username="arnaud", password="test123")
    u2 = User.objects.create_user(username="marie", password="test123")
    u3 = User.objects.create_user(username="paul", password="test123")

    # --- Création de projets ---
    p1 = Project.objects.create(name="Projet Django", author=u1, description="API de gestion de projet")
    p2 = Project.objects.create(name="Application Mobile", author=u3, description="Développement d'une app mobile React Native")

    # --- Associer contributeurs ---
    c1 = Contributor.objects.create(user=u1, project=p1, role="author")
    c2 = Contributor.objects.create(user=u2, project=p1, role="contributor")
    c3 = Contributor.objects.create(user=u3, project=p2, role="author")

    # --- Création d'issues ---
    i1 = Issue.objects.create(
        title="Corriger bug d'affichage",
        description="La page d’accueil plante quand on clique sur un bouton",
        project=p1,
        author=u1,
        assignee=u2,
        tag="bug",
        priority="high",
        status="to_do"
    )

    i2 = Issue.objects.create(
        title="Ajouter un écran profil",
        description="Créer un écran pour afficher les infos utilisateur",
        project=p2,
        author=u3,
        assignee=u1,
        tag="task",
        priority="medium",
        status="in_progress"
    )

    # --- Ajouter des commentaires ---
    Comment.objects.create(text="Je regarde ça dès demain.", issue=i1, author=c2)
    Comment.objects.create(text="Bonne idée, je commence la maquette.", issue=i2, author=c1)

    print("✅ Base de données remplie avec succès !")


def create_new_project():
    u1 = User.objects.filter(user_id='5')
    u2 = User.objects.filer(user_id="2")


    p1 = Project.objects.create(name="Projet API", author=u1, description="API de FI")

    c1 = Contributor.objects.create(user=u1, project=p1, role="author")
    c2 = Contributor.objects.create(user=u2, project=p1, role="contributor")
   
    # --- Création d'issues ---
    i1 = Issue.objects.create(
        title="Corriger bug d'affichage",
        description="La page d’accueil plante quand on clique sur un bouton",
        project=p1,
        author=u1,
        assignee=u2,
        tag="bug",
        priority="high",
        status="to_do"
    )

    Comment.objects.create(text="Je regarde ça dès demain.", issue=i1, author=c2)
    Comment.objects.create(text="Parfait, merci", issue=i1, author=c1)

if __name__ == "__main__":
    run()
