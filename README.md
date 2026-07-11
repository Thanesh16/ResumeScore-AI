# 📄 ResumeScore AI

### AI-Powered Resume Screening System using Flask, NLP & Sentence Transformers

---

## 📌 About the Project

ResumeScore AI is an intelligent resume-screening application that compares resumes with domain-specific job descriptions using Natural Language Processing and Sentence Transformers.

The application extracts text from PDF resumes, cleans the content, generates semantic embeddings, and calculates cosine similarity to produce an AI-based resume score.

---

## 🚀 Features

- Upload resumes in PDF format
- Automatic resume-text extraction
- Resume cleaning and preprocessing
- Domain-specific job matching
- Semantic comparison using Sentence Transformers
- Cosine-similarity-based resume scoring
- Skill matching and missing-skill identification
- Flask-based web interface

---

## 🎥 Demo

![ResumeScore AI Demo](screenshots/demo.gif)

---

## 📸 Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Resume Upload

![Resume Upload](screenshots/upload.png)

### Domain Selection

![Domain Selection](screenshots/domain.png)

### Analysis Result

![Analysis Result](screenshots/result.png)

### Resume Score

![Resume Score](screenshots/score.png)

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| NLP Model | Sentence Transformers |
| Similarity Method | Cosine Similarity |
| Data Processing | Pandas |
| PDF Extraction | pdfplumber |
| Frontend | HTML, CSS |

---

## 🔄 Workflow

```text
Resume PDF
    ↓
Text Extraction
    ↓
Text Cleaning and Preprocessing
    ↓
Domain Requirement Selection
    ↓
Sentence Transformer Embeddings
    ↓
Cosine Similarity Calculation
    ↓
Skill Matching
    ↓
Resume Score and Analysis
```

---

## 📂 Project Structure

```text
ResumeScore-AI/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── matching_engine/
│   ├── Requirement.csv
│   ├── resume_extractor.py
│   └── sentence_transformer.py
│
├── requirements/
│   ├── Requirement.csv
│   └── requirements.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── uploads/
│
└── screenshots/
    ├── home.png
    ├── upload.png
    ├── domain.png
    ├── result.png
    ├── score.png
    └── demo.gif
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Thanesh16/ResumeScore-AI.git
```

### 2. Open the project folder

```bash
cd ResumeScore-AI
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

### 5. Open the application in your browser

```text
http://127.0.0.1:5000
```

---

## 🔮 Future Enhancements

- ATS compatibility analysis
- Improved required-skills matching
- Resume improvement suggestions
- Multiple-resume ranking
- Detailed skill-gap analysis
- LLM-based resume feedback
- Cloud deployment

---

## 👨‍💻 Author

**Thanesh S**

Aspiring Data Scientist

[GitHub](https://github.com/Thanesh16) • [LinkedIn](https://linkedin.com/in/thanesh006)

---

⭐ If you found this project useful, consider starring the repository.
