import streamlit as st

pages_dict = {
    "Home": [],
    "Work": ["Model 1", "Model 2"],
}

def main():
    st.sidebar.title("Pages")
    main_category = st.sidebar.radio("", list(pages_dict.keys()))

    if main_category in pages_dict:
        subcategories = pages_dict[main_category]
        if subcategories:
            sub_category = st.sidebar.selectbox("", subcategories)
        else:
            sub_category = None

    # Page content based on selection
    if main_category == "Home":
        st.title("Home Page")
        # Add your home page content here
    elif main_category == "Work" and sub_category == "Model 1":
        st.title("Model 1")
        # Add Model 1 content here
    elif main_category == "Work" and sub_category == "Model 2":
        st.title("Model 2")
        # Add Model 2 content here

if __name__ == "__main__":
    main()
