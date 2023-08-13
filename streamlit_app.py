from pathlib import Path
import os
import replicate
# from langchain.llms import OpenAI
import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import requests

DB_PATH = (Path(__file__).parent / "Chinook.db").absolute()

openai_key = os.getenv("OPENAI_API_KEY")

# Replicate CONSTANTS
MODEL = "stability-ai/sdxl"
VERSION = "a00d0b7dcbb9c3fbb34ba87d2d5b46c56969c84a628bf778a7fdaec30b1b99c5"

def build_prompt(user_input):
    # Placeholder. Modify as required.
    # llm = OpenAI(openai_api_key=openai_key)
    # text = f'I need a single stable diffusion prompt to generate a imagery representing the following note:\n {user_input}. The style should be memorable, simple design and high contrast/logo colors.'

    # llm(text)
    return user_input

# st.title("🦜 LangChain: Chat with search")
st.set_page_config(
    page_title="Theia", page_icon="👀🧠", layout="wide", initial_sidebar_state="collapsed"
)

"# 👀🧠 Theia: Connect your ideas"
openai_api_key = st.write(
    os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"],
)
# Replicate Variables
replicate_api_key = st.write(
    os.environ["REPLICATE_API_TOKEN"] == st.secrets["REPLICATE_API_TOKEN"],
)
model = replicate.models.get(MODEL)
version = model.versions.get(VERSION)
output_url = ''

## Base HTML will be initial pre-build nodes from Obsidian
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
        """ + f"""
                var graphDefinition = `graph LR; 
                            B[<img src='https://i.imgur.com/n5w3eNs.png' width='250' height='250'>]
                            A[<img src='https://i.imgur.com/38U9Iag.png' width='250' height='250'>]
                            C[<img src='https://i.imgur.com/QEg6015.png' width='250' height='250'>]
                            D[<img src='https://i.imgur.com/NvhoSK6.png' width='250' height='250'>]
                            E[<img src='https://i.imgur.com/Vcfw3Dy.png' width='250' height='250'>]
                        A-->B
                        B-->C
                        B-->D
                        B-->E
                `
                var graph = mermaidAPI.render("mermaid", graphDefinition, insertSvg);
            </script>

            </body>
            </html>
        """

# Existing imports and setup
# tabs = st.tabs(["Input", "Visualization"])

# with tabs[0]:
    # with st.form(key="form"):
user_input = st.text_input("Add an item to your visualizer")
html(my_html, height=1000)
# submit_clicked = st.form_submit_button("Build visualization")
if user_input:
    st.write("Visualize my life 🧠...")
    st.write('Converting into a Stable Diffusion prompt...')
    processed_prompt = build_prompt(user_input)
    st.write('Sending prompt to Stable Diffusion...')
    output_url = version.predict(
        prompt = processed_prompt)[0]

    st.write('Building Chart...')
    # Fetch the image from the URL
    response = requests.get(output_url, stream=True)
    img = Image.open(response.raw)

    # Cap the image's resolution to (width, height)
    max_width = 300
    max_height = 300

    # Resize the image maintaining the aspect ratio
    img.thumbnail((max_width, max_height))
    # Display the image in the Streamlit app
    # st.image(img, caption='Your Generated Image', use_column_width=False)

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
            """ + f"""
                    var graphDefinition = `graph LR; 
                            B[<img src='https://i.imgur.com/n5w3eNs.png' width='250' height='250'>]
                            A[<img src='https://i.imgur.com/38U9Iag.png' width='250' height='250'>]
                            C[<img src='https://i.imgur.com/QEg6015.png' width='250' height='250'>]
                            D[<img src='https://i.imgur.com/NvhoSK6.png' width='250' height='250'>]
                            E[<img src='https://i.imgur.com/Vcfw3Dy.png' width='250' height='250'>]
                            F[<img src='{output_url}' width='250' height='250'>]
                            A-->B
                            B-->C
                            B-->D
                            B-->E
                            B-->F
                    `
                    var graph = mermaidAPI.render("mermaid", graphDefinition, insertSvg);
                </script>

                </body>
                </html>
            """
    # st.markdown(my_html, unsafe_allow_html=True)
    html(my_html, height=2200)

# with tabs[1]:
