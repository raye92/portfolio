import streamlit as st
import inspect

def show_code(page):
    """Showing the code of the page."""
    show_code = st.sidebar.checkbox("Show code", False)
    if show_code:
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(page)
        st.code("".join(sourcelines))
