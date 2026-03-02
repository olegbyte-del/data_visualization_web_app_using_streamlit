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
    
    columns = df.columns.tolist()
    
    with col1:
        st.write("")
        st.write(df.head())

    with col2:
        # User selection of df columns
        x_axis = st.selectbox("Select the X-axis", options = columns + ["None"], index=None)
        y_axis = st.selectbox("Select the Y-axis", options = columns + ["None"], index=None)
        
        plot_list = ["Line Plot", "Bar Chart", "Scatter PLot", "Distribution Plot", "Count Plot"]
        
        selected_plot = st.selectbox("Select a pot", options=plot_list, index = None)
        
        st.write(x_axis)
        st.write(y_axis)
        st.write(selected_files)
        
# button to generate plots
if st.button("Generate Plot"):
    
    fig, ax = plt.subplot(figsize = (6, 4))
    
    if selected_plot == "Line Plot":
        sns.lineplot(x = df[x_axis], y = df[y_axis], ax=ax)
    
    elif selected_plot == "Bar Chart":
        sns.barplot(x = df[x_axis], y = df[y_axis], ax=ax)
        
    elif selected_plot == "Scatter Plot":
        sns.scatterplot(x = df[x_axis], y = df[y_axis], ax=ax)
        
    elif selected_plot == "Distribution Plot":
        sns.histplot(df[x_axis], kde=True, ax=ax)
    
    elif selected_plot == "Count Plot":
        sns.countplot(df[x_axis], kde=True, ax=ax)
    
    # adjust label sizes
    ax.tick_params(axis="x", labelsize = 10)
    ax.tick_params(axis="y", labelsize = 10)
    
    # title axes labels
    
    plt.title(f"{selected_plot} of {y_axis} vs {x_axis}", fontsize = 12)
    plt.xlabel(x_axis, fontsize = 10)
    plt.ylabel(y_axis, fontsize = 10)
    
    st.pyplot(fig)
    