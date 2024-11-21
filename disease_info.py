import wikipediaapi
import streamlit as st
import time

def fetch_disease_info(disease_name):
    if not disease_name.strip():
        st.warning("Please enter a disease name.")
        return
    
    st.spinner('Fetching information...')
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page(disease_name)
    if page.exists():
        st.subheader("Disease Information:")
        st.write(page.text[:1000])
    else:
        st.error("Disease information not found.")
