import streamlit as st

# Set page config first
st.set_page_config(
    page_title="NICE Academy",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Questions Data
QUESTIONS = [
    {
        "id": 1,
        "text": "Which of the following is the single most important practice to reduce the transmission of infectious agents in healthcare settings?",
        "options": [
            "Wearing gloves",
            "Hand hygiene",
            "Wearing a mask",
            "Patient isolation"
        ],
        "correctAnswer": 1,
        "explanation": "Hand hygiene is widely recognized as the single most important measure to prevent the spread of pathogens."
    },
    {
        "id": 2,
        "text": "What type of precautions should be used for a patient with confirmed or suspected tuberculosis?",
        "options": [
            "Contact Precautions",
            "Droplet Precautions",
            "Airborne Precautions",
            "Standard Precautions only"
        ],
        "correctAnswer": 2,
        "explanation": "Tuberculosis is transmitted via airborne particles, so Airborne Precautions (negative pressure room, N95 respirator) are required."
    },
    {
        "id": 3,
        "text": "When should Standard Precautions be applied?",
        "options": [
            "Only for patients with known infections",
            "Only for patients with visible blood",
            "For all patients, regardless of diagnosis or presumed infection status",
            "Only in the emergency department"
        ],
        "correctAnswer": 2,
        "explanation": "Standard Precautions are the minimum infection prevention practices that apply to all patient care, regardless of suspected or confirmed infection status."
    },
    {
        "id": 4,
        "text": "Which of the following organisms is most commonly associated with healthcare-associated infections (HAIs) and is resistant to methicillin?",
        "options": [
            "Escherichia coli",
            "Staphylococcus aureus (MRSA)",
            "Clostridioides difficile",
            "Pseudomonas aeruginosa"
        ],
        "correctAnswer": 1,
        "explanation": "Methicillin-resistant Staphylococcus aureus (MRSA) is a major cause of HAIs."
    },
    {
        "id": 5,
        "text": "What is the recommended hand hygiene method when hands are visibly soiled with blood or body fluids?",
        "options": [
            "Alcohol-based hand rub",
            "Washing with soap and water",
            "Wiping with a paper towel",
            "Rinsing with hot water"
        ],
        "correctAnswer": 1,
        "explanation": "When hands are visibly dirty or soiled with blood or body fluids, they must be washed with soap and water. Alcohol-based rubs are for non-soiled hands."
    },
    {
        "id": 6,
        "text": "Which personal protective equipment (PPE) should be removed first after leaving a patient’s room (or before leaving, depending on protocol)?",
        "options": [
            "Mask",
            "Gown",
            "Gloves",
            "Eye protection"
        ],
        "correctAnswer": 2,
        "explanation": "Gloves are the most contaminated and should usually be removed first to avoid contaminating other PPE or skin."
    },
    {
        "id": 7,
        "text": "For a patient with Clostridioides difficile (C. diff) infection, which hand hygiene method is required?",
        "options": [
            "Alcohol-based hand rub",
            "Soap and water",
            "Surgical scrub",
            "Any of the above"
        ],
        "correctAnswer": 1,
        "explanation": "Alcohol-based hand rubs are not effective against C. diff spores; washing with soap and water is necessary to physically remove the spores."
    },
    {
        "id": 8,
        "text": "What is the correct sequence for donning (putting on) PPE?",
        "options": [
            "Gloves, Gown, Mask, Goggles",
            "Gown, Mask/Respirator, Goggles/Face Shield, Gloves",
            "Mask, Goggles, Gown, Gloves",
            "Gloves, Mask, Goggles, Gown"
        ],
        "correctAnswer": 1,
        "explanation": "The CDC recommends: Gown first, then Mask/Respirator, then Goggles/Face Shield, and finally Gloves."
    },
    {
        "id": 9,
        "text": "Which of the following is a key component of a bundle to prevent Central Line-Associated Bloodstream Infections (CLABSI)?",
        "options": [
            "Changing dressings every 2 hours",
            "Maximal sterile barrier precautions during insertion",
            "Administering prophylactic antibiotics",
            "Using femoral site as first choice"
        ],
        "correctAnswer": 1,
        "explanation": "Maximal sterile barrier precautions (cap, mask, sterile gown, sterile gloves, and large sterile drape) are critical for CLABSI prevention."
    },
    {
        "id": 10,
        "text": "How long should you rub your hands together when using an alcohol-based hand rub?",
        "options": [
            "5 seconds",
            "10 seconds",
            "Until they are dry (approx. 20 seconds)",
            "1 minute"
        ],
        "correctAnswer": 2,
        "explanation": "Rub hands together covering all surfaces until they feel dry, which typically takes around 20 seconds."
    },
    {
        "id": 11,
        "text": "Which of the following is considered a vector-borne transmission?",
        "options": [
            "Transmission via coughing",
            "Transmission via mosquitoes or ticks",
            "Transmission via contaminated water",
            "Transmission via sexual contact"
        ],
        "correctAnswer": 1,
        "explanation": "Vector-borne transmission occurs through insects like mosquitoes, ticks, or fleas."
    },
    {
        "id": 12,
        "text": "What is the primary purpose of a negative pressure room?",
        "options": [
            "To protect the patient from outside contaminants",
            "To prevent airborne pathogens from drifting to other areas",
            "To maintain a constant temperature",
            "To increase oxygen levels"
        ],
        "correctAnswer": 1,
        "explanation": "Negative pressure rooms keep air inside the room from flowing out to hallways, preventing the spread of airborne diseases like TB."
    },
    {
        "id": 13,
        "text": "Which vaccination is most critical for healthcare workers to prevent bloodborne transmission after a needlestick injury?",
        "options": [
            "Influenza",
            "Hepatitis B",
            "Tetanus",
            "Measles"
        ],
        "correctAnswer": 1,
        "explanation": "Hepatitis B vaccination is essential for healthcare workers to protect against infection from bloodborne exposure."
    },
    {
        "id": 14,
        "text": "Spaulding’s classification system categorizes medical devices into critical, semi-critical, and non-critical. A colonoscope is considered:",
        "options": [
            "Critical",
            "Semi-critical",
            "Non-critical",
            "Disposable"
        ],
        "correctAnswer": 1,
        "explanation": "Semi-critical items contact mucous membranes or non-intact skin (e.g., endoscopes) and require high-level disinfection."
    },
    {
        "id": 15,
        "text": "What is the minimum level of disinfection required for non-critical items like blood pressure cuffs?",
        "options": [
            "Sterilization",
            "High-level disinfection",
            "Low-level disinfection",
            "Cleaning with water only"
        ],
        "correctAnswer": 2,
        "explanation": "Non-critical items that touch intact skin require low-level disinfection."
    },
    {
        "id": 16,
        "text": "Which of the following scenarios requires Droplet Precautions?",
        "options": [
            "Measles",
            "Influenza",
            "Varicella (Chickenpox)",
            "Tuberculosis"
        ],
        "correctAnswer": 1,
        "explanation": "Influenza is transmitted by large droplets, requiring Droplet Precautions. Measles, Varicella, and TB require Airborne Precautions."
    },
    {
        "id": 17,
        "text": "What is the correct definition of an iatrogenic infection?",
        "options": [
            "An infection acquired in the community",
            "An infection caused by a diagnostic or therapeutic procedure",
            "An infection present at admission",
            "An infection with no known cause"
        ],
        "correctAnswer": 1,
        "explanation": "Iatrogenic infections are those resulting from medical treatment or procedures."
    },
    {
        "id": 18,
        "text": "In the chain of infection, the \"portal of exit\" refers to:",
        "options": [
            "The way the agent leaves the reservoir",
            "The microorganism causing the disease",
            "The person at risk of infection",
            "The method of transmission"
        ],
        "correctAnswer": 0,
        "explanation": "The portal of exit is the path by which the pathogen leaves its host (reservoir)."
    },
    {
        "id": 19,
        "text": "Which agency is the primary regulatory body for workplace safety, including bloodborne pathogens standards in the US?",
        "options": [
            "CDC",
            "WHO",
            "OSHA",
            "CMS"
        ],
        "correctAnswer": 2,
        "explanation": "OSHA (Occupational Safety and Health Administration) sets and enforces standards for safe and healthful working conditions."
    },
    {
        "id": 20,
        "text": "Safe injection practices include which of the following?",
        "options": [
            "Reusing a needle for the same patient",
            "Using a single-dose vial for multiple patients if the needle is changed",
            "Not using the same syringe for more than one patient",
            "Re-capping needles using two hands"
        ],
        "correctAnswer": 2,
        "explanation": "Never administer medications from the same syringe to more than one patient, even if the needle is changed."
    }
]

def run_native_app():
    st.title("Hospital Infection Control Nurse Competency Assessment")
    st.markdown("A 20-question self-assessment for Hospital Infection Control Nurses to evaluate their knowledge of infection prevention protocols, standard precautions, and disease transmission.")
    
    # Initialize session state
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    # Progress
    progress = (st.session_state.current_question / len(QUESTIONS))
    st.progress(progress)

    # Logic
    if not st.session_state.submitted:
        if st.session_state.current_question < len(QUESTIONS):
            q_index = st.session_state.current_question
            q_data = QUESTIONS[q_index]
            
            st.header(f"Question {q_index + 1} of {len(QUESTIONS)}")
            st.subheader(q_data['text'])
            
            # Use radio button, handle previous selection
            current_answer = st.session_state.answers.get(q_index, None)
            
            # Create a unique key for each question's radio button to avoid state conflicts
            selected_option = st.radio(
                "Choose your answer:",
                q_data['options'],
                index=current_answer if current_answer is not None else None,
                key=f"q_{q_index}"
            )
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                if st.button("Previous", disabled=q_index == 0):
                    st.session_state.current_question -= 1
                    st.rerun()
            
            with col2:
                if st.button("Next" if q_index < len(QUESTIONS) - 1 else "Submit"):
                    # Save answer
                    # Find index of selected option
                    ans_idx = q_data['options'].index(selected_option) if selected_option else None
                    if ans_idx is not None:
                        st.session_state.answers[q_index] = ans_idx
                        
                        if q_index < len(QUESTIONS) - 1:
                            st.session_state.current_question += 1
                            st.rerun()
                        else:
                            st.session_state.submitted = True
                            st.rerun()
                    else:
                        st.warning("Please select an answer.")
        
    else:
        # Results Page
        st.success("Assessment Completed!")
        
        score = 0
        for q_idx, ans_idx in st.session_state.answers.items():
            if QUESTIONS[q_idx]['correctAnswer'] == ans_idx:
                score += 1
        
        percentage = (score / len(QUESTIONS)) * 100
        passed = percentage >= 50
        
        st.metric("Your Score", f"{percentage:.1f}%", f"{score}/{len(QUESTIONS)}")
        
        if passed:
            st.balloons()
            st.header("Congratulations! You Passed.")
            st.write("You have demonstrated good knowledge of infection control protocols.")
        else:
            st.error("You did not pass.")
            st.write("Please review the material and try again.")
            
        st.divider()
        st.header("Review")
        
        for i, q in enumerate(QUESTIONS):
            user_ans = st.session_state.answers.get(i)
            correct = user_ans == q['correctAnswer']
            
            with st.expander(f"Question {i+1}: {q['text']} - {'✅ Correct' if correct else '❌ Incorrect'}"):
                st.write(f"**Your Answer:** {q['options'][user_ans] if user_ans is not None else 'Skipped'}")
                st.write(f"**Correct Answer:** {q['options'][q['correctAnswer']]}")
                st.info(f"**Explanation:** {q['explanation']}")
        
        if st.button("Restart Assessment"):
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.submitted = False
            st.rerun()

def main():
    run_native_app()

if __name__ == "__main__":
    main()
