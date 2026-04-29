# Job Matcher AI

An AI-powered CV skill matching system built using Python, Flask, and Sentence Transformers.

## Overview
This project analyzes a CV text and matches it against a predefined skills database using NLP embeddings (Sentence-BERT). It provides matched skills, missing skills, and an overall similarity score.

## Tech Stack
- Python
- Flask
- Sentence Transformers
- NumPy
- SQLite

## How It Works
1. CV text is converted into embeddings using SentenceTransformer
2. Skills are stored in a SQLite database with embeddings
3. Cosine similarity is used to compare CV and skills
4. The API returns matched skills and a compatibility score

## API Endpoint
POST /job_match

Request Body:
{
  "cv_text": "I know Python, Flask and machine learning"
}

Response Example:
{
  "matched_skills": ["python", "flask", "machine learning"],
  "missing_skills": ["java", "c++", "react"],
  "score": 45.0
}

## Run Locally
pip install -r requirements.txt
python init_db.py
python app.py

## Test Example
import requests

res = requests.post(
    "http://127.0.0.1:5000/job_match",
    json={"cv_text": "I know Python and Flask"}
)

print(res.json())

## Project Purpose
This project demonstrates how NLP and embeddings can be used in HR systems to automatically analyze CVs and extract relevant skills.

## Author
Inass Rabah
