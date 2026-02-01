import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configuration
st.set_page_config(
    page_title="NICE Academy",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_frontend():
    """
    Loads the React frontend built in the 'dist' directory.
    """
    # Locate the dist folder
    # When deployed, the script is usually at the root, so dist is ./dist
    build_dir = os.path.join(os.path.dirname(__file__), "dist")
    index_path = os.path.join(build_dir, "index.html")

    if not os.path.exists(index_path):
        st.error("Build artifact not found. Please run 'npm run build' first.")
        # Debug info
        st.write(f"Current working directory: {os.getcwd()}")
        st.write(f"Looking for index at: {index_path}")
        st.write("Files in current directory:")
        st.write(os.listdir(os.getcwd()))
        if os.path.exists(build_dir):
            st.write(f"Files in {build_dir}:")
            st.write(os.listdir(build_dir))
        return

    # Read the index.html file
    try:
        with open(index_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        # Remove default Streamlit padding to make it look like a native app
        st.markdown(
            """
            <style>
                .block-container {
                    padding: 0 !important;
                }
                /* Hide Streamlit elements */
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
            </style>
            """,
            unsafe_allow_html=True
        )
        
        # Render the HTML
        # height=1000 is a placeholder; usually we want it to fit the screen.
        # But for a long page like this, a large height is better.
        components.html(html_content, height=1000, scrolling=True)
        
    except Exception as e:
        st.error(f"Error loading frontend: {e}")

if __name__ == "__main__":
    load_frontend()
