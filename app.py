import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains.retrieval import create_retrieval_chain

from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
os.environ['GOOGLE_API_KEY']=os.getenv("GOOGLE_API_KEY")

st.title("NeuroMate")

llm=ChatGroq(groq_api_key=groq_api_key,model="gemma2-9b-it")


prompt=ChatPromptTemplate.from_template(

    """
Answer the Questions based on the Context only.
Maintain a helpful tone, like a Doctor. 
<context>
{context}
<context>

Question:{input}
"""
)


def vector_embeddings():

    if "vectors" not in st.session_state:
        st.session_state.embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader=PyPDFDirectoryLoader("./Data") #data ingestion
        st.session_state.docs=st.session_state.loader.load() #docs loading
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)


prompt1=st.text_input("How can I help you?")

if st.button("Creating Vector Store"):
    vector_embeddings()
    st.write("Your DB is ready")

import time

if prompt1:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)


    start=time.process_time()

    response=retrieval_chain.invoke({'input':prompt1})
    st.write(response['answer'])


    with st.expander("Text Book Similarity Search"):

        for i ,doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x-x-x-")
