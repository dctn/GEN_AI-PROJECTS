import streamlit as st
import os
import datasets
import pandas as pd

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
import os
load_dotenv()
st.title("TNPSC Retrevial System")

if 'embedding' not in st.session_state:
    st.session_state['embedding'] = None

user_question = st.text_input("Enter your question to be searched for")
no_of_questions = st.number_input("How many Similar questions do you want?",min_value=3,max_value=10,step=1)

if user_question and st.session_state.embedding == None:
    with st.spinner('Loading embedding'):
        # loading dataset from huggingface
        dataset = datasets.load_dataset('snegha24/Tamil_tnpscExam')

        # turning into dataframe
        df = pd.DataFrame(dataset['train'])

        # feature engineering for answer with options
        def extract_ans_from_list(series):
            try:
                ans_index = int(series['answer'])
                series['answer'] = series['options'][ans_index - 1]
            except:
                pass
            return series

        df = df.apply(extract_ans_from_list, axis=1)

        # turning questions into docs with metadata as answer, options, source link
        docs = []

        for i, row in df.iterrows():
            docs.append(
                Document(
                    page_content=row['question'],
                    metadata={'options': ", ".join(row['options']),
                              'answer':row['answer'],
                              'original_question_num': row['original_question_num'],
                              "link": row['source'],
                              'question_asked_paper':row['file_name']
                              },
                )
            )

        # loading embedding model
        embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        # convert question into vectors and store in Chroma DB
        vector_db = Chroma().from_documents(docs,embedding=embedding,collection_name='TNPSC',)

        # assign vector db to session state of streamlit
        st.session_state.embedding = vector_db

if user_question:
    similar_output_question = st.session_state.embedding.similarity_search_with_score(user_question,k=no_of_questions)

    st.markdown('## similar questions')
    for index in range(len(similar_output_question)):
        if similar_output_question[index][1] < 0.9:
            with st.expander(f'question NO: {index+1}', expanded=True):
                st.markdown(f'**question** and `similarity score: {round(similar_output_question[index][1],2)}`:')
                st.write(similar_output_question[index][0].page_content)

                st.markdown('**Options**:')
                st.write(similar_output_question[index][0].metadata['options'])

                st.markdown('**Answer**:')
                st.write(similar_output_question[index][0].metadata['answer'])

                st.markdown('**Question asked paper**:')
                st.write(similar_output_question[index][0].metadata['question_asked_paper'])

                st.markdown('**Question no paper**:')
                st.write(similar_output_question[index][0].metadata['original_question_num'])

                st.markdown('**Question paper Download link**:')
                st.write(similar_output_question[index][0].metadata['link'])
        else:
            st.markdown(f'**no similar questions matched **')




