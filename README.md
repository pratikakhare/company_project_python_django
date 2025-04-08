
NexaNova is a web-based trainer-subject management application built using Django. It allows administrators to add, view, and manage trainers and subjects, with clean UI and API endpoints for integration.

#Features
Add, view, delete trainers and subjects
Assign subject(s) to trainers
Pagination and search on listing pages
RESTful APIs for backend integration
Clean Bootstrap-styled UI

#Tech Stack
Backend: Django, Django REST Framework
Frontend: HTML, CSS, Bootstrap
Database: SQLite (default), supports PostgreSQL/MySQL

#Folder Structure
├── trainer/              # Django app for core logic
│   ├── templates/trainer # HTML templates
│   ├── static/           # CSS/JS/Bootstrap
│   └── views.py
├── NexaNova/             # Django project settings
│   └── settings.py
├── db.sqlite3
├── manage.py


 #Setup Instructions
# Clone the repository
$ git clone https://github.com/your-username/nexanova.git
# Navigate to project
$ cd nexanova

# Create virtual environment
$ python -m venv venv && source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Run migrations
$ python manage.py migrate

# Start server
$ python manage.py runserver

#API Endpoints
Trainer APIs
GET /trainer/ → List trainers
POST /trainer/ → Create trainer
GET /trainer/<emp_id>/ → Get trainer details
DELETE /trainer/<emp_id>/ → Delete trainer
GET /trainer/<subject>/topic/ → Trainers by subject

#Subject APIs
GET /subject/ → List subjects
POST /subject/ → Create subject
GET /subject/<id>/ → Subject with trainers
DELETE /subject/<pk>/delete/ → Delete subject

#Author
Pratik AkhareWeb Developer | MCA Student
pratikakhare95@gmail.com

#Fully Completed & Tested – Ready for Demo / Submission
