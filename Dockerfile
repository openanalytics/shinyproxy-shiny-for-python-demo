FROM python:3.10

LABEL maintainer "Tobias Verbeke <tobias.verbeke@openanalytics.eu>"

RUN pip3 install shiny matplotlib numpy

WORKDIR /app

EXPOSE 8080

COPY ./app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
