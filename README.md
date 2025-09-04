# Projet de Gestion de Projet - API REST

Une application web back-end développée en **Django** et **Django REST Framework** pour gérer des projets, leurs contributeurs, issues (tickets) et commentaires.

---

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Base de données](#base-de-données)
- [Routes principales](#routes-principales)

---

## Fonctionnalités

- Gestion des projets (création, lecture, mise à jour, suppression)
- Gestion des contributeurs par projet
- Création et suivi des issues (bugs, tâches, améliorations)
- Ajout et consultation des commentaires sur les issues
- API REST complète avec URLs imbriquées pour refléter les relations entre ressources

---

## Technologies utilisées

- Python 3.12
- Django 5
- Django REST Framework
- DRF Nested Routers
- SQLite (par défaut, peut être remplacé par PostgreSQL)
- Environnement virtuel `venv`

---

## Installation

1. Cloner le dépôt :

```bash
git clone <URL_DU_REPO>
cd api_rest
```
Créer un environnement virtuel et l'activer :
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Installer les dépendances :
```bash
pip install -r requirements.txt
```
Appliquer les migrations :
```bash
python manage.py migrate
```
Remplir la base de données avec des exemples :
```bash
python populate_db.py
```
Lancer le serveur de développement :
```bash
python manage.py runserver
```
L'API sera accessible sur : http://127.0.0.1:8000/api/

## Base de données

1. Les modèles principaux sont :

User : Utilisateur du système
Project : Projet contenant plusieurs contributeurs
Contributor : Relation entre User et Project avec un rôle (author ou contributor)
Issue : Ticket lié à un projet avec priorité, tag et statut
Comment : Commentaire lié à une issue, écrit par un contributeur

2. Le script populate_db.py crée :

* 3 utilisateurs (arnaud, marie, paul)
* 2 projets
* Des relations contributeur/projet
* 2 issues
* Des commentaires associés aux issues

## Routes principales

Projets

GET /api/project/           # Liste des projets
GET /api/project/<id>/      # Détails d'un projet

Contributeurs
GET /api/project/<project_pk>/contributors/      # Liste des contributeurs d’un projet

Issues
GET /api/project/<project_pk>/issue/            # Liste des issues d’un projet
GET /api/project/<project_pk>/issue/<issue_pk>/ # Détails d’une issue

Commentaires
GET /api/project/<project_pk>/issue/<issue_pk>/comments/        # Liste des commentaires d’une issue
POST /api/project/<project_pk>/issue/<issue_pk>/comments/ 