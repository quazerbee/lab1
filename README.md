# Lab 1 – Client-Server Interaction

## Description
Simple FastAPI server that returns number of days before New Year.

## Run locally
python -m uvicorn main:app --reload

## Run with Docker
docker build -t lab1 .
docker run -p 8000:8000 lab1

## Run with Docker Compose
docker compose up --build

## Endpoint

GET /info

Example response:
{
  "days_before_new_year": 123
}