FROM python:3.7
RUN pip install pipenv
COPY . /app
WORKDIR /app

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
ENV SECRET_KEY=$SECRET_KEY
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT "/app/entrypoint.sh"
