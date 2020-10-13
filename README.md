# ecommerce

## Features

- **FastAPI** with Python 3.8
- Postgres
- SqlAlchemy with Alembic for migrations
- Pytest for backend tests
- Docker compose for easier development

## Development

The only dependencies for this project should be docker and docker-compose.

### Quick Start

Starting the project with hot-reloading enabled
(the first time it will take a while):

```bash
docker-compose up -d
```

To run the alembic migrations (for the users table):

```bash
docker-compose run --rm backend alembic upgrade head
```

And navigate to http://localhost:8000

Auto-generated docs will be at
http://localhost:8000/api/docs

### Rebuilding containers:

```
docker-compose build
```

### Restarting containers:

```
docker-compose restart
```

### Bringing containers down:

```
docker-compose down
```

## Migrations

Migrations are run using alembic. To run all migrations:

```
docker-compose run --rm backend alembic upgrade head
```

To create a new migration:

```
alembic revision -m "create users table"
```

And fill in `upgrade` and `downgrade` methods. For more information see
[Alembic's official documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script).

## Testing

There is a helper script for tests:

```
bash ./scripts/test.sh
```


## Logging

```
docker-compose logs
```

Or for a specific service:

```
docker-compose logs -f name_of_service # frontend|backend|db
```

## Project Layout

```
ecommerce
└── app
    ├── alembic
    │   └── versions # where migrations are located
    ├── api
    │   └── admin
    │   │   └── endpoints
    │   └── auth
    │   │   └── endpoints
    │   └── shop
    │       └── endpoints
    ├── core    # config
    ├── db      # db models
    ├── schemas # schemas
    ├── tests   # pytest
    └── main.py # entrypoint to backend

```
