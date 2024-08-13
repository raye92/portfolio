import streamlit as st

def home_page():
    st.set_page_config(page_title = "Home", page_icon="🏠")

    st.markdown("""
    # Hi. I'm Ray. A Programmer.
    """)

    st.sidebar.success("Select a page above.")

if __name__ == "__main__":
    home_page()
