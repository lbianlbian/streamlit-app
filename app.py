import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
#run it with this command py -m streamlit run app.py
#for reference: https://docs.streamlit.io/
st.title("Wesley Bian - STATS 21 Participation Project")

#need to have a button to upload a csv file
data = st.file_uploader("upload csv file here")

#show statistics about dataset
if data != None:
    df = pd.read_csv(data)
    st.markdown("Number of rows: " + str(df.shape[0]))
    st.markdown("Number of columns: " + str(df.shape[1]))
    numeric_cols = df.select_dtypes(include = "number")
    categorical_cols = df.select_dtypes(include = "object")
    st.markdown("Number of numerical variables: " + str(numeric_cols.shape[1])) #
    st.markdown("Number of categorical variables: " + str(categorical_cols.shape[1])) #object
    st.markdown("Number of bool variables: " + str(df.select_dtypes(include = "bool").shape[1]))
    col = st.selectbox("Select a column", df.columns)
    if col != None:
        series = df[col]
        if col in numeric_cols.columns:
            st.table(series.describe().loc[['min', '25%', '50%', '75%', 'max']])
            possible_colors = ["red", "green", "blue", "yellow", "cyan"]
            rand_color = possible_colors[random.randint(0, len(possible_colors))]
            #plot distribution
            fig, ax = plt.subplots()
            ax.hist(series, color = rand_color)
            plt.title("Distribution of " + col)
            plt.xlabel(col)
            plt.ylabel("frequency")
            st.pyplot(fig)
            # do some more customization somehow
        elif col in categorical_cols.columns:
            st.table(series.value_counts() / 200)
            #barplot
            st.bar_chart(series.value_counts())
#plt.style.available gives all of the matplotlib styles
#def func(argname:type = default) -> return type:
#from typing import List, Optional, Tuple
#pip3 install git+githuburl to instsall a github repository

