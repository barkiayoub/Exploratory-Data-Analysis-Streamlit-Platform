# Importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components

# Setting the page configuration
st.set_page_config(
    page_title="Exploratory Data Analysis Plateform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Adding some CSS for a better UI
st.markdown("""
    <style>
        .main {
            background-color: #dark;
        }
        .report-container {
            max-width: 100%;
        }
        .css-18e3th9 {
            padding-top: 0rem;
        }
        .css-1d391kg {
            padding-top: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

# Title of the web app
st.markdown("""
# **Exploratory Data Analysis Plateform**  
   **Upload your dataset and generate an interactive EDA report!**                    
""")

st.sidebar.header("Upload your CSV file")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Sidebar for user interactions
st.sidebar.header("Instructions")
st.sidebar.markdown("""
1. **Upload your CSV file**: Use the file uploader below to upload your CSV dataset.
2. **View the DataFrame**: The uploaded dataset will be displayed in the main page.
3. **Generate EDA Report**: An interactive profiling report will be generated and displayed.
4. **Explore the Report**: Scroll through the report for insights and visualizations.
""")

# Function to load data
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# Function to generate profile report
@st.cache_data
def generate_profile_report(dataframe):
    profile = ProfileReport(dataframe, title="Dataset Report", dark_mode=True)
    return profile

# If file is uploaded, load data and display profiling report
if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.header('**Input DataFrame**')
    st.write(df)
    profile_html = generate_profile_report(df).to_html()

    st.header('**Profiling Report**')
    # Download button to download the HTML report
    st.download_button(
        label="Download Report as HTML",
        data=profile_html,
        file_name="EDA_Report.html",
        mime="text/html"
    )

    components.html(profile_html, height=1000, scrolling=True)
    
# If no file is uploaded, display info and offer example dataset
else:
    st.sidebar.info('Awaiting for CSV file to be uploaded...')
    if st.sidebar.button('Press to use Example Dataset'):
        @st.cache_data
        def load_example_data():
            return pd.DataFrame(np.random.rand(100, 5), columns=['a', 'b', 'c', 'd', 'e'])

        df = load_example_data()
        st.header('**Example DataFrame**')
        st.write(df)

        st.header('**Profiling Report**')
        profile_report = generate_profile_report(df)
        profile_html = profile_report.to_html()
        components.html(profile_html, height=1000, scrolling=True)
