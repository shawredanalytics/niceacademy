import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

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
# DATA: QUESTIONS WITH CATEGORIES
# -----------------------------------------------------------------------------
QUESTIONS = [
    {
        "id": 1,
        "category": "Hand Hygiene & PPE",
        "text": "Which of the following is the single most important practice to reduce the transmission of infectious agents in healthcare settings?",
        "options": ["Wearing gloves", "Hand hygiene", "Wearing a mask", "Patient isolation"],
        "correctAnswer": 1,
        "explanation": "Hand hygiene is widely recognized as the single most important measure to prevent the spread of pathogens."
    },
    {
        "id": 2,
        "category": "Transmission-Based Precautions",
        "text": "What type of precautions should be used for a patient with confirmed or suspected tuberculosis?",
        "options": ["Contact Precautions", "Droplet Precautions", "Airborne Precautions", "Standard Precautions only"],
        "correctAnswer": 2,
        "explanation": "Tuberculosis is transmitted via airborne particles, so Airborne Precautions (negative pressure room, N95 respirator) are required."
    },
    {
        "id": 3,
        "category": "Standard Precautions",
        "text": "When should Standard Precautions be applied?",
        "options": ["Only for patients with known infections", "Only for patients with visible blood", "For all patients, regardless of diagnosis or presumed infection status", "Only in the emergency department"],
        "correctAnswer": 2,
        "explanation": "Standard Precautions are the minimum infection prevention practices that apply to all patient care, regardless of suspected or confirmed infection status."
    },
    {
        "id": 4,
        "category": "Specific Pathogens",
        "text": "Which of the following organisms is most commonly associated with healthcare-associated infections (HAIs) and is resistant to methicillin?",
        "options": ["Escherichia coli", "Staphylococcus aureus (MRSA)", "Clostridioides difficile", "Pseudomonas aeruginosa"],
        "correctAnswer": 1,
        "explanation": "Methicillin-resistant Staphylococcus aureus (MRSA) is a major cause of HAIs."
    },
    {
        "id": 5,
        "category": "Hand Hygiene & PPE",
        "text": "What is the recommended hand hygiene method when hands are visibly soiled with blood or body fluids?",
        "options": ["Alcohol-based hand rub", "Washing with soap and water", "Wiping with a paper towel", "Rinsing with hot water"],
        "correctAnswer": 1,
        "explanation": "When hands are visibly dirty or soiled with blood or body fluids, they must be washed with soap and water. Alcohol-based rubs are for non-soiled hands."
    },
    {
        "id": 6,
        "category": "Hand Hygiene & PPE",
        "text": "Which personal protective equipment (PPE) should be removed first after leaving a patient’s room (or before leaving, depending on protocol)?",
        "options": ["Mask", "Gown", "Gloves", "Eye protection"],
        "correctAnswer": 2,
        "explanation": "Gloves are the most contaminated and should usually be removed first to avoid contaminating other PPE or skin."
    },
    {
        "id": 7,
        "category": "Specific Pathogens",
        "text": "For a patient with Clostridioides difficile (C. diff) infection, which hand hygiene method is required?",
        "options": ["Alcohol-based hand rub", "Soap and water", "Surgical scrub", "Any of the above"],
        "correctAnswer": 1,
        "explanation": "Alcohol-based hand rubs are not effective against C. diff spores; washing with soap and water is necessary to physically remove the spores."
    },
    {
        "id": 8,
        "category": "Hand Hygiene & PPE",
        "text": "What is the correct sequence for donning (putting on) PPE?",
        "options": ["Gloves, Gown, Mask, Goggles", "Gown, Mask/Respirator, Goggles/Face Shield, Gloves", "Mask, Goggles, Gown, Gloves", "Gloves, Mask, Goggles, Gown"],
        "correctAnswer": 1,
        "explanation": "The CDC recommends: Gown first, then Mask/Respirator, then Goggles/Face Shield, and finally Gloves."
    },
    {
        "id": 9,
        "category": "Device-Associated Infections",
        "text": "Which of the following is a key component of a bundle to prevent Central Line-Associated Bloodstream Infections (CLABSI)?",
        "options": ["Changing dressings every 2 hours", "Maximal sterile barrier precautions during insertion", "Administering prophylactic antibiotics", "Using femoral site as first choice"],
        "correctAnswer": 1,
        "explanation": "Maximal sterile barrier precautions (cap, mask, sterile gown, sterile gloves, and large sterile drape) are critical for CLABSI prevention."
    },
    {
        "id": 10,
        "category": "Hand Hygiene & PPE",
        "text": "How long should you rub your hands together when using an alcohol-based hand rub?",
        "options": ["5 seconds", "10 seconds", "Until they are dry (approx. 20 seconds)", "1 minute"],
        "correctAnswer": 2,
        "explanation": "Rub hands together covering all surfaces until they feel dry, which typically takes around 20 seconds."
    },
    {
        "id": 11,
        "category": "Transmission Modes",
        "text": "Which of the following is considered a vector-borne transmission?",
        "options": ["Transmission via coughing", "Transmission via mosquitoes or ticks", "Transmission via contaminated water", "Transmission via sexual contact"],
        "correctAnswer": 1,
        "explanation": "Vector-borne transmission occurs through insects like mosquitoes, ticks, or fleas."
    },
    {
        "id": 12,
        "category": "Engineering Controls",
        "text": "What is the primary purpose of a negative pressure room?",
        "options": ["To protect the patient from outside contaminants", "To prevent airborne pathogens from drifting to other areas", "To maintain a constant temperature", "To increase oxygen levels"],
        "correctAnswer": 1,
        "explanation": "Negative pressure rooms keep air inside the room from flowing out to hallways, preventing the spread of airborne diseases like TB."
    },
    {
        "id": 13,
        "category": "Occupational Health",
        "text": "Which vaccination is most critical for healthcare workers to prevent bloodborne transmission after a needlestick injury?",
        "options": ["Influenza", "Hepatitis B", "Tetanus", "Measles"],
        "correctAnswer": 1,
        "explanation": "Hepatitis B vaccination is essential for healthcare workers to protect against infection from bloodborne exposure."
    },
    {
        "id": 14,
        "category": "Disinfection & Sterilization",
        "text": "Spaulding’s classification system categorizes medical devices into critical, semi-critical, and non-critical. A colonoscope is considered:",
        "options": ["Critical", "Semi-critical", "Non-critical", "Disposable"],
        "correctAnswer": 1,
        "explanation": "Semi-critical items contact mucous membranes or non-intact skin (e.g., endoscopes) and require high-level disinfection."
    },
    {
        "id": 15,
        "category": "Disinfection & Sterilization",
        "text": "What is the minimum level of disinfection required for non-critical items like blood pressure cuffs?",
        "options": ["Sterilization", "High-level disinfection", "Low-level disinfection", "Cleaning with water only"],
        "correctAnswer": 2,
        "explanation": "Non-critical items that touch intact skin require low-level disinfection."
    },
    {
        "id": 16,
        "category": "Transmission-Based Precautions",
        "text": "Which of the following scenarios requires Droplet Precautions?",
        "options": ["Measles", "Influenza", "Varicella (Chickenpox)", "Tuberculosis"],
        "correctAnswer": 1,
        "explanation": "Influenza is transmitted by large droplets, requiring Droplet Precautions. Measles, Varicella, and TB require Airborne Precautions."
    },
    {
        "id": 17,
        "category": "Terminology",
        "text": "What is the correct definition of an iatrogenic infection?",
        "options": ["An infection acquired in the community", "An infection caused by a diagnostic or therapeutic procedure", "An infection present at admission", "An infection with no known cause"],
        "correctAnswer": 1,
        "explanation": "Iatrogenic infections are those resulting from medical treatment or procedures."
    },
    {
        "id": 18,
        "category": "Chain of Infection",
        "text": "In the chain of infection, the \"portal of exit\" refers to:",
        "options": ["The way the agent leaves the reservoir", "The microorganism causing the disease", "The person at risk of infection", "The method of transmission"],
        "correctAnswer": 0,
        "explanation": "The portal of exit is the path by which the pathogen leaves its host (reservoir)."
    },
    {
        "id": 19,
        "category": "Regulatory",
        "text": "Which agency is the primary regulatory body for workplace safety, including bloodborne pathogens standards in the US?",
        "options": ["CDC", "WHO", "OSHA", "CMS"],
        "correctAnswer": 2,
        "explanation": "OSHA (Occupational Safety and Health Administration) sets and enforces standards for safe and healthful working conditions."
    },
    {
        "id": 20,
        "category": "Safe Injection Practices",
        "text": "Safe injection practices include which of the following?",
        "options": ["Reusing a needle for the same patient", "Using a single-dose vial for multiple patients if the needle is changed", "Not using the same syringe for more than one patient", "Re-capping needles using two hands"],
        "correctAnswer": 2,
        "explanation": "Never administer medications from the same syringe to more than one patient, even if the needle is changed."
    }
]

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def reset_app():
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.assessment_started = False
    st.session_state.user_info = {}

def start_assessment(name, role, hospital):
    st.session_state.user_info = {
        "name": name,
        "role": role,
        "hospital": hospital,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
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
            role = st.selectbox("Role / Designation", [
                "Select your role...",
                "Infection Control Nurse (ICN)",
                "Staff Nurse",
                "Physician / Doctor",
                "Nursing Assistant",
                "Healthcare Administrator",
                "Student",
                "Other"
            ])
            hospital = st.text_input("Hospital / Organization (Optional)", placeholder="e.g. General Hospital")
            
            submitted = st.form_submit_button("Start Assessment", use_container_width=True)
            
            if submitted:
                if name and role != "Select your role...":
                    start_assessment(name, role, hospital)
                else:
                    st.error("Please provide your Name and select a Role to proceed.")

def show_assessment_page():
    # Sidebar Info
    with st.sidebar:
        st.write(f"**Candidate:** {st.session_state.user_info['name']}")
        st.write(f"**Role:** {st.session_state.user_info['role']}")
        st.progress((st.session_state.current_question / len(QUESTIONS)))
        st.caption(f"Question {st.session_state.current_question + 1} of {len(QUESTIONS)}")
        if st.button("Quit Assessment"):
            reset_app()
            st.rerun()

    # Question Display
    q_index = st.session_state.current_question
    q_data = QUESTIONS[q_index]
    
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
        is_last = q_index == len(QUESTIONS) - 1
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
    st.markdown('<h1 class="main-header">Assessment Report</h1>', unsafe_allow_html=True)
    
    # Calculate Score
    total_q = len(QUESTIONS)
    correct_count = 0
    category_scores = {}
    
    for i, q in enumerate(QUESTIONS):
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
    
    df_cat = pd.DataFrame(cat_data)
    fig = px.bar(df_cat, x="Score (%)", y="Category", orientation='h', 
                 title="Performance Breakdown", 
                 range_x=[0, 100], 
                 color="Score (%)",
                 color_continuous_scale=["red", "yellow", "green"])
    st.plotly_chart(fig, use_container_width=True)

    # Detailed Review
    with st.expander("View Detailed Answer Key"):
        for i, q in enumerate(QUESTIONS):
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

    # Routing
    if not st.session_state.assessment_started:
        show_landing_page()
    elif not st.session_state.submitted:
        show_assessment_page()
    else:
        show_results_page()

if __name__ == "__main__":
    main()
