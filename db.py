import sqlite3
import json
import numpy as np

def get_skills_from_db():
    conn = sqlite3.connect("skills.db")
    cursor = conn.cursor()

    cursor.execute("SELECT skill_name, embedding FROM skills")
    rows = cursor.fetchall()

    conn.close()

    skills = []

    for name, emb in rows:
        skills.append({
            "name": name,
            "embedding": np.array(json.loads(emb), dtype=np.float32)
        })

    return skills