FROM python:3.9-slim


WORKDIR /JantuLab

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","main:app", "--host=0.0.0.0","--reload"]

