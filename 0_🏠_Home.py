import streamlit as st

def home_page():
    st.set_page_config(page_title = "Home", page_icon="🏠")

    st.markdown("""
    # Hi. I'm Ray. A Programmer.
    I have a passion for problem solving, software development, and artificial intelligence.
    """)

    st.image("./data/pfp.jpg", width = 200)

    st.write("### Skills")

    st.button("Python")
    st.button("Pandas")
    st.button("sk-learn")
    st.button("Artificial Intelligence")

    st.sidebar.success("Select a page above.")


if __name__ == "__main__":
    home_page()
