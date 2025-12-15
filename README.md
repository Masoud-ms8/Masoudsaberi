README.md

````markdown
# Tourism Django Project

## Project Overview
This project is a **tourism web application** built with **Django** and **Django REST Framework (DRF)**.  
It provides information about various tourist destinations in Iran and allows managing users, destinations, and travel plans.

The project exposes a **RESTful API** and uses the **DRF Browsable API** for testing and visualizing data.

---

## Applications (Apps)

### 1. accounts
- **Purpose:** Manage users of the project.
- **Main operations:** Register users, list users, and manage user information.
- **Models:** User (Django default)
- **API Endpoints:**
  - `GET /api/users/` → List all users
  - `POST /api/users/` → Create a new user
  - `GET /api/users/<id>/` → Retrieve a specific user
  - `PUT/PATCH/DELETE /api/users/<id>/` → Update or delete a user

### 2. destinations
- **Purpose:** Manage tourist destinations.
- **Main operations:** Create, read, update, delete destinations.
- **Models:** Destination (fields: name, city, description, created_at)
- **API Endpoints:**
  - `GET /api/destinations/` → List all destinations
  - `POST /api/destinations/` → Create a new destination
  - `GET /api/destinations/<id>/` → Retrieve a specific destination
  - `PUT/PATCH/DELETE /api/destinations/<id>/` → Update or delete a destination

### 3. plans
- **Purpose:** Manage travel plans.
- **Main operations:** Create travel plans, retrieve plan details, and manage plans.
- **Models:** Plan (fields: title, description, related destinations, created_at)
- **API Endpoints:**
  - `GET /api/plans/` → List all plans
  - `POST /api/plans/` → Create a new plan
  - `GET /api/plans/<id>/` → Retrieve a specific plan
  - `PUT/PATCH/DELETE /api/plans/<id>/` → Update or delete a plan

---

## Installation & Running

1. Clone the repository:
```bash
git clone <YOUR_REPOSITORY_URL>
cd <PROJECT_FOLDER>
````

2. Create and activate a virtual environment:

```bash
py -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Access the API in your browser:

* Users: `http://127.0.0.1:8000/api/users/`
* Destinations: `http://127.0.0.1:8000/api/destinations/`
* Plans: `http://127.0.0.1:8000/api/plans/`
* Browsable DRF interface is available for all endpoints.

---

## Important Notes

* The `venv/` folder is ignored (`.gitignore` included)
* Default database: SQLite (`db.sqlite3` is also ignored)
* All API endpoints support **GET, POST, PUT, PATCH, DELETE** methods

---

## Future Enhancements

* Add advanced authentication (JWT or Token-based)
* Include images for destinations
* Build a frontend with React or Vue connected to this API
* Implement search and filter for destinations and travel plans
---
