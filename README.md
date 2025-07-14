# AI Resume Screener 🔍📄

This project is a mini AI-based tool that screens resumes against a job description and scores them based on relevance using TF-IDF and cosine similarity.

## 💡 Features
- Accepts `.txt` and `.pdf` resume formats
- Calculates % match score
- Uses TF-IDF vectorization and cosine similarity
- Real-world HR screening concept

<pre> ## 📁 Folder Structure ``` AI-Resume-Screener/ ├── resumes/ # Folder of resumes (.txt or .pdf) ├── screener_txt.py # Basic version using .txt ├── screener_pdf.py # PDF version using PyMuPDF ├── requirements.txt └── README.md ``` </pre>

## 🔧 How to Run

### 1. Install Dependencies
pip install -r requirements.txt

### 2. Run PDF Resume Screener
python screener_pdf.py

<pre> ## ✅ Sample Output ``` resume_python_ml.pdf: 58.3% match resume_ai_data.pdf: 51.69% match resume3.pdf: 18.18% match resume2.pdf: 16.36% match resume1.pdf: 6.22% match resume5.pdf: 2.53% match resume4.pdf: 2.51% match ``` </pre>

⚠️ Note: TF-IDF matches exact words. If resumes use synonyms or different phrasing, similarity scores will be lower. For better matching, we can use BERT, sentence embeddings, or keyword expansion in future versions.


## ✨ Future Enhancements
- Support for `.docx` files
- GUI using Streamlit
- PDF report generation

---

Made with 💙