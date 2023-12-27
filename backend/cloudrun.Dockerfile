  
FROM python:3.8

RUN mkdir /app
WORKDIR /app

RUN apt update && \
    apt install -y postgresql-client

# Install Poetry
RUN pip install poetry
# RUN curl -sSL https://install.python-poetry.org | python3 -
RUN POETRY_HOME=/opt/poetry python
#     cd /usr/local/bin && \
#     ln -s /opt/poetry/bin/poetry && \
#     poetry config virtualenvs.create false
RUN poetry config virtualenvs.create false
COPY ./backend/pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root

COPY backend/ /app

ENV PORT 80
EXPOSE 80

CMD ["python", "app/main.py"]