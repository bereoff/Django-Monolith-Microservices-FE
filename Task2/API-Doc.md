# API Documentation

## User Authentication App

### Health Check

- **Method:** GET
- **Endpoint:** http://0.0.0.0:8000/
- **Response:**
  ```json
  {
     "Health Check": "OK"
  }
  ```

### Create New User

- **Method:** POST
- **Endpoint:** http://0.0.0.0:8000/api/v1/auth/new/
- **Request:**
  ```json
  {
      "username": "foo_bar",
      "first_name": "Foo",
      "last_name": "Bar",
      "email": "test@email.com",
      "password": "1234testpass",
      "email": "test@email.com"
  }
  ```
- **Response:**
  - (200 OK)
    ```json
    {
       "user": "test@email.com",
       "Token": "618e1bb4a0560740229d89713e2cf03992d4070d"
    }
    ```
  - (400 BAD REQUEST)
    ```json
    {
       "username": [
           "A user with that username already exists."
       ],
       "email": [
           "user with this email address already exists."
       ]
    }
    ```

### User Login

- **Method:** POST
- **Endpoint:** http://0.0.0.0:8000/api/v1/auth/login/
- **Request:**
  ```json
  {
     "password": "1234testpass",
     "email": "test@email.co"
  }
  ```
- **Response:**
  - (404 NOT FOUND)
    ```json
    {
       "detail": "Not found."
    }
    ```
  - (200 OK)
    ```json
    {
       "Token:": "618e1bb4a0560740229d89713e2cf03992d4070d"
    }
    ```

### List All Users

- **Method:** GET
- **Endpoint:** http://0.0.0.0:8000/api/v1/auth/
- **Response:**
  - (200 OK)
    ```json
    {
       "count": 2,
       "next": null,
       "previous": null,
       "results": [
           {
               "id": 1,
               "username": "foo_bar",
               "first_name": "Foo",
               "last_name": "Bar",
               "password": "hashed_password_1",
               "email": "test@email.com"
           },
           {
               "id": 2,
               "username": "user_name",
               "first_name": "John",
               "last_name": "Wick",
               "password": "hashed_password_2",
               "email": "test2@email.com"
           }
       ]
    }
    ```

## Blog

### Health Check

- **Method:** GET
- **Endpoint:** http://0.0.0.0:8001/
- **Response:**
  ```json
  {
     "Health Check": "OK"
  }
  ```

### Create New Post

- **Method:** POST
- **Endpoint:** http://0.0.0.0:8001/api/v1/app/new/
- **Request:**
  ```json
  [
     {
         "title": "New Post 2",
         "content": "Second new post"
     }
  ]
  ```
- **Response:**
  - (201 CREATED)

### List Posts

- **Method:** GET
- **Endpoint:** http://0.0.0.0:8001/api/v1/app/?page_size=5&page_num=1
- **Response:**
  - (200 OK)
    ```json
    {
       "posts": [
           {
               "_id": "65d2cc9cfdec83d3dc01f5f8",
               "title": "New Post",
               "content": "First Post",
               "date_posted": "2024-02-19T03:35:56.270000Z"
           },
           {
               "_id": "65d2cceab28deaf0578dbf48",
               "title": "New Post 2",
               "content": "Second new post",
               "date_posted": "2024-02-19T03:37:14.190000Z"
           }
       ],
       "total_pages": 1,
       "total_items": 2
    }
    ```
