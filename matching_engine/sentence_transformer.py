import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer, util


CURRENT_FOLDER = Path(__file__).resolve().parent

requirements = pd.read_csv(
    CURRENT_FOLDER / "Requirement.csv"
)


# ### Particularly slicing the domain description .

# In[95]:


def analyze_resume(resume_cleaned, Selected_Domain):

    selected_row = requirements[
        requirements["Domain"] == Selected_Domain
    ]

    if selected_row.empty:
        return None

    job_description = selected_row["Description"].iloc[0]

    # Your existing resume-score code
    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    resume_embedding = model.encode(
        resume_cleaned,
        convert_to_tensor=True
    )

    job_embedding = model.encode(
        job_description,
        convert_to_tensor=True
    )

    similarity_score = util.cos_sim(
        resume_embedding,
        job_embedding
    ).item()

    resume_score = round(
        similarity_score * 100,
        2
    )

    # Your existing skill-score code
    job_skills = selected_row[
        "Required_skills"
    ].iloc[0]

    job_req_skills = [
        skill.strip()
        for skill in job_skills.split(",")
    ]

    resume_lower = resume_cleaned.lower()

    Matched_skills = []
    UnMatched_skills = []

    for skill in job_req_skills:

        if skill.lower() in resume_lower:
            Matched_skills.append(skill)

        else:
            UnMatched_skills.append(skill)

    skill_score = round(
        len(Matched_skills)
        / len(job_req_skills)
        * 100,
        2
    )

    Overall_score = round(
        (0.8 * resume_score)
        + (0.2 * skill_score),
        2
    )

    return (
        resume_score,
        skill_score,
        Overall_score,
        Matched_skills,
        UnMatched_skills
    )