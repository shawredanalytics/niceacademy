import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from questions_data import ASSESSMENTS

# Page Config
st.set_page_config(
    page_title="NICE Academy | Competency Assessment",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #0066cc;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #333;
        margin-bottom: 2rem;
    }
    .question-card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0066cc;
        margin-bottom: 20px;
    }
    .success-score {
        color: #28a745;
        font-weight: bold;
    }
    .fail-score {
        color: #dc3545;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def reset_app():
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.assessment_started = False
    st.session_state.user_info = {}
    st.session_state.current_questions = []

def start_assessment(name, role, hospital, assessment_type):
    # Get the questions for the selected assessment type
    # Default to "Other" (Full Set) if not found, but logic should prevent this
    questions = ASSESSMENTS.get(assessment_type, ASSESSMENTS["Other"])
    
    st.session_state.user_info = {
        "name": name,
        "role": role,
        "hospital": hospital,
        "assessment_type": assessment_type,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    st.session_state.current_questions = questions
    st.session_state.assessment_started = True
    st.rerun()

# -----------------------------------------------------------------------------
# APP COMPONENTS
# -----------------------------------------------------------------------------

def show_landing_page():
    st.markdown('<h1 class="main-header">NICE Academy</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header" style="text-align: center;">Healthcare Professional Competency Assessment</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("""
        **Welcome!** This portal allows healthcare professionals to assess their knowledge of:
        - Infection Prevention & Control
        - Standard & Transmission-Based Precautions
        - Hand Hygiene & PPE Protocols
        - Patient Safety Standards
        
        Please enter your details to begin the assessment.
        """)
        
        with st.form("registration_form"):
            name = st.text_input("Full Name", placeholder="e.g. Jane Doe, RN")
            
            # Role Selection
            role_options = [
                "Select your role...",
                "Infection Control Nurse (ICN)",
                "Staff Nurse",
                "Physician / Doctor",
                "Technician / Allied Health",
                "Nursing Assistant / Support Staff",
                "Administrative Personnel",
                "Student",
                "Other"
            ]
            role = st.selectbox("Role / Designation", role_options)
            
            hospital = st.text_input("Hospital / Organization (Optional)", placeholder="e.g. General Hospital")
            
            # Assessment Module Selection (Auto-select based on role if possible, or let user choose)
            st.markdown("---")
            st.markdown("**Select Assessment Module**")
            
            # Map role to assessment type for default selection if possible
            assessment_options = list(ASSESSMENTS.keys())
            
            # Create a radio or selectbox for assessment type
            # We can default it based on the role selected above, but since Streamlit forms 
            # don't update dynamically until submit/rerun, we'll just let them choose or default to a generic one.
            # Ideally, we bind this logic after submission, but explicit choice is better for flexibility.
            
            assessment_type = st.selectbox(
                "Choose the assessment module you wish to take:",
                options=["Match my Role"] + assessment_options,
                index=0,
                help="Select 'Match my Role' to automatically assign the assessment based on your designation."
            )
            
            submitted = st.form_submit_button("Start Assessment", use_container_width=True)
            
            if submitted:
                if name and role != "Select your role...":
                    # Determine final assessment type
                    final_assessment = assessment_type
                    if assessment_type == "Match my Role":
                        # Try to match role to assessment key
                        if role in ASSESSMENTS:
                            final_assessment = role
                        else:
                            # Fallback map or default
                            if "Nurse" in role:
                                final_assessment = "General Staff Nurse"
                            elif "Technician" in role or "Allied" in role:
                                final_assessment = "Technician / Allied Health"
                            elif "Admin" in role:
                                final_assessment = "Administrative Personnel"
                            else:
                                final_assessment = "Other"
                    
                    start_assessment(name, role, hospital, final_assessment)
                else:
                    st.error("Please provide your Name and select a Role to proceed.")

def show_assessment_page():
    questions = st.session_state.current_questions
    
    # Sidebar Info
    with st.sidebar:
        st.write(f"**Candidate:** {st.session_state.user_info['name']}")
        st.write(f"**Role:** {st.session_state.user_info['role']}")
        st.write(f"**Module:** {st.session_state.user_info['assessment_type']}")
        
        progress = st.session_state.current_question / len(questions)
        st.progress(progress)
        st.caption(f"Question {st.session_state.current_question + 1} of {len(questions)}")
        
        if st.button("Quit Assessment"):
            reset_app()
            st.rerun()

    # Question Display
    q_index = st.session_state.current_question
    q_data = questions[q_index]
    
    st.markdown(f"### Question {q_index + 1}")
    st.markdown(f"**Category:** {q_data['category']}")
    
    st.markdown(f"""
    <div class="question-card">
        <h4>{q_data['text']}</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Options
    current_answer = st.session_state.answers.get(q_index, None)
    selected_option = st.radio(
        "Select your answer:",
        q_data['options'],
        index=current_answer if current_answer is not None else None,
        key=f"q_{q_index}",
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Navigation
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Previous", disabled=q_index == 0, use_container_width=True):
            st.session_state.current_question -= 1
            st.rerun()
            
    with col2:
        is_last = q_index == len(questions) - 1
        btn_text = "Submit Assessment 🏁" if is_last else "Next ➡️"
        
        if st.button(btn_text, use_container_width=True):
            # Save answer
            ans_idx = q_data['options'].index(selected_option) if selected_option else None
            
            if ans_idx is not None:
                st.session_state.answers[q_index] = ans_idx
                if not is_last:
                    st.session_state.current_question += 1
                    st.rerun()
                else:
                    st.session_state.submitted = True
                    st.rerun()
            else:
                st.warning("Please select an answer before proceeding.")

def show_results_page():
    questions = st.session_state.current_questions
    st.markdown('<h1 class="main-header">Assessment Report</h1>', unsafe_allow_html=True)
    
    # Calculate Score
    total_q = len(questions)
    correct_count = 0
    category_scores = {}
    
    for i, q in enumerate(questions):
        user_ans = st.session_state.answers.get(i)
        is_correct = (user_ans == q['correctAnswer'])
        if is_correct:
            correct_count += 1
            
        # Category breakdown
        cat = q['category']
        if cat not in category_scores:
            category_scores[cat] = {'correct': 0, 'total': 0}
        category_scores[cat]['total'] += 1
        if is_correct:
            category_scores[cat]['correct'] += 1

    percentage = (correct_count / total_q) * 100
    passed = percentage >= 80  # Stricter pass for professional competency
    
    # Summary Card
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric("Total Score", f"{percentage:.1f}%", f"{correct_count}/{total_q}")
        if passed:
            st.success("Result: COMPETENT ✅")
        else:
            st.error("Result: NEEDS IMPROVEMENT ⚠️")
            
    with col2:
        st.write(f"**Name:** {st.session_state.user_info['name']}")
        st.write(f"**Role:** {st.session_state.user_info['role']}")
        st.write(f"**Assessment Module:** {st.session_state.user_info['assessment_type']}")
        st.write(f"**Date:** {st.session_state.user_info['date']}")
        if st.session_state.user_info['hospital']:
            st.write(f"**Organization:** {st.session_state.user_info['hospital']}")

    st.markdown("---")
    
    # Category Performance Chart
    st.subheader("Competency by Domain")
    
    cat_data = []
    for cat, stats in category_scores.items():
        cat_data.append({
            "Category": cat,
            "Score (%)": (stats['correct'] / stats['total']) * 100,
            "Questions": stats['total']
        })
    
    if cat_data:
        df_cat = pd.DataFrame(cat_data)
        fig = px.bar(df_cat, x="Score (%)", y="Category", orientation='h', 
                     title="Performance Breakdown", 
                     range_x=[0, 100], 
                     color="Score (%)",
                     color_continuous_scale=["red", "yellow", "green"])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No category data available.")

    # Detailed Review
    with st.expander("View Detailed Answer Key"):
        for i, q in enumerate(questions):
            user_ans = st.session_state.answers.get(i)
            correct = user_ans == q['correctAnswer']
            icon = "✅" if correct else "❌"
            
            st.markdown(f"**{i+1}. {q['text']}** {icon}")
            if not correct:
                st.markdown(f"Your Answer: *{q['options'][user_ans] if user_ans is not None else 'Skipped'}*")
                st.markdown(f"Correct Answer: **{q['options'][q['correctAnswer']]}**")
                st.info(f"💡 {q['explanation']}")
            st.markdown("---")

    # Restart
    if st.button("Start New Assessment", use_container_width=True):
        reset_app()
        st.rerun()

# -----------------------------------------------------------------------------
# MAIN APP FLOW
# -----------------------------------------------------------------------------
def main():
    # Initialize Session State
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'assessment_started' not in st.session_state:
        st.session_state.assessment_started = False
    if 'user_info' not in st.session_state:
        st.session_state.user_info = {}
    if 'current_questions' not in st.session_state:
        st.session_state.current_questions = []

    # Routing
    if not st.session_state.assessment_started:
        show_landing_page()
    elif not st.session_state.submitted:
        show_assessment_page()
    else:
        show_results_page()

if __name__ == "__main__":
    main()
