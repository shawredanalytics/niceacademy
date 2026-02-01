
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
from datetime import datetime
import time
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from questions_data import ASSESSMENT_MODULES, ROLE_ACCESS
from streamlit_autorefresh import st_autorefresh

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
    .timer-box {
        font-size: 1.2rem;
        font-weight: bold;
        color: #d9534f;
        padding: 10px;
        border: 2px solid #d9534f;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

import os
import subprocess

# ... (rest of imports)

# -----------------------------------------------------------------------------
# DATA PERSISTENCE
# -----------------------------------------------------------------------------
DATA_FILE = "data/assessment_results.csv"

def save_result(user_info, score, total_q, passed):
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Create record
    record = {
        "Name": user_info['name'],
        "Email": user_info['email'],
        "Role": user_info['role'],
        "Hospital": user_info['hospital'],
        "Module": user_info['assessment_type'],
        "Date": user_info['date'],
        "Score": score,
        "Total": total_q,
        "Percentage": f"{(score/total_q)*100:.1f}%",
        "Result": "PASS" if passed else "FAIL"
    }
    
    # Save to CSV
    df_new = pd.DataFrame([record])
    
    if os.path.exists(DATA_FILE):
        df_new.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        df_new.to_csv(DATA_FILE, mode='w', header=True, index=False)

def push_data_to_github():
    try:
        # Add the data file
        subprocess.run(["git", "add", DATA_FILE], check=True)
        
        # Commit
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subprocess.run(["git", "commit", "-m", f"Auto-backup assessment data: {timestamp}"], check=True)
        
        # Push
        subprocess.run(["git", "push"], check=True)
        return True, "Data successfully backed up to GitHub!"
    except subprocess.CalledProcessError as e:
        return False, f"Git Error: {str(e)}"
    except Exception as e:
        return False, f"Error: {str(e)}"

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
    if 'q_start_time' in st.session_state:
        del st.session_state.q_start_time

def start_assessment(name, email, role, hospital, assessment_type):
    # Get the questions for the selected assessment type
    all_questions = ASSESSMENT_MODULES.get(assessment_type, ASSESSMENT_MODULES["Infection Control Guidelines"])
    
    # Limit to 10 questions as requested, randomized to ensure variety
    # Use random.sample to get unique questions for this session
    questions = random.sample(all_questions, min(10, len(all_questions)))
    
    st.session_state.user_info = {
        "name": name,
        "email": email,
        "role": role,
        "hospital": hospital,
        "assessment_type": assessment_type,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.current_questions = questions
    st.session_state.assessment_started = True
    st.session_state.q_start_time = time.time() # Start timer for first question
    st.rerun()

def generate_certificate(name, role, module, score_str, date_str):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Border
    c.setStrokeColor(colors.darkblue)
    c.setLineWidth(5)
    c.rect(0.5*inch, 0.5*inch, width-1*inch, height-1*inch)
    
    # Header
    # Draw Logo if exists
    try:
        logo_path = "assets/logo.png"
        # Draw logo centered at top, width=2 inch, preserve aspect ratio
        c.drawImage(logo_path, width/2 - 1*inch, height - 2.5*inch, width=2*inch, height=1*inch, preserveAspectRatio=True, mask='auto')
        header_y_offset = 2.8 * inch # Push text down
    except Exception:
        header_y_offset = 2 * inch # Default if no logo
        c.setFont("Helvetica-Bold", 30)
        c.setFillColor(colors.darkblue)
        c.drawCentredString(width/2, height - 2*inch, "NICE ACADEMY")

    c.setFont("Helvetica", 20)
    c.setFillColor(colors.black)
    c.drawCentredString(width/2, height - header_y_offset - 0.5*inch, "Certificate of Competency")
    
    c.setFont("Helvetica", 14)
    c.drawCentredString(width/2, height - header_y_offset - 1.2*inch, "This certifies that")
    
    # Name
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height - header_y_offset - 1.9*inch, name)
    
    # Details
    c.setFont("Helvetica", 14)
    c.drawCentredString(width/2, height - header_y_offset - 2.7*inch, f"has successfully completed the self-assessment for")
    
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height - header_y_offset - 3.2*inch, module)
    
    c.setFont("Helvetica", 14)
    c.drawCentredString(width/2, height - header_y_offset - 4.2*inch, f"Role: {role}")
    c.drawCentredString(width/2, height - header_y_offset - 4.7*inch, f"Date: {date_str}")
    c.drawCentredString(width/2, height - header_y_offset - 5.2*inch, f"Score: {score_str}")
    
    # Footer (Disclaimer)
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.gray)
    
    disclaimer_y = 1.2 * inch
    line_height = 0.2 * inch
    
    c.drawCentredString(width/2, disclaimer_y, "This is a digital certificate provided to the Healthcare Professional on successful completion of the online competency assessment module.")
    c.drawCentredString(width/2, disclaimer_y - line_height, "It is advised that the competency assessment is conducted by competent individuals in clinical settings")
    c.drawCentredString(width/2, disclaimer_y - 2*line_height, "before privileges are provided to the Healthcare Professionals to conduct relevant duties.")
    
    c.save()
    buffer.seek(0)
    return buffer.getvalue()

# -----------------------------------------------------------------------------
# APP COMPONENTS
# -----------------------------------------------------------------------------

def show_about_page():
    # Logo area
    col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])
    with col_logo_2:
        try:
            st.image("assets/logo.png", use_container_width=True)
        except Exception:
            pass

    st.markdown('<h1 class="main-header">About NICE Academy</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Healthcare Professionals Skill Development Academy
    
    **NICE Academy** is a dedicated healthcare professionals skill development institution committed to elevating clinical expertise, operational excellence, and leadership capabilities across the healthcare sector. By blending evidence-based medical knowledge with practical, real-world training, NICE Academy empowers healthcare practitioners, administrators, and support staff to deliver high-quality, patient-centric care. 
    
    ---
    
    ### Mission 
    To enhance the competency, confidence, and career readiness of healthcare professionals through structured skill development programs that align with industry standards, emerging technologies, and best practices. 
    
    ### Vision 
    To be a leading center of excellence in healthcare education, fostering continuous lifelong learning and contributing to improved health outcomes globally.
    """)

def show_landing_page():
    st.markdown('<h1 class="main-header">NICE Academy</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header" style="text-align: center;">Healthcare Professional Competency Assessment</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("""
        **Welcome!** This portal allows healthcare professionals to assess their knowledge of quality systems and key patient safety protocols.
        
        **Assessment Rules:**
        - **10 Questions** per module.
        - **15 Seconds** time limit per question.
        - **+1** for Correct Answer.
        - **-1** for Wrong Answer (Negative Marking).
        - **0** for Unanswered/Timeout.
        - **Pass Mark:** 75%.
        """)
        
        # Registration Inputs
        name = st.text_input("Full Name", placeholder="e.g. Jane Doe, RN")
        email = st.text_input("Email ID", placeholder="e.g. jane.doe@example.com")
        
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
        
        st.markdown("---")
        
        # Dynamic Assessment Selection based on Role
        available_assessments = []
        if role != "Select your role...":
            available_assessments = ROLE_ACCESS.get(role, ROLE_ACCESS["Other"])
            
            st.markdown(f"**Available Assessments for {role}:**")
            assessment_type = st.selectbox(
                "Select Assessment Module",
                options=available_assessments,
                help="Select the specific competency assessment you wish to undertake."
            )
        else:
            st.warning("Please select a Role to see available assessments.")
            assessment_type = None

        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("Start Assessment", use_container_width=True):
            if name and email and role != "Select your role..." and assessment_type:
                start_assessment(name, email, role, hospital, assessment_type)
            elif not name:
                st.error("Please enter your Full Name.")
            elif not email:
                st.error("Please enter your Email ID.")
            elif role == "Select your role...":
                st.error("Please select a Role.")
            elif not assessment_type:
                st.error("Please select an Assessment Module.")

def show_assessment_page():
    # Auto-refresh every 1 second to update timer and check for timeout
    st_autorefresh(interval=1000, key="assessment_timer")

    questions = st.session_state.current_questions
    q_index = st.session_state.current_question
    q_data = questions[q_index]
    
    # Initialize timer if not set (redundant check if set in start_assessment, but safe)
    if 'q_start_time' not in st.session_state:
        st.session_state.q_start_time = time.time()

    # Check for Timeout
    elapsed = time.time() - st.session_state.q_start_time
    if elapsed > 15:
        # Check if user selected something (auto-submit if selected)
        selected_option = st.session_state.get(f"q_{q_index}")
        
        if selected_option:
            try:
                ans_idx = q_data['options'].index(selected_option)
                st.session_state.answers[q_index] = ans_idx
                st.toast("Time's up! Submitting your selection.", icon="⚠️")
            except ValueError:
                st.session_state.answers[q_index] = "TIMEOUT"
        else:
            st.session_state.answers[q_index] = "TIMEOUT"
            st.toast("Time's up! No answer selected.", icon="⏳")
            
        # Move to next
        if q_index + 1 < len(questions):
            st.session_state.current_question += 1
            st.session_state.q_start_time = time.time()
            st.rerun()
        else:
            st.session_state.submitted = True
            st.session_state.end_time = time.time()
            st.rerun()
        
    # Sidebar Info
    with st.sidebar:
        try:
            st.image("assets/logo.png", use_container_width=True)
        except Exception:
            pass
            
        st.write(f"**Candidate:** {st.session_state.user_info['name']}")
        st.write(f"**Module:** {st.session_state.user_info['assessment_type']}")
        
        st.markdown("---")
        
        if st.button("Quit Assessment"):
            reset_app()
            st.rerun()

    # Main Question Area
    
    # NEW: Progress and Timer Header
    # Calculate remaining time
    elapsed = time.time() - st.session_state.q_start_time
    remaining_time = max(0, 15 - int(elapsed))

    col_header1, col_header2 = st.columns([3, 1])
    
    with col_header1:
        st.write(f"**Question {q_index + 1} of {len(questions)}**")
        progress = (q_index + 1) / len(questions)
        st.progress(progress)
        
    with col_header2:
        # Visual Countdown Timer using HTML/JS
        # We use a key to force re-render of the component on every question change or rerun
        timer_html = f"""
        <div id="timer_div" style="
            font-size: 1.2rem; 
            font-weight: bold; 
            color: #333; 
            text-align: center; 
            border: 2px solid #ddd; 
            border-radius: 5px; 
            padding: 5px;
            background-color: #fff;">
            ⏱️ <span id="time_left">{remaining_time}</span>s
        </div>
        <script>
            var timeleft = {remaining_time};
            var timer = setInterval(function(){{
                if(timeleft <= 0){{
                    clearInterval(timer);
                    document.getElementById("time_left").innerHTML = "0";
                    document.getElementById("timer_div").style.color = "#d9534f"; // Red
                    document.getElementById("timer_div").style.borderColor = "#d9534f";
                }} else {{
                    document.getElementById("time_left").innerHTML = timeleft;
                    if(timeleft <= 5) {{
                        document.getElementById("timer_div").style.color = "#d9534f"; // Red warning
                        document.getElementById("timer_div").style.borderColor = "#d9534f";
                    }}
                }}
                timeleft -= 1;
            }}, 1000);
        </script>
        """
        components.html(timer_html, height=50)
        
        # Time Consumption Bar (Visual Ticking Clock)
        time_pct = max(0.0, min(1.0, (15 - elapsed) / 15))
        st.progress(time_pct)

    st.markdown("---")
    
    st.markdown(f"**Category:** {q_data['category']}")
    
    st.markdown(f"""
    <div class="question-card">
        <h4>{q_data['text']}</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Options
    # Use a unique key per question to reset selection
    selected_option = st.radio(
        "Select your answer:",
        q_data['options'],
        key=f"q_{q_index}",
        index=None
    )
    
    st.markdown("---")
    
    # Navigation
    col1, col2 = st.columns([1, 1])
    
    # Disable Previous Button for timed assessment integrity
    with col1:
        st.button("⬅️ Previous", disabled=True, use_container_width=True, help="Navigation is forward-only for timed assessments.")
            
    with col2:
        is_last = q_index == len(questions) - 1
        btn_text = "Submit Assessment 🏁" if is_last else "Next ➡️"
        
        if st.button(btn_text, use_container_width=True):
            # Check Timer
            elapsed_time = time.time() - st.session_state.q_start_time
            
            if elapsed_time > 15:
                # Timeout case
                st.session_state.answers[q_index] = "TIMEOUT"
                st.toast(f"Question {q_index+1} timed out! Recorded as unanswered.", icon="⏳")
            else:
                # Normal submission
                if selected_option:
                    ans_idx = q_data['options'].index(selected_option)
                    st.session_state.answers[q_index] = ans_idx
                else:
                    # User clicked Next without selecting (treat as unanswered/skip)
                    st.session_state.answers[q_index] = None
            
            # Move to next
            if not is_last:
                st.session_state.current_question += 1
                st.session_state.q_start_time = time.time() # Reset timer for next question
                st.rerun()
            else:
                st.session_state.submitted = True
                st.rerun()

def show_results_page():
    questions = st.session_state.current_questions
    
    # Logo area
    col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])
    with col_logo_2:
        try:
            st.image("assets/logo.png", use_container_width=True)
        except Exception:
            pass

    st.markdown('<h1 class="main-header">Assessment Report</h1>', unsafe_allow_html=True)
    
    # Calculate Score
    total_q = len(questions)
    score = 0
    correct_count = 0
    wrong_count = 0
    unanswered_count = 0
    
    for i, q in enumerate(questions):
        user_ans = st.session_state.answers.get(i)
        
        if user_ans == "TIMEOUT" or user_ans is None:
            unanswered_count += 1
            # 0 marks for unanswered
        elif user_ans == q['correctAnswer']:
            score += 1
            correct_count += 1
        else:
            score -= 1 # Negative marking
            wrong_count += 1

    # Max possible score is total_q (assuming all correct = +1 each)
    # Pass mark is 75%
    percentage = (score / total_q) * 100
    passed = percentage >= 75
    
    # Save Results
    if not st.session_state.get('results_saved', False):
        save_result(st.session_state.user_info, score, total_q, passed)
        st.session_state.results_saved = True
    
    # Summary Card
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric("Final Score", f"{percentage:.1f}%", f"{score}/{total_q} Points")
        if passed:
            st.success("Result: COMPETENT ✅")
            st.balloons()
        else:
            st.error("Result: NEEDS IMPROVEMENT ⚠️")
            
    with col2:
        st.write(f"**Name:** {st.session_state.user_info['name']}")
        st.write(f"**Role:** {st.session_state.user_info['role']}")
        st.write(f"**Module:** {st.session_state.user_info['assessment_type']}")
        st.write(f"**Date:** {st.session_state.user_info['date']}")
        
        st.markdown(f"""
        - Correct Answers: **{correct_count}** (+{correct_count})
        - Wrong Answers: **{wrong_count}** (-{wrong_count})
        - Unanswered/Timeout: **{unanswered_count}** (0)
        """)

    st.markdown("---")
    
    # Certificate Download
    if passed:
        st.subheader("🎉 Congratulations!")
        st.write("You have successfully completed the competency assessment.")
        
        cert_data = generate_certificate(
            st.session_state.user_info['name'],
            st.session_state.user_info['role'],
            st.session_state.user_info['assessment_type'],
            f"{percentage:.1f}%",
            st.session_state.user_info['date']
        )
        
        st.download_button(
            label="📜 Download Certificate",
            data=cert_data,
            file_name="Competency_Certificate.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.warning("You did not meet the required pass mark of 75%. Please review the guidelines and try again.")

    # Detailed Review
    st.markdown("---")
    with st.expander("View Detailed Answer Key"):
        for i, q in enumerate(questions):
            user_ans = st.session_state.answers.get(i)
            
            if user_ans == "TIMEOUT" or user_ans is None:
                st.markdown(f"**{i+1}. {q['text']}** ⏳ *Unanswered/Timeout*")
                st.markdown(f"Correct Answer: **{q['options'][q['correctAnswer']]}**")
                st.info(f"💡 {q['explanation']}")
            else:
                correct = user_ans == q['correctAnswer']
                icon = "✅" if correct else "❌"
                st.markdown(f"**{i+1}. {q['text']}** {icon}")
                if not correct:
                    st.markdown(f"Your Answer: *{q['options'][user_ans]}*")
                    st.markdown(f"Correct Answer: **{q['options'][q['correctAnswer']]}**")
                    st.info(f"💡 {q['explanation']}")
            st.markdown("---")

    # Restart
    if st.button("Start New Assessment", use_container_width=True):
        reset_app()
        st.rerun()

def show_admin_page():
    st.markdown('<h1 class="main-header">Admin Dashboard</h1>', unsafe_allow_html=True)
    
    # Simple Authentication
    password = st.sidebar.text_input("Admin Password", type="password")
    
    if password == "admin123": # TODO: Use safer auth in production
        st.success("Authenticated")
        
        st.subheader("Assessment Results")
        
        if os.path.exists(DATA_FILE):
            df = pd.read_csv(DATA_FILE)
            st.dataframe(df, use_container_width=True)
            
            # Download Button
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download Data (CSV)",
                csv,
                "assessment_results.csv",
                "text/csv",
                key='download-csv'
            )
            
            st.markdown("---")
            st.subheader("Data Backup")
            st.write("Push the latest results to the GitHub repository.")
            
            if st.button("☁️ Backup Data to GitHub"):
                with st.spinner("Backing up data..."):
                    success, msg = push_data_to_github()
                    if success:
                        st.success(msg)
                    else:
                        st.error(msg)
        else:
            st.info("No assessment data available yet.")
            
    elif password:
        st.error("Invalid Password")
    else:
        st.info("Please enter the admin password to view data.")

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
        # Sidebar Navigation for Home/About
        with st.sidebar:
            try:
                st.image("assets/logo.png", use_container_width=True)
            except Exception:
                pass
            
            st.markdown("### Navigation")
            page = st.radio("Go to", ["Home", "About Us", "Admin Login"])
            
            st.markdown("---")
            st.info("Select 'Home' to start an assessment.")

        if page == "Home":
            show_landing_page()
        elif page == "About Us":
            show_about_page()
        elif page == "Admin Login":
            show_admin_page()
            
    elif not st.session_state.submitted:
        show_assessment_page()
    else:
        show_results_page()

if __name__ == "__main__":
    main()
