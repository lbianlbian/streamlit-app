import streamlit as st
#run it with this command py -m streamlit run app.py
#for reference: https://docs.streamlit.io/
st.title("STATS 21 Wesley Bian Participation Project")
st.markdown("**test**testtesttest")

st.sidebar.title("title of my sidebar")

agree = st.checkbox("I agree")
if agree:
    st.write("Great!")
#sidebaragree = st.sidebar.checkbox("I agree")

side_check = st.sidebar.checkbox("click me")
if side_check:
    st.sidebar.write("sidebar checkbox clicked")
    st.write("sidebar checkbox clicked main notification")