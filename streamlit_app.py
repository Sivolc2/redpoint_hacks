from pathlib import Path
import os
import replicate

import streamlit as st
from streamlit.components.v1 import html

DB_PATH = (Path(__file__).parent / "Chinook.db").absolute()

def render_mermaid_with_images(graph_definition):
    my_html = f"""
        <script src="https://unpkg.com/mermaid@8.0.0-rc.8/dist/mermaid.min.js"></script>
        <script src="https://raw.githubusercontent.com/Sivolc2/redpoint_hacks/main/mermaid_with_images.js"></script>
        <div id="mermaid-chart"></div>
        <script>
            var graphDefinition = `{graph_definition}`;
            renderMermaid("mermaid-chart", graphDefinition);
        </script>
        """
    # st.write(
    #     s,
    #     unsafe_allow_html=True,
    # )
    html(my_html)
    # st.markdown(my_html, unsafe_allow_html=True)

# st.title("🦜 LangChain: Chat with search")
st.set_page_config(
    page_title="Theia", page_icon="*", layout="wide", initial_sidebar_state="collapsed"
)

"# 🦜🔗 Theia: Connect your ideas"
openai_api_key = st.write(
    os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"],
)
# Replicate Variables
replicate_api_key = st.write(
    os.environ["REPLICATE_API_TOKEN"] == st.secrets["REPLICATE_API_TOKEN"],
)
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get(
    "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")

# Existing imports and setup
tabs = st.tabs(["Input", "Visualization"])

with tabs[0]:
    with st.form(key="form"):
        user_input = st.text_input("Add an item to your visualizer")
        output_url = version.predict(
            prompt = user_input)[0]
        
        # Display the image in the Streamlit app
        st.image(output_url, caption='Generated Image', use_column_width=True)

        # yourfunction(user_input)
        # if not user_input:
        #     user_input = prefilled
        submit_clicked = st.form_submit_button("Build visualization")
    
    # graph_definition = f"""graph LR; Systemstart-->SomeIcon(<img src='https://github.com/Sivolc2/redpoint_hacks/blob/main/img/test.png?raw=true' width='50' height='50' />)"""
    # render_mermaid_with_images(graph_definition)

with tabs[1]:
    # my_html = """
    # <!DOCTYPE html>
    # <html lang="en">
    # <body>



    #     <script src="https://unpkg.com/mermaid@8.0.0-rc.8/dist/mermaid.min.js"></script>
    #     <script type="text/javascript" src="https://github.com/Sivolc2/redpoint_hacks/blob/main/mermaid/mermaid_graph.js"></script>

    # </body>
    # </html>
    # """
    my_html = """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <!-- You might want to include meta and other tags here. -->
        </head>
        <body>

        <div id="app"></div> <!-- This is where the Mermaid graph will render. -->

        <script src="https://unpkg.com/mermaid@8.0.0-rc.8/dist/mermaid.min.js"></script>

        <!-- Inlined JavaScript from mermaid_graph.js -->
        <script type="text/javascript">
            var mermaidAPI = mermaid.mermaidAPI;

            mermaidAPI.initialize({
            startOnLoad: false
            });

            var element = document.getElementById("app");
            var insertSvg = function(svgCode, bindFunctions) {
            element.innerHTML = svgCode;
            };
            var graphDefinition = `graph LR; Nodetext-->SomeIcon(<img src='https://store.nytimes.com/cdn/shop/products/notebook-chambray_1024x1024.jpg?v=1571439076' width='40' height='40' />)`;
            var graphDefinition2; // This variable is declared but not used in your provided script.
            var graph = mermaidAPI.render("mermaid", graphDefinition, insertSvg);
        </script>

        </body>
        </html>
    """
    html(my_html)
#     graph_definition = f"""graph LR; Systemstart-->SomeIcon(<img src='https://github.com/Sivolc2/redpoint_hacks/blob/main/img/test.png' width='50' height='50' />)"""
#     render_mermaid_with_images(graph_definition)


# Define your javascript
my_js = """
alert("Hola mundo");
"""

# Wrapt the javascript as html code
my_html = f"<script>{my_js}</script>"

# Execute your app
st.title("Javascript example")
html(my_html)

