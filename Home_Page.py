import streamlit as st

st.set_page_config(
    page_title="My Webpage",
    page_icon=":tada:",
    layout="wide")
st.write("CS 1301 - Johnny Bravo (Julia Henggeler)")
st.title("Web Development Lab 01")
st.sidebar.success("Select which page you'd like to visit!")
st.subheader("Welcome to the Johnny Bravo Show!")
st.markdown("Where fitness is our #1 goal, baby!")
st.divider()
st.markdown(
    """
    With my amazing help, you'll be able to navigate this page like a pro, with these hunks of biceps leading you every step of the way.
    To begin, click on the sidebar to the left to access the (amazing) menu I've prepared, giving you access to two different, unique pages:
    """)
st.write("1. **Johnny Bravo's Portfolio:** A peek into the expertise and experience of yours truly - THE Johnny Bravo!")
st.write("2. **Bravo's Body Bootcamp:** How my plentiful fitness knowledge can make you succeed (with data to prove it!).")
    
