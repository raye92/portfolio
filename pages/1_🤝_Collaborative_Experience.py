import streamlit as st
from utils import file_code

def colab_page():
    st.set_page_config(page_title = "Team Experience", page_icon = "🤝")

    st.title("Teamwork Experience: 599 Robodox")

    intro()
    vision()

def intro():
    columns = st.columns(2)
    columns[0].image("./data/robodox.jpg", caption = "State Champions using CV sensor in autonomous program", use_column_width = "auto", output_format = "JPEG")
    columns[1].markdown("""
    ### Role: Captain
    I fostered collaborative teamwork with a common goal in mind: building an efficient and innovative robot.
    ### Role: Head programmer
    I led writing and designing effective autonomous functions with sensors and real-time data integration to enable precise robot navigation and decision-making (see below).
    """)

def vision():
    st.write("# Vex Vision Sensor Demo")
    st.write("In this project, I implemented a PID (Proportional-Integral-Derivative) control loop using the V5 Vision Sensor for autonomous functions.")

    columns = st.columns([3, 4] , gap = "medium")
    columns[0].video("./data/vision_demo.mp4")
    columns[1].write("Vision sensor utilization: ")
    columns[1].image("./data/visionUI.png")
    columns[1].image("./data/p_calculation.png")

    st.write("With Vex's computer vision library we can calculate the error for PID (( x + 1/2 width ) - midpoint 158) to center our robot to the game element.")
    st.image("./data/pid_diagram.png")
    st.write("Continuously calculating error at short intervals allows us to minimize motor overshooting, oscillation, and steady-state error. Error multiplied by dt for the derivative term, and Error multiplied by t for the integral term. ")

    file_code("./data/vision_code.txt", True)

if __name__ == "__main__":
    colab_page()
