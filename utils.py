import streamlit as st
import inspect

def show_code(page, default = False):
    """Showing the code of the page."""
    show_code = st.sidebar.checkbox("Show code", default)
    if show_code:
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(page)
        st.code("".join(sourcelines))

def file_code(path, default = True):
    """Showing content from a file"""
    show_code = st.sidebar.checkbox("Show code", default)
    if show_code:
        st.write("### Sample snapshot: ")
        try:
            with open(path, 'r') as file:
                content = file.read()
            st.code(content)
        except FileNotFoundError:
            st.error("No file")
