import streamlit as st
from src.load_subject_data import load_subject_data, get_subject_names, get_subject_image
from PIL import Image


st.set_page_config(
    page_title="EKG App",
    #page_icon=":heart:",
    layout="centered",
    initial_sidebar_state="auto",
    )

# Sicherstellen, dass auch vor der Nutzerwahl schon ein Wert im SessionState ist
if "current_subject" not in st.session_state:
    current_subject = "No subject selected"

# Import name list
FILE_PATH = "data/person_db.json"

user_data = load_subject_data(FILE_PATH)
name_list = get_subject_names(user_data)
print(name_list)

# A header for the first layer
st.title("EKG App") # or st.write("EKG App")
st.write("This app offers a simple interface to select a test subject and view the EKG data.")

# A header for the second layer
st.write("### Select test subject")

# A selectbox for the second layer
st.session_state.current_subject = st.selectbox(
    "Select a test subject",
    options=name_list, key="sbSubject"
    )

st.write(f"## {st.session_state.current_subject}")

# Add images
st.image(get_subject_image(st.session_state.current_subject), caption=st.session_state.current_subject)
