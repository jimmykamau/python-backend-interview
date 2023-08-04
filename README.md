# Amitruck

A service composed of APIs to help Amitruck and its partners achieve the goal of capturing trip details.

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation and Setup

1. Clone the repository:

   ```shell
   git clone https://github.com/jimmykamau/python-backend-interview.git
   cd python-backend-interview
   ```

2. Create a `.env` file with the contents of [.env.example](amitruck/.env.example), updating the values as required.

3. Build and start the Docker containers using Docker Compose:

   ```shell
   docker compose up --build
   ```

   Docker Compose will build the images and start the Django application and MySQL database containers.

4. Run migrations

    ```shell
    docker compose exec web python manage.py migrate
    ```

5. Access the app in your browser at `http://localhost:8000/`. 

## Interacting with the API
API documentation can be accessed at `http://localhost:8000/swagger/`.
To interact with the REST endpoints, first create a token by making a JSON `POST` request to `api-token-auth/` and pass your `username` and `password`. The endpoint will return a token that can be used in the `Authorization` header of requests. The header body should be in the format `api_token <token>`

## Running Tests

To run the unit tests for the app, use the following command:

```shell
docker compose exec web python manage.py test
```

## Admin Interface

The app includes an admin interface for viewing/managing app data. To access the admin interface:

1. Create a superuser account:

   ```shell
   docker compose exec web python manage.py createsuperuser
   ```

2. Access the admin interface in your browser at `http://localhost:8000/admin/`. Log in with your superuser credentials.

## Stopping the App

To stop the running Docker containers, use the following command:

```shell
docker compose down
```

This will stop and remove the containers, but will preserve the database data.