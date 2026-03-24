import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PW Skills Clone", layout="wide")

# This reads your existing index.html and displays it in Streamlit
with open("index.html", "r") as f:
    html_code = f.read()

components.html(html_code, height=1000, scrolling=True)
