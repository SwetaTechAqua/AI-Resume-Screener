# screener_pdf.py
import os
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def load_resumes(resume_folder):
    resumes = []
    filenames = []
    for file in os.listdir(resume_folder):
        if file.endswith(".pdf"):
            try:
                text = extract_text_from_pdf(os.path.join(resume_folder, file))
                resumes.append(text)
                filenames.append(file)
            except Exception as e:
                print(f"Error reading {file}: {e}")
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
Looking for a Python developer with 1–3 years of experience in building machine learning models, data analysis using pandas, numpy, and scikit-learn. Should have worked with real-world datasets and have experience in AI, ML, statistics, data wrangling, and model evaluation.
"""

    folder = "resumes"
    result = analyze_resumes(folder, job_desc)
    for file, score in result.items():
        print(f"{file}: {score}% match")
