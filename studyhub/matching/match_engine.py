from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_user_vector(user_profile):
    combined = " ".join(user_profile.subjects + user_profile.strengths)
    return model.encode(combined)

def match_user_to_groups(user_vector, group_list):
    group_vectors = [model.encode(g.subject + " " + g.description) for g in group_list]
    scores = cosine_similarity([user_vector], group_vectors)[0]
    return sorted(zip(group_list, scores), key=lambda x: x[1], reverse=True)
