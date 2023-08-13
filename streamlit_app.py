from pathlib import Path
from dotenv import load_dotenv
import os
import replicate
from langchain.llms import OpenAI
import streamlit as st
from streamlit.components.v1 import html

DB_PATH = (Path(__file__).parent / "Chinook.db").absolute()
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Replicate CONSTANTS
MODEL = "stability-ai/sdxl"
VERSION = "a00d0b7dcbb9c3fbb34ba87d2d5b46c56969c84a628bf778a7fdaec30b1b99c5"

def build_prompt(user_input):
    # Placeholder. Modify as required.
    llm = OpenAI(openai_api_key=openai_key)
    text = f'I need a single stable diffusion prompt to generate a imagery representing the following note:\n {doc}. The style should be memorable, simple design and high contrast/logo colors.'
    return llm(text)

def export_prompt(processed_prompt):
    with open('./data/output_prompt.txt', 'a') as file:
        file.write(processed_prompt + '\n')

st.set_page_config(
    page_title="Theia", page_icon="*", layout="wide", initial_sidebar_state="collapsed"
)

"# 🦜🔗 Theia: Connect your ideas"

# Ensure you have valid API keys.
model = replicate.models.get(MODEL)
version = model.versions.get(VERSION)

tabs = st.tabs(["Input", "Visualization"])

with tabs[0]:
    with st.form(key="form"):
        user_input = st.text_input("Add an item to your visualizer")
        submit_clicked = st.form_submit_button("Build visualization")

        if user_input:
            processed_prompt = build_prompt(user_input)
            export_prompt(processed_prompt)
            
            # Now read from the saved prompts and generate the graph
            with open('./data/output_prompt.txt', 'r') as file:
                lines = file.readlines()

            graph_nodes = []
            graph_relations = []
            for idx, line in enumerate(lines):
                line = line.strip()
                output_url = version.predict(prompt=line)[0]
                node_str = f"A{idx}[<img src='{output_url}' width='100' height='100' />]"
                graph_nodes.append(node_str)

                if idx > 0:
                    graph_relations.append(f"A{idx-1}-->A{idx}")
            
            graph_definition = ";\n".join(graph_nodes + graph_relations)
            # Construct the graph in HTML
            graph_def_script = f"""var graphDefinition = `{graph_definition}`;var graph = mermaidAPI.render("mermaid", graphDefinition, insertSvg);
                </script>
                </body>
                </html>"""
            
            my_html = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <!-- You might want to include meta and other tags here. -->
                </head>
                <body>

                <div id="app"></div> <!-- This is where the Mermaid graph will render. -->

                <script src="https://unpkg.com/mermaid@8.0.0-rc.8/dist/mermaid.min.js"></script>
                <script type="text/javascript">
                    var mermaidAPI = mermaid.mermaidAPI;
                    mermaidAPI.initialize({{ startOnLoad: false }});
                    var element = document.getElementById("app");
                    var insertSvg = function(svgCode, bindFunctions) {{
                        element.innerHTML = svgCode;
                    }};                    
            """ + graph_def_script

            print('Running', my_html)
            html(my_html)
