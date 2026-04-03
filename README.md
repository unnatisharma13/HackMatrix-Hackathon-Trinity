# 🚀 ResuMatch – Resume Analyzer

ResuMatch is a web-based application that helps users evaluate how well their resume matches a job description.

It analyzes resumes using Natural Language Processing (NLP) and provides:

- ✅ Match Score (in percentage)
- 🔍 Matching Keywords
- ❌ Missing Skills
- 📊 Improvement Insights

---

# 📌 Features

- Upload Resume in PDF format
- Enter job description
- Automatic keyword extraction using NLP
- Match percentage calculation
- Identification of missing skills
- Clean and interactive result UI
- Personalized improvement roadmap (UI)

---

# How It Works

1. User uploads a resume (PDF)
2. User enters a job description
3. Backend extracts text from PDF
4. NLP is applied using NLTK
5. Important keywords are extracted
6. Resume and job description keywords are compared
7. Match score is calculated
8. Results are displayed on frontend

---

#  Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- Python
- Flask

## Libraries Used
- NLTK (Natural Language Processing)
- PyPDF (PDF text extraction)
- Flask-CORS (for frontend-backend communication)

---

# 📂 Project Structure
    Backend
        ##app.py
            Flask server
            Handles API request /analyze
            Extracts text from PDF
            Runs NLP (keyword extraction)
            Calculates:
            match score
            matched keywords
            missing skills

    Frontend
        index.html
            Homepage
            Navigation
            Entry point
        analyze.html
            Upload resume (PDF)
            Enter job description
            Sends data to backend (API call)
        results.html
            Displays:
            match score
            matching keywords
            missing skills
            Uses backend response
