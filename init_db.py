import sqlite3
import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

skills = [
    "Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS",
    "Flask", "Django", "React", "Node.js", "Machine Learning"
]

conn = sqlite3.connect("skills.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name TEXT UNIQUE,
    embedding TEXT
)
""")

for skill in skills:
    emb = model.encode(skill).astype(float).tolist()

    cursor.execute("""
        INSERT OR REPLACE INTO skills (skill_name, embedding)
        VALUES (?, ?)
    """, (skill.lower(), json.dumps(emb)))

conn.commit()
conn.close()

print("DB ready")