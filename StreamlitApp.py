import streamlit as st
from QA_with_PDF.data_ingestion import load_data_from_directory
from QA_with_PDF.embedding import download_gemini_embedding_model
from QA_with_PDF.model_api import load_model    

def main():
    st.set_page_config("QA Application using Gemini API and LlamaIndex")

    doc = st.file_uploader("Upload your PDF file")

    st.header("information retrieval")

    user_query = st.text_input("Ask a question about the document")

    if st.button("Submit"):
        with st.spinner("Processing..."):
            documents = load_data_from_directory(doc)
            model = load_model()
            query_engine = download_gemini_embedding_model(model, documents)
            response = query_engine.query(user_query)
            st.write(response)

if __name__ == "__main__":
    main()
