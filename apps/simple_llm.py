import streamlit as st
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()
groq_key = os.getenv('GROQ_KEY')

st.title('URL LL Model')

if "retriever" not in st.session_state:
    st.session_state.retriever = None

llm = ChatGroq(model='openai/gpt-oss-20b',api_key=groq_key)
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)

prompt = ChatPromptTemplate.from_template(
    """
    you are used to answer for given question with given context:
    <context>
    {context}
    </context>
    
    question:
    {input}
    """
)


user_input_url = st.text_input("Enter your website url",)

if user_input_url and st.session_state.retriever is None:
    with st.spinner("Scraping  data from url"):

        web_loader = WebBaseLoader(user_input_url)
        splitted_docs = text_splitter.split_documents(web_loader.load())
        vector_db = Chroma.from_documents(splitted_docs,embedding,collection_name='simple_url_llm',)
        st.session_state.retriever = vector_db.as_retriever()

        st.success("site is scraped successfully")

if st.session_state.retriever:
    user_question = st.text_input("Enter your question", )

    docs_chain = create_stuff_documents_chain(llm, prompt)
    retriever_chain = create_retrieval_chain(st.session_state.retriever, docs_chain)
    if user_question:
        response = retriever_chain.invoke({"input": user_question})

        st.write(response['answer'])
