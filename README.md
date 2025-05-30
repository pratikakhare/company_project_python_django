# NexaNova

**NexaNova** is a web-based trainer-subject management application built using Django. It allows administrators to add, view, and manage trainers and subjects, with a clean UI and API endpoints for integration.

## Features
- Add, view, delete trainers and subjects
- Assign subject(s) to trainers
- Pagination and search on listing pages
- RESTful APIs for backend integration
- Clean Bootstrap-styled UI

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default), supports PostgreSQL/MySQL

# Folder structure
![Screenshot 2025-04-09 004123](https://github.com/user-attachments/assets/57bccd74-f4fd-4dda-b7e4-42f15e4a7c4c)

## Setup Instructions

1. **Clone the repository**
    ```sh
    git clone https://github.com/your-username/nexanova.git
    ```

2. **Navigate to project**
    ```sh
    cd nexanova
    ```

3. **Create virtual environment**
    ```sh
    python -m venv venv && source venv/bin/activate
    ```

4. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

5. **Run migrations**
    ```sh
    python manage.py migrate
    ```

6. **Start server**
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### Trainer APIs
- **GET** `/trainer/` → List trainers
- **POST** `/trainer/` → Create trainer
- **GET** `/trainer/<emp_id>/` → Get trainer details
- **DELETE** `/trainer/<emp_id>/` → Delete trainer
- **GET** `/trainer/<subject>/topic/` → Trainers by subject

### Subject APIs
- **GET** `/subject/` → List subjects
- **POST** `/subject/` → Create subject
- **GET** `/subject/<id>/` → Subject with trainers
- **DELETE** `/subject/<pk>/delete/` → Delete subject

## Author
**Pratik Akhare**  
Web Developer | MCA Student  
[pratikakhare95@gmail.com](mailto:pratikakhare95@gmail.com)

---

**Fully Completed & Tested** – Ready for Demo / Submission
