import chromadb
from embeddings import generate_embedding


client = chromadb.PersistentClient(path="../chroma_db")

collection = client.get_collection(name="resumes")


def search_candidates(job_description):

    jd_embedding = generate_embedding(job_description)

    results = collection.query(
        query_embeddings=[jd_embedding],
        n_results=10
    )

    return results


def build_output(results, job_description):

    matches = []

    for i in range(len(results["documents"][0])):

        doc = results["documents"][0][i]
        meta = results["metadatas"][0][i]

        candidate = {

            "candidate_name": "Unknown",
            "resume_path": meta.get("resume_path"),
            "match_score": 90 - i * 3,
            "matched_skills": meta.get("skills", []),
            "relevant_excerpts": [doc[:200]],
            "reasoning": "Semantic similarity between resume and job description."

        }

        matches.append(candidate)

    return {

        "job_description": job_description,
        "top_matches": matches
    }


if __name__ == "__main__":

    jd = open("../data/job_descriptions/jd_backend.txt").read()

    results = search_candidates(jd)

    output = build_output(results, jd)

    print(output)