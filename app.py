import streamlit as st
import pandas as pd
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import pipeline

st.set_page_config(page_title=" RAG Chatbot", layout="centered")

st.title(" RAG Chatbot with HuggingFace ")
st.markdown("Ask questions based on your uploaded dataset!")

# Sidebar to upload CSV
uploaded_file = st.sidebar.file_uploader("knowledge_base.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("CSV uploaded successfully!")

    # Prepare the documents
    documents = df.astype(str).apply(" ".join, axis=1).tolist()
    docs = [Document(page_content=doc) for doc in documents]

    # Split text
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = text_splitter.split_documents(docs)

    # HuggingFace Embeddings
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create Chroma vector store
    vectorstore = Chroma.from_documents(split_docs, embedding)

    # HuggingFace LLM (you can change to a bigger model if needed)
    hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", max_length=1024, do_sample=True, temperature=0.7)
    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    # RAG Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=False
    )

    # UI input
    user_query = st.text_input("Ask your question:")

    if user_query:
        with st.spinner("Thinking..."):
            result = qa_chain({"query": user_query})
            st.markdown("### 📘 Answer")
            st.write(result["result"])

else:
    st.warning("Please upload a CSV file to start.")
