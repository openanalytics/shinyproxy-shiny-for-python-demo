FROM python:3.10

LABEL maintainer "Tobias Verbeke <tobias.verbeke@openanalytics.eu>"

RUN pip3 install shiny matplotlib numpy gunicorn

WORKDIR /app

EXPOSE 8080

COPY ./app.py .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080", "-k", "uvicorn.workers.UvicornWorker"]
