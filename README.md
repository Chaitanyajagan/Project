# Hi, I'm Chaitanya Jagan! 👋
## 🚀 About Me
Motivated and detail-oriented Computer Science undergraduate specializing in Artificial Intelligence and MachineLearning. Adept in Python programming, data structures, and algorithmic problem-solving. Experienced in applying AI/ML concepts to real-world projects. Actively seeking entry-level opportunities in AI Engineering,Machine Learning, and Python Development roles to contribute technical and analytical skills in a collaborative, fast-paced environment.

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](http://www.linkedin.com/in/chaitanyajagan)

# 🤖 Chatbot Based on RAG
A Retrieval-Augmented Generation (RAG) based chatbot that retrieves relevant context from documents and generates human-like responses using HuggingFace LLMs.

# 📖 About the Project
This chatbot integrates document retrieval and language generation to provide meaningful responses based on a custom knowledge base. Built using Python and HuggingFace Transformers, it serves as a lightweight and effective solution for document-driven Q&A.

## ✨ Features
- 📄 Loads and queries from CSV-based knowledge base
- 🧠 Uses HuggingFace LLMs for answer generation
- 🔍 Retrieves relevant context from local files
- 🛠️ Simple backend in Python
- 💬 Outputs responses to a text file `(output.txt)`


## 🛠 Tech Stack
- Backend: Python
- Frontend: Streamlit
- LLM Integration: HuggingFace Transformers
- Knowledge Source: ` knowledge_base.csv `

## 🗂️ Project Structure
```bash
Project/
│
├── Project.ipynb           # Jupyter Notebook version (for testing/debugging)
├── app.py                  # Main Python script to run the chatbot
├── knowledge_base.csv      # Source knowledge base (Q&A or documents)
├── output.txt              # File where chatbot responses are saved
```

## ▶️ Running Tests

```bash
  # Run the chatbot (example with Streamlit or CLI) on bash
  streamlit run app.py
```
