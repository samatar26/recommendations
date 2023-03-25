# recommendations

Playground which will hopefully turn into a fully-fledged recommendation machine

### Development

I'm of the opinion that the sooner you set up some linting, formatting, testing and continious integration, the easier it is to develop your application over time with a high degree of confidence things are working correctly.

In order to make sure the code is **always** of a high standard before merging it into main I'm using the following tools:
- [black](https://pypi.org/project/black/) - ensures consistent formatting throughout the code base
- [ruff](https://beta.ruff.rs/docs/) - ensures code is syntactically correct and of a good standard (no unused variables, imports at the top, etc.)
- [pre-commit](https://pre-commit.com/) - ensures that every commit has been checked by both ruff and black
- [circleci](https://circleci.com/) - continious integration/deployment pipeline ensuring my code is fully working by running format, linting and tests
- [pytest](https://docs.pytest.org/en/7.2.x/) - because tdd

The package manager I'll be using is pipenv, may possibly migrate to poetry due to its support for pyproject.toml

### Server
I'll be using [uvicorn](https://www.uvicorn.org/) as it's an extremely fast ASGI web server allowing me to handle a large number of connections simultaneously in an async manner. The web framework I'll be using is [FastApi](https://fastapi.tiangolo.com/) due to its async support, speed, ability to leverage type-hints, ease-of-use of the Pydantic data validation library and more!

### Database
[Postgresql](https://www.postgresql.org/) is the database I'll be using to store the data. I'll be using [alembic](https://alembic.sqlalchemy.org/en/latest/) to handle database migrations and [sqlalchemy](https://www.sqlalchemy.org/) as ORM. Alembic and sqlalchemy work **really** well together and allows me to auto-generate any database migrations just by running a simple command


### Deployment 
TBD

