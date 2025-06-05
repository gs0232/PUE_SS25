import streamlit as st
from src.load_subject_data import load_subject_data, get_subject_names, get_subject_image
from PIL import Image
from src.analyze_hr_data import load_activity_data, set_max_hr, assign_zones, zone_time_and_power, plot_hr_data


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
SUBJECT_PATH = "data/person_db.json"

user_data = load_subject_data(SUBJECT_PATH)
name_list = []
for person in user_data:
    name_list.append(person.firstname + " " + person.lastname)
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

st.write(f"# {st.session_state.current_subject}")

# Add images
st.image(get_subject_image(user_data, st.session_state.current_subject), caption=st.session_state.current_subject)

# Dataframe with subject data
st.write("### Subject Data")

max_hr_input = st.number_input(
    "Gib deine maximale Herzfrequenz ein (in bpm):",
    min_value=100,
    max_value=250,
    value=200,  # Standardwert
    step=1
)
    
#max_hr_input = int(max_hr_subject)    
ACTIVITY_PATH = "data/activity.csv"
df_subject = load_activity_data(ACTIVITY_PATH)
#max_hr_subject = set_max_hr(df_subject["HeartRate"].max())
max_hr_subject = set_max_hr(max_hr_input)
df_subject, time_in_zones_subject = assign_zones(df_subject, max_hr_subject)

st.table(zone_time_and_power(df_subject, time_in_zones_subject))

# Plot the heart rate data
st.plotly_chart(plot_hr_data(df_subject, max_hr_subject))
