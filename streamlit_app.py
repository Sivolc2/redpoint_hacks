from pathlib import Path

import streamlit as st

DB_PATH = (Path(__file__).parent / "Chinook.db").absolute()


# st.title("🦜 LangChain: Chat with search")
st.set_page_config(
    page_title="Theia", page_icon="*", layout="wide", initial_sidebar_state="collapsed"
)

"# 🦜🔗 Lumos: Revolutionize Your Business"
openai_api_key = st.write(
    os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"],
)

# Existing imports and setup
# tabs = st.tabs(["Product Search", "QA", "Map"])

with tabs[0]:
    with st.form(key="form"):
        user_input = st.text_input("What type of business do you run?")
        # if not user_input:
        #     user_input = prefilled
        submit_clicked = st.form_submit_button("Submit Inquiry")
