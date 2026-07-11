from pathlib import Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from Resumes.resume_extractor import (
    extract_resume_text,
    clean_resume_text
)

from Matching_engine.sentence_transformer import (
    analyze_resume
)


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
RESUME_FOLDER = BASE_DIR / "Resumes"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    Selected_Domain = request.form["domain"]
    resume_file = request.files["resume"]

    filename = secure_filename(resume_file.filename)
    resume_path = RESUME_FOLDER / filename

    resume_file.save(resume_path)

    resume = extract_resume_text(resume_path)

    resume_cleaned = clean_resume_text(resume)

    result = analyze_resume(
        resume_cleaned,
        Selected_Domain
    )

    if result is None:
        return "Domain was not found."

    (
        resume_score,
        skill_score,
        Overall_score,
        Matched_skills,
        UnMatched_skills
    ) = result

    return render_template(
        "index.html",
        resume_score=resume_score,
        skill_score=skill_score,
        overall_score=Overall_score,
        matched_skills=Matched_skills,
        missing_skills=UnMatched_skills
    )


if __name__ == "__main__":
    app.run(debug=True)