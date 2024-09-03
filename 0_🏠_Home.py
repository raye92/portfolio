import streamlit as st

def home_page():
    st.set_page_config(page_title = "Home", page_icon="🏠")

    st.markdown("""
    # Hi. I'm Ray. A Programmer.
    I have a passion for problem solving, software development, and artificial intelligence.
    """)

    st.image("./data/pfp.jpg", width = 200)


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


    st.sidebar.success("Select a page above.")


if __name__ == "__main__":
    home_page()
