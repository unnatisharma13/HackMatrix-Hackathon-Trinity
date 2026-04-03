from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pypdf import PdfReader
import io

app = Flask(__name__)
CORS(app)

# Extra words to ignore
extra_words = {
    "looking", "skills", "skill", "candidate", "job", "role",
    "experience", "knowledge", "ability", "work", "working",
    "good", "strong", "required", "responsible", "responsibilities",
    "must", "should", "will", "using", "use", "based",
    "team", "teams", "project", "projects",
    "develop", "developing", "developed",
    "build", "building", "built",
    "create", "creating", "created",
    "need", "needed", "requirements",
    "etc", "like", "including", "include"
}

def extract_keywords(text):
    if not text:
        return set()

    text = text.lower()
    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    stop_words.update(extra_words)

    keywords = []
    for word in words:
        clean_word = word.strip().lower()
        if clean_word.isalnum() and clean_word not in stop_words and len(clean_word) > 2:
            keywords.append(clean_word)

    return set(keywords)

def extract_text_from_pdf(file):
    pdf_bytes = file.read()
    pdf_reader = PdfReader(io.BytesIO(pdf_bytes))

    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "

    return text.strip()

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_text = ""
    job_desc = ""

    # Option 1: JSON input
    if request.is_json:
        data = request.get_json()
        resume_text = data.get("resume", "")
        job_desc = data.get("job_desc", "")

    # Option 2: Form-data input (PDF upload)
    else:
        job_desc = request.form.get("job_desc", "")
        resume_text = request.form.get("resume", "")

        uploaded_file = request.files.get("resume_pdf")

        if uploaded_file and uploaded_file.filename.lower().endswith(".pdf"):
            resume_text = extract_text_from_pdf(uploaded_file)

    if not resume_text or not job_desc:
        return jsonify({
            "error": "Resume text/PDF and job description are required."
        }), 400

    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_desc)

    matched = resume_keywords.intersection(job_keywords)
    missing = job_keywords - resume_keywords

    if len(job_keywords) == 0:
        match_score = 0
    else:
        match_score = (len(matched) / len(job_keywords)) * 100

    return jsonify({
        "match_score": round(match_score, 2),
        "matched_keywords": list(matched),
        "missing_skills": list(missing),
        "resume_text_preview": resume_text[:300]
    })

if __name__ == '__main__':
    app.run(debug=True)