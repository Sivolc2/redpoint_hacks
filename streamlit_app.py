from pathlib import Path
import os
import replicate
import streamlit as st
from streamlit.components.v1 import html

DB_PATH = (Path(__file__).parent / "Chinook.db").absolute()

# Replicate CONSTANTS
MODEL = "stability-ai/stable-diffusion"
VERSION = "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf"

def build_prompt(user_input):
    # Placeholder. Modify as required.
    return user_input

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
                    mermaidAPI.initialize({ startOnLoad: false });
                    var element = document.getElementById("app");
                    var insertSvg = function(svgCode, bindFunctions) {
                        element.innerHTML = svgCode;
                    };
                    var graphDefinition = `{graph_definition}`;
                    var graph = mermaidAPI.render("mermaid", graphDefinition, insertSvg);
                </script>
                </body>
                </html>
            """
            
            with tabs[1]:
                html(my_html)
