import streamlit as st
import pandas as pd
import numpy as np
import json

file = open('bravodata.json') #.json file
data = json.load(file)
file.close()

file_two = open('bravodata2.json') #.json file
data_two = json.load(file_two)
file_two.close()

file_three = open('bravodata3.json') #.json file
data_three = json.load(file_three)
file_three.close()

st.title("Bravo's Body Bootcamp: Your Future in Fitness!") # Second page
st.markdown(
    """
    This program is designed to replicate the fantastic figure of Johnny Bravo (that's me!) through rigorous, specialized programs based on your body!

    This includes auto-generated fitness programs based on user inputs, recommended meal plans, and motivational quotes that are day-dependent!

    But, without the data to prove it, what kinda personal trainer would I be?

    Check out the results (including real time updates!):
    """)
tab1,tab2,tab3 = st.tabs(["Muscle Growth","Endurance Growth","Cardiovascular Health"]) # tabs for graphs

with tab1:
    chart_data = pd.DataFrame(data)
    chart_data = chart_data.set_index("How Far Into the Program (weeks)")
    st.line_chart(chart_data) #NEW
    st.caption("_Fig 1._ Line chart showing the relationship between time and muscle mass, from clients pursuing Johnny Bravo'2_Bravo's_Body_Bootcamp.py")
    st.write("This graph shows how my exercise routine will give you the pump of your lifetime, using actual data from my clientele!")
with tab2:
    hours = st.select_slider(
        "How many hours of cardio will you do a week?",
        options =[
            "1",
            "2",
            "3",
            "4",
            "5",
            "6+"
        ]
    )
    st.subheader(f"Growth for {hours} hrs/week")
    if hours == "1":
        endurance_df = pd.DataFrame(data_two[0])
        st.line_chart(data = endurance_df, x = "Weeks Trained", y = "Endurance Growth (%)")
    elif hours == "2":
        endurance_df = pd.DataFrame(data_two[1])
        st.line_chart(data = endurance_df, x = "Weeks Trained", y = "Endurance Growth (%)")
    elif hours == "3":
        endurance_df = pd.DataFrame(data_two[2])
        st.line_chart(data = endurance_df, x = "Weeks Trained", y = "Endurance Growth (%)")
    elif hours == "4":
        endurance_df = pd.DataFrame(data_two[3])
        st.line_chart(data = endurance_df, x = "Weeks Trained", y = "Endurance Growth (%)")
    elif hours == "5":
        endurance_df = pd.DataFrame(data_two[4])
        st.line_chart(data = endurance_df, x = "Weeks Trained", y = "Endurance Growth (%)")
    elif hours == "6+":
        endurance_df = pd.DataFrame(data_two[5])
        st.line_chart(data = endurance_df, x = "Weeks Trained", y = "Endurance Growth (%)")
    st.caption("_Fig 2._ This graph shows the relationship between endurance and time spent training under the Bravo regimen, depending on hours committed to cardio weekly. This is a **dynamic** graph.")
    st.write("Again, flawless results proving the effectiveness of the Bravo way! Growth in endurance is the y-axis, while weeks trained under the one-man army are seen in x-axis.")
with tab3:
    hours = st.selectbox(
        "How many hours of training will you do weekly??",
        options =[
            "3",
            "4",
            "5",
            "6+"
        ]
    )
    st.subheader(f"Growth for {hours} hrs/week")
    if hours == "3":
        health_df = pd.DataFrame(data_three[0])
        st.line_chart(data = health_df, x = "Weeks Trained", y = "Cardiovascular Disease Risk (%)")
    elif hours == "4":
        health_df = pd.DataFrame(data_three[1])
        st.line_chart(data = health_df, x = "Weeks Trained", y = "Cardiovascular Disease Risk (%)")
    elif hours == "5":
        health_df = pd.DataFrame(data_three[1])
        st.line_chart(data = health_df, x = "Weeks Trained", y = "Cardiovascular Disease Risk (%)")
    elif hours == "6+":
        health_df = pd.DataFrame(data_three[1])
        st.line_chart(data = health_df, x = "Weeks Trained", y = "Cardiovascular Disease Risk (%)")
    st.caption("_Fig 3._ This graph shows the relationship between likelihood of cardiovascular disease (%) and the weeks trained under the Bravo regimen, depending on hours exercised in a week.")
    st.write("Finally, and likely the most compelling data, showing how cardiovascular disease (y-axis) has a significant drop when testing my routine for weeks on end (x-axis)!")

st.divider()

st.title("Program Options")
st.write(
    """
    Now that I've captured your attention, let's get into the actual programs!
    
    I've got three programs for you, with increasing difficulty based on how badly you'd like to look like me.
    1. **Easy:** Slow and steady approach
    2. **Medium:** Safe option, but not too much of a bore for the energetic folks!
    3. **Hard:** Pushing your limits, I like it!

    To determine the most suitable program, answer the questionnaire below!
    """
    )
days = st.selectbox("How many days a week do you plan on exercising?",[1,2,3,4,5,6,7]) #NEW
if int(days) >= 5:
    st.caption("Wiggy!")
elif int(days) > 3:
    st.caption("Solid routine!")
elif int(days) <= 3:
    st.caption("Every bit counts, if you want to look like me!")
choice = st.selectbox("Do you have access to a gym?", ["Yep!","Nope..."])
if choice == "Yep!":
    st.caption("Great!")
else:
    st.caption("Gotta try extra hard!")
if int(days) >=5:
    st.subheader("Purchase the Hard plan below!")
elif int(days) > 3 and choice == "Yep!":
    st.subheader("Purchase the Hard plan below!")
elif int(days) <= 3 and choice == "Nope...":
    st.subheader("Purchase the Medium plan below!")
else:
    st.subheader("Purchase the Easy plan below!")
    
st.divider()

st.write("Short on cash? Don't stress it --- explore that slick graph on the right to see what's suitable to your needs!")

col1,col2 = st.columns(2) #NEW

with col1:
    st.link_button("Hard Plan", "https://hardplanbravo.com/gallery")
    st.caption("This doesn't lead anywhere, but it's clickable/has a url.")
    st.markdown("Includes two full 5-day and 6-day workout routines and exclusive Johnny Bravo personal training guidance!")
    st.link_button("Medium Plan", "https://mediumplanbravo.com/gallery")
    st.caption("This doesn't lead anywhere, but it's clickable/has a url.")
    st.markdown("Includes a full 4-day workout routine!")

    st.link_button("Easy Plan", "https://hardplanbravo.com/gallery")
    st.caption("This doesn't lead anywhere, but it's clickable/has a url.")
    st.markdown("Includes a full 3-day workout routine!")
with col2:
    budget = st.select_slider(
        "What's your budget?",
        options =[
            ">50",
            "50-75",
            ">75"
            ]
        )
    if budget == ">75":
        st.write("Go at it Hard, you'll look like me in no time!")
    elif budget == "50-75":
        st.write("Get a Medium plan; effective, but a little easier on the bank.")
    elif budget == ">50":
        st.write("Easy mode for you, it seems!")
    st.image("https://m.media-amazon.com/images/M/MV5BNzllYWYxNTktODUwYi00ODNhLWE1NzktOGU3MWEzMmU3MDY4XkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_.jpg")
st.title("What if I want a plan for more than one person?")

col1, col2 = st.columns(2)
with col1:
    st.write("""
             Don't fret! You can buy in bulk!

             Click the button as many times as you want for the people you're buying for,
             and you might see a discount!
             """)
    if "click_count" not in st.session_state:
        st.session_state.click_count = 0
    if st.button(f"Click! Me!"): #NEW
        st.session_state.click_count += 1 #NEW
        if st.session_state.click_count <= 5:
            st.write("Unfortunately, no discount is available for your group!")
        else:
            discount = int(st.session_state.click_count) * 5
            st.write(f"Congratulations!!! Your group of {st.session_state.click_count} gets a discount of ${discount}!")
with col2:
    st.write("Make a mistake? Reset the clicks with the button below!")
    if st.button("Reset"):
        st.session_state.click_count = 0

st.caption("These buttons involve a st.session_state function in order to keep track of clicking!")
st.divider()

st.header("Rate this page below!")
st.feedback("stars") # this is useless i just wanted to make the page prettier


# i was going to do theming/font changes but i have no clue what a toml file is :(
