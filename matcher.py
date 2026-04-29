from sentence_transformers import SentenceTransformer, util
from db import get_skills_from_db
import numpy as np


# load model ONCE 
model = SentenceTransformer('all-MiniLM-L6-v2')


class JobMatcher:

    def __init__(self, cv_text):
        self.cv_text = cv_text.lower()
        self.cv_embedding = None

    def encode_cv(self):
        self.cv_embedding = model.encode(self.cv_text).astype(np.float32)

    def match(self):
        skills_db = get_skills_from_db()

        matched = []
        missing = []

        cv_emb = model.encode(self.cv_text, convert_to_numpy=True).astype(np.float32)

        for skill in skills_db:
            skill_text = skill["name"]

            skill_emb = model.encode(skill_text, convert_to_numpy=True).astype(np.float32)

            score = util.cos_sim(cv_emb, skill_emb).item()

            print(skill_text, score)  # مهم للتجربة

            if score > 0.3:   
                matched.append(skill_text)
            else:
                missing.append(skill_text)

        return {
        "matched_skills": matched,
        "missing_skills": missing,
        "score": self.calculate_score(matched, skills_db)
    }

    def calculate_score(self, matched, all_skills):
        if len(all_skills) == 0:
            return 0
        return (len(matched) / len(all_skills)) * 100