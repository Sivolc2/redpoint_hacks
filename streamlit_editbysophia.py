import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Theia",
    page_icon="👀🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
    primary_color="#4a90e2"  # Blue color
)

# CSS to set the transparent background image, style the button, and set text colors
st.markdown(
    """
    <style>
        body {
            background-image: url("http://www.scottmcd.net/artanalysis/wp-content/uploads/2010/01/Escher-Big.jpg");
            background-size: cover;
            color: black;  # Setting general text font color to black
        }
        body:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: white;
            opacity: 0.7;  # Adjust the opacity for higher or lower transparency
            pointer-events: none;
            z-index: -1;
        }
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }
        .stButton > button {
            background-color: #4a90e2;  # Button color set to blue
            color: white;  # Button text color set to white
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='center'>👀🧠 Theia: Auto-organize your life visually</div>", unsafe_allow_html=True)

# 1. Upload Raw Data with the new description
st.write("Upload a File")
uploaded_file = st.file_uploader("", type=["txt", "csv", "ics", "pdf", "docx"])

# 2. Enter Prompts with the updated label and default value
prompt = st.text_input("Enter your prompt or question:", value="Where is my AI alignment mind?")

# If the user provides both the raw data and the prompt, allow them to initiate the visualization
if uploaded_file and prompt:
    if st.button("Let's go! 👀"):
        # Placeholder for visualization processing and display
        st.write("Visualize my life 🧠...")
        # Depending on the visualization library you're using, integrate the code to create and display the visualization.
        st.image("path_to_visualization_image.png")  # Replace with actual visualization or path to visualization image.
