FROM python:3.7
RUN pip install pipenv
COPY . /app
WORKDIR /app

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
ENV SECRET_KEY=$SECRET_KEY
ENV POSTGRES_DB=$POSTGRES_DB
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
ENV POSTGRES_HOST=$POSTGRES_HOST
ENV POSTGRES_PORT=$POSTGRES_PORT
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT "/app/entrypoint.sh"
