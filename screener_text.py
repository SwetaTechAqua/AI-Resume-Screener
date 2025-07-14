# screener_txt.py
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_resumes(resume_folder):
    resumes = []
    filenames = []
    for file in os.listdir(resume_folder):
        if file.endswith(".txt"):
            with open(os.path.join(resume_folder, file), 'r', encoding='utf-8') as f:
                resumes.append(f.read())
                filenames.append(file)
    return resumes, filenames

def compute_similarity(resumes, job_description):
    documents = resumes + [job_description]
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    return scores

def analyze_resumes(resume_folder, job_description):
    resumes, filenames = load_resumes(resume_folder)
    scores = compute_similarity(resumes, job_description)
    result = {filenames[i]: round(scores[i] * 100, 2) for i in range(len(filenames))}
    sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    return sorted_result

# Example use
if __name__ == "__main__":
    job_desc = """
    Looking for a Python developer with experience in machine learning, 
    pandas, numpy, and data analysis.
    """
    folder = "resumes"
    result = analyze_resumes(folder, job_desc)
    for file, score in result.items():
        print(f"{file}: {score}% match")
