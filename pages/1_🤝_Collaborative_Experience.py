import streamlit as st
from utils import show_code

def colab_page():
    st.set_page_config(page_title = "Team Experience", page_icon = "🤝")

    st.title("Teamwork Experience: 599 Robodox")
    columns = st.columns(2)
    columns[0].image("./data/robodox.jpg", caption = "State Champions using CV sensor in autonomous program", use_column_width = "auto", output_format = "JPEG")
    columns[1].markdown("""### Captain
    Fostering colaborative teamwork with a common goal in mind; building a efficient and innovative robot.
    """)


if __name__ == "__main__":
    colab_page()
