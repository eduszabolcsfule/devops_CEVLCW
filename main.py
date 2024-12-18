import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

st.set_page_config(
    page_title="Óriás Pandák Napi Teendői",
    page_icon="🐼",
    layout="centered"
)

st.title("Óriás Pandák Napi Teendői 🐼")

uploaded_file = st.file_uploader("Tölts fel egy CSV fájlt az óriás pandák napi tevékenységeiről", type="csv")

if uploaded_file is not None:
    df = load_data(uploaded_file)

    st.subheader("CSV Tartalom")
    st.dataframe(df)

    fig = px.pie(df, 
                 names="Tevékenység", 
                 values="Órák száma", 
                 title="Óriás Pandák Napi Tevékenységei",
                 color_discrete_sequence=px.colors.qualitative.Set1)

    st.plotly_chart(fig)
else:
    st.info("Kérlek, tölts fel egy CSV fájlt az elemzéshez!")