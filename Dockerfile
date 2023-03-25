FROM python:3.10-bullseye

WORKDIR /app

COPY Pipfile* ./

RUN pip install --no-cache-dir pipenv
RUN pipenv install --deploy --ignore-pipfile

COPY recommendations_api ./recommendations_api

EXPOSE 8000

# https://github.com/pypa/pipenv/pull/2762 - best practice to favour virtual environemnts inside a Docker container
# No need for multi-stage builds (yet 😄)
CMD ["pipenv", "run", "uvicorn", "recommendations_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
