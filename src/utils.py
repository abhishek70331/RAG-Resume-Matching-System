import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader


def load_resumes(folder_path):

    documents = []

    for file in os.listdir(folder_path):

        path = os.path.join(folder_path, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)

        elif file.endswith(".docx"):
            loader = Docx2txtLoader(path)

        else:
            continue

        docs = loader.load()

        for d in docs:
            d.metadata["source"] = path

        documents.extend(docs)

    return documents