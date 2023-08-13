from pathlib import Path
import os

import streamlit as st
from streamlit.components.v1 import html

DB_PATH = (Path(__file__).parent / "Chinook.db").absolute()

def render_mermaid_with_images(graph_definition):
    st.write(
        f"""
        <script src="https://unpkg.com/mermaid@8.0.0-rc.8/dist/mermaid.min.js"></script>
        <script src="./mermaid_with_images.js"></script>
        <div id="mermaid-chart"></div>
        <script>
            var graphDefinition = `{graph_definition}`;
            renderMermaid("mermaid-chart", graphDefinition);
        </script>
        """,
        unsafe_allow_html=True,
    )

# st.title("🦜 LangChain: Chat with search")
st.set_page_config(
    page_title="Theia", page_icon="*", layout="wide", initial_sidebar_state="collapsed"
)

"# 🦜🔗 Theia: Connect your ideas"
openai_api_key = st.write(
    os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"],
)

# Existing imports and setup
tabs = st.tabs(["Input", "Visualization"])

with tabs[0]:
    with st.form(key="form"):
        user_input = st.text_input("Add an item to your visualizer")
        # yourfunction(user_input)
        # if not user_input:
        #     user_input = prefilled
        submit_clicked = st.form_submit_button("Build visualization")

with tabs[1]:
    graph_definition = f"""graph LR; Systemstart-->SomeIcon(<img src='https://github.com/Sivolc2/redpoint_hacks/blob/main/img/test.png' width='50' height='50' />)"""
    render_mermaid_with_images(graph_definition)


# # Define your javascript
# my_js = """
# alert("Hello World");
# """

# # Wrapt the javascript as html code
# my_html = f"<script>{my_js}</script>"

# # Execute your app
# st.title("Javascript example")
# html(my_html)

