import streamlit as st
import pandas as pd
import json
import requests

### Config
st.set_page_config(
    page_title="Streamlit",
    page_icon="🧑",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.image('img.jpg')

### Title et markdown : st.title et st.markdown
st.title("My Credit - ISEN")

# Cach data @st.cache_data
@st.cache_data
def load_data():
    return pd.read_csv("utiles/train.csv", sep=';')

df = load_data()
url = 'https://api-brest-isen-8f7979410f0b.herokuapp.com/predict'

### Checkbox st.checkbox
if st.checkbox("Show Dataframe"): st.write(df)

# Read the file with json
with open('utiles/all_dict.json') as json_file: data = json.load(json_file)

st.sidebar.write(df.columns)

# Lire le fichier json contenant les données de décogage
st.sidebar.write(data.keys())

# Formulaire
with st.form(key='my_form'):

    st.write("## Enter your informations")

    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", min_value=18, max_value=100, value=50, step=1)                       # Age
        job = data['job'][st.selectbox("Job", options=data['job'])]                                 # Job
        marital = data['marital'][st.selectbox("Marital", options=data['marital'])]                 # Marital
        education = data['education'][st.selectbox("Education", options=data['education'])]         # Education
        default = data['default'][st.selectbox("Default", options=data['default'])]                 # Default
        housing = data['housing'][st.selectbox("Housing", options=data['housing'])]                 # Housing

    with col2:
        loan = data['loan'][st.selectbox("Loan", options=data['loan'])]                             # Loan
        balance = st.slider("Balance", min_value=-1000, max_value=10000, value=5000, step=1)        # Balance
        campaign = st.slider("Campaign", min_value=0, max_value=10, value=10, step=1)               # Campaign
        pdays = st.slider("Pdays", min_value=0, max_value=100, value=50, step=1)                    # Pdays
        previous = st.slider("Previous", min_value=0, max_value=10, value=10, step=1)               # Previous
        poutcome = data['poutcome'][st.selectbox("Poutcome", options=data['poutcome'])]             # Poutcome


    if st.form_submit_button(label='Submit Form'):
        form_data = {
            "age": age, "job":  job, "marital": marital, "education": education,"default": default,
            "balance": balance, "housing": housing, "loan": loan, "campaign": campaign, "pdays": pdays,
            "previous": previous, "poutcome": poutcome
                    }
        st.write("# Your data:",
                 form_data)
        r = requests.post(url, json=form_data)
        st.write(r.json())