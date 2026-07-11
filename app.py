from pathlib import Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from matching_engine.resume_extractor import (
    extract_resume_text,
    clean_resume_text
)

from matching_engine.sentence_transformer import analyze_resume


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
RESUME_FOLDER = BASE_DIR / "uploads"

# Create the uploads folder automatically if it does not exist
RESUME_FOLDER.mkdir(exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    selected_domain = request.form["domain"]
    resume_file = request.files["resume"]

    filename = secure_filename(resume_file.filename)
    resume_path = RESUME_FOLDER / filename

    resume_file.save(resume_path)

    resume = extract_resume_text(resume_path)
    resume_cleaned = clean_resume_text(resume)

    result = analyze_resume(
        resume_cleaned,
        selected_domain
    )

    if result is None:
        return "Domain was not found."

    (
        resume_score,
        skill_score,
        overall_score,
        matched_skills,
        unmatched_skills
    ) = result

    return render_template(
        "index.html",
        resume_score=resume_score,
        skill_score=skill_score,
        overall_score=overall_score,
        matched_skills=matched_skills,
        missing_skills=unmatched_skills
    )


if __name__ == "__main__":
    app.run(debug=True)