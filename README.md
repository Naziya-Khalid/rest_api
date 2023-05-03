# django and rest api
This is a Django-based web application that allows users to register as either a client or an artist. Clients can view works created by artists and filter them by 
work type. They can also search for artists by name. Artists can create works and associate them with their profile.

Project Structure
The project consists of the following components:
client table: Contains information about clients, including their name and a foreign key reference to their user instance.
artist table: Contains information about artists, including their name and a many-to-many relationship with works.
work table: Contains information about works, including a link to the work and its type (e.g. YouTube, Instagram, Other).

API Endpoints
The following API endpoints are available:
/api/works/: Displays a list of works. Allows filtering by work type.
/api/artists/: Displays a list of artists. Allows searching by name.
/api/register/: Allows users to register with a username and password.

Signals
Whenever a new user is registered, a new client object is automatically created using signals.

Install the required dependencies:
pip install django django-framework

Important commands
django-admin startproject project_name
django-admin startapp app_name
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
