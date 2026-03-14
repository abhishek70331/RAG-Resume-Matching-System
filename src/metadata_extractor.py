import re

SKILLS_DB = [
    "python","java","sql","machine learning",
    "aws","docker","kubernetes","react",
    "flask","fastapi","pandas","tensorflow"
]

def extract_metadata(text):

    found_skills = []

    for skill in SKILLS_DB:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    exp_match = re.search(r'(\d+)\+?\s*years', text.lower())

    experience = exp_match.group(1) if exp_match else "0"

    return {
        "skills": found_skills,
        "experience_years": experience
    }