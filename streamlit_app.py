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
    build_dir = os.path.join(os.path.dirname(__file__), "dist")
    index_path = os.path.join(build_dir, "index.html")

    if not os.path.exists(index_path):
        st.error("Build artifact not found. Please run 'npm run build' first.")
        st.info("If you are deploying on Streamlit Cloud, ensure 'packages.txt' includes 'nodejs' and 'npm'.")
        return

    # Read the index.html file
    try:
        with open(index_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        # Basic approach: Render the HTML in an iframe
        # Note: Relative paths in index.html (like /assets/...) may need adjustment 
        # depending on how Streamlit serves static files.
        # For a production-grade integration, consider using 'streamlit-component-template' 
        # or serving static files via a separate backend.
        
        st.markdown(
            """
            <style>
                /* Remove default Streamlit padding */
                .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        components.html(html_content, height=1000, scrolling=True)
        
    except Exception as e:
        st.error(f"Error loading frontend: {e}")

if __name__ == "__main__":
    load_frontend()
