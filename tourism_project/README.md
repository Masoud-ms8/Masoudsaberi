# 🧭 Tourism Django Project

## 📌 Project Overview

This project is a **tourism backend application** built with **Django**.  
The main goal of the project was to practice **backend architecture, data modeling, API design, and testing**.

The project was initially designed using **Django REST Framework (DRF)** and later **refactored and extended to use GraphQL** with **Graphene-Django** to support more flexible data querying.

The application manages:
- Users
- Tourist destinations
- Travel plans

---

## 🧠 Project Evolution (Important)

This project was developed in **two main phases**:

### Phase 1 – REST API (DRF)
- RESTful endpoints were implemented for all resources
- CRUD operations were supported
- DRF Browsable API was used for manual testing

### Phase 2 – GraphQL Migration (Final State)
- REST APIs were replaced with **GraphQL**
- Queries and Mutations were implemented
- Centralized GraphQL schema was introduced
- Automated tests were written for GraphQL APIs
- Code coverage was measured and validated

➡️ **Current and final version of the project uses GraphQL**.

---

## 🏗️ Technologies Used

- Python 3
- Django
- Graphene-Django (GraphQL)
- Django REST Framework (initial phase)
- SQLite (development database)
- Django Test Framework
- Coverage.py

---

## 📁 Project Structure

```

tourism_project/
├── accounts/        # User management
├── destinations/   # Tourist destinations
├── plans/           # Travel plans
├── config/          # Global settings & GraphQL schema
└── manage.py

````

---

## 👤 Accounts App

### Purpose
Manage users of the system.

### Model
- Django default `User` model

### GraphQL
- Query:
  - `allUsers`
- Mutation:
  - `createUser`

### Example Query
```graphql
query {
  allUsers {
    id
    username
    email
  }
}
````

---

## 🏨 Destinations App

### Purpose

Manage tourist destinations.

### Model

Destination fields:

* name
* city
* description
* price

### GraphQL

* Query:

  * `allDestinations`
* Mutation:

  * `createDestination`

### Example Mutation

```graphql
mutation {
  createDestination(
    name: "Persepolis"
    city: "Shiraz"
    description: "Historical site"
    price: 0
  ) {
    destination {
      id
      name
      city
      price
    }
  }
}
```

---

## 🗺️ Plans App

### Purpose

Manage travel plans and their relationships.

### Model

Each plan:

* belongs to a user
* can include multiple destinations (Many-to-Many)
* has title and description

### GraphQL

* Query:

  * `allPlans`
* Mutation:

  * `createPlan`

### Example Query

```graphql
query {
  allPlans {
    title
    user {
      username
    }
    destinations {
      name
      city
    }
  }
}
```

---

## 🔗 Relationships

* A **User** can have multiple **Plans**
* A **Plan** can include multiple **Destinations**
* Relationships are fully tested through GraphQL queries

---

## 🧪 Testing

GraphQL tests are written for each app:

* accounts
* destinations
* plans

### What is tested?

* GraphQL endpoint availability
* Query correctness
* Returned data structure
* Absence of execution errors

### Run tests

```bash
python manage.py test
```

---

## 📊 Test Coverage

Coverage is measured using **coverage.py**.

```bash
coverage run manage.py test
coverage report
```

* Overall test coverage is **above 80%**
* Meets the project requirements

---

## 🧹 Database Cleanup During Development

During development, multiple test records were created manually.
Before final testing:

* Database was cleaned
* Data was recreated in a controlled and related manner
* All relations were re-tested via GraphQL

---

## ✅ Final Project Status

* ✔️ Proper data models
* ✔️ GraphQL Queries & Mutations implemented
* ✔️ Clean schema structure
* ✔️ Automated tests written
* ✔️ Coverage above required threshold

---

## 📝 Notes

This project focuses on **learning backend concepts**, not production deployment.
The emphasis is on:

* correctness
* structure
* relationships
* testing

---