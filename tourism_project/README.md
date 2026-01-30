---


- Python 3
- Django
- Graphene-Django (GraphQL)
- Django Test Framework
- Coverage.py

---


```

tourism_project/
└── manage.py

````

---



### GraphQL
- Query:
  - `allUsers`
- Mutation:
  - `createUser`

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




* name
* city
* description
* price

### GraphQL

* Query:

  * `allDestinations`
* Mutation:

  * `createDestination`


```graphql
mutation {
  createDestination(
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





### GraphQL

* Query:

  * `allPlans`
* Mutation:

  * `createPlan`


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







```bash
python manage.py test
```


```bash
coverage run manage.py test
coverage report
```


---




---



---

