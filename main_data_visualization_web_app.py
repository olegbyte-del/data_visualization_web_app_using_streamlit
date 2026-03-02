import os


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set page configuration (This allows you to edit the web app)
st.set_page_config(page_title="Data Visualizer",
                    layout="centered",page_icon="📊")

# Title
st.title("📊 Data Visualizer - Web App")

# getting the working directory of the main
working_dir = os.path.dirname(os.path.abspath(__file__)) #check datafiles

folder_path = f"{working_dir}/data"

# List the files present in "data" folder
files_list = [f for f in os.listdir((folder_path)) if f.endswith(".csv")] #Returns all the data files

# Dropdown for all the files 
selected_files = st.selectbox("Select a file", files_list, index=None) # Adds a button to chose the file list index is default

if selected_files:
    
    # Get the complete file of the selected file
    file_path = os.path.join(folder_path, selected_files)
    
    # Reading the csv files as a pandas dataframe
    df = pd.read_csv(file_path)
    
    col1, col2 = st.columns(2) # The number of columns depends on the number you put
    
    with col1:
        st.write("")
        st.write(df.head())
    