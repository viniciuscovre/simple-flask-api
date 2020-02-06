# Simple Flask API

Simple API using Flask, SQLAlchemy (PostgreSQL database) and Marshmallow.

## Local Development

### Project Setup

Having [Pipenv](https://github.com/pypa/pipenv) installed on your machine, run the command for configuring your virtual environment:

```bash
  pipenv shell
```

After that, install the dependencies:

```bash
  make install
```

### Database Setup

Start by creating your PostgreSQL database and place the settings in the `config.py` file.

After that, configure the database by running:

```bash
  make db
```

### Start the local server

Start your local server with:

```bash
  make serve
```

You can also check linter by running:

```bash
  make lint
```

## API Examples (v1)

### GET /health

Check the health status of the server:

```bash
  curl --location --request GET 'http://127.0.0.1:5000/v1/health'
```

### POST /users

Create a new user:

```bash
  curl --location --request POST 'http://127.0.0.1:5000/v1/users' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "name": "Vinicius Covre",
    "dateOfBirth": "06/02/1995",
    "job": "Software Engineer"
  }'
```

### GET /users

Retrieve all users from the database:

```bash
  curl --location --request GET 'http://127.0.0.1:5000/v1/users'
```

### GET /users/:id

Get user by id:

```bash
  curl --location --request GET 'http://127.0.0.1:5000/v1/users/1'
```
