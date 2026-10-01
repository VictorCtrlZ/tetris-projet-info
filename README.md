Technologies utilisées
Backend
Python
Django
Django REST Framework
Frontend
HTML
CSS
JavaScript
Canvas HTML5


Installation
1. Cloner le projet
git clone <URL_DU_REPOSITORY>
cd tetris-projet-info
2. Créer l'environnement virtuel
python -m venv .venv
3. Activer l'environnement virtuel

Sous Windows :

.venv\Scripts\activate

Sous Linux/macOS :

source .venv/bin/activate
4. Installer les dépendances
pip install -r requirements.txt
5. Effectuer les migrations
python manage.py migrate
6. Lancer le serveur
python manage.py runserver

Le projet est ensuite accessible à l'adresse :

http://127.0.0.1:8000/