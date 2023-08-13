from pathlib import Path
import os
import replicate
import webbrowser

import streamlit as st

DB_PATH = (Path(__file__).parent / "Chinook.db").absolute()

# Replicate Variables
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get(
    "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")


# st.title("🦜 LangChain: Chat with search")
st.set_page_config(
    page_title="Theia", page_icon="*", layout="wide", initial_sidebar_state="collapsed"
)

"# 🦜🔗 Theia: Connect your ideas"
openai_api_key = st.write(
    os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"],
)

# Existing imports and setup
tabs = st.tabs(["Visualization"])

with tabs[0]:
    with st.form(key="form"):
        user_input = st.text_input("Add an item to your visualizer")
        output_url = version.predict(
            prompt = user_input)[0]
        # yourfunction(user_input)
        # if not user_input:
        #     user_input = prefilled
        submit_clicked = st.form_submit_button("Build visualization")
# jupyter nbconvert --to script *.ipynb
