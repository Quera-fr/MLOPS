import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(
    page_title="Documentation API",
    page_icon="🧑",
    layout="wide",
)

st.title("Documentation API")

components.html(
"""<iframe
  width="1200"
  height="3000"
  src="https://api-brest-isen-8f7979410f0b.herokuapp.com/docs">
</iframe>
    """,
    height=2000,
)