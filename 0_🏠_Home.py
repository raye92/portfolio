import streamlit as st
from streamlit_timeline import timeline

def home_page():
    st.set_page_config(page_title = "Home", page_icon="🏠")

    st.sidebar.success("Select a page above.")

    st.markdown("""
    # Hi. I'm Ray. A Programmer.
    I have a passion for problem solving, software development, and artificial intelligence.
    """)

    st.image("./data/pfp.jpg", width = 200)

    timeline_js()

    st.subheader("Skills & Tools ⚒️")
    skills = ["Python", "C++", "Java", "SQL", "RobotC", "Machine Learning", "Data Analysis & Visualization", "Database Management", "Backend Development", "Artificial Intelligence", "Computer Vision", "Pandas", "sk-learn"]
    skill = iter(skills)
    num_columns = 5
    for x in range( 1 + (len(skills) // num_columns) ):
        column = st.columns(num_columns)
        for i in range(num_columns):
            try:
                column[i].button(next(skill))
            except:
                break


def timeline_js():
    st.subheader("Career Overview")
    with st.spinner(text="Building line"):
        with open('./data/timeline.json', "r") as f:
            data = f.read()
            timeline(data, height=500)

if __name__ == "__main__":
    home_page()
