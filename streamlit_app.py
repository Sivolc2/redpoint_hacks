from pathlib import Path
import os
import replicate
import webbrowser

import streamlit as st
from streamlit.components.v1 import html

DB_PATH = (Path(__file__).parent / "Chinook.db").absolute()

# Replicate Variables
replicate_api_key = st.write(
    os.environ["REPLICATE_API_KEY"] == st.secrets["REPLICATE_API_KEY"],
)
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
<<<<<<< HEAD
        # yourfunction(user_input)
=======
        webbrowser.open(output_url)
>>>>>>> cb22540 (open output in new tab)
        # if not user_input:
        #     user_input = prefilled
        submit_clicked = st.form_submit_button("Build visualization")


# Define your javascript
my_js = """
alert("Hola mundo");
"""

# Wrapt the javascript as html code
my_html = f"<script>{my_js}</script>"

# Execute your app
st.title("Javascript example")
html(my_html)

