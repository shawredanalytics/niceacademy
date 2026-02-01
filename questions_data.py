
# -----------------------------------------------------------------------------
# DATA: QUESTIONS WITH CATEGORIES
# -----------------------------------------------------------------------------

# 1. INFECTION CONTROL GUIDELINES (Existing ICN Set)
INFECTION_CONTROL_QUESTIONS = [
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

# 2. RADIATION SAFETY GUIDELINES (For Radiation Workers/Technicians)
RADIATION_SAFETY_QUESTIONS = [
    {
        "id": 1,
        "category": "Principles of Radiation Protection",
        "text": "What does the ALARA principle stand for in radiation safety?",
        "options": ["As Low As Reasonably Achievable", "Always Limit All Radiation Exposure", "As Low As Regulation Allows", "Avoid Long And Repetitive Access"],
        "correctAnswer": 0,
        "explanation": "ALARA means making every reasonable effort to maintain exposures to ionizing radiation as far below the dose limits as practical."
    },
    {
        "id": 2,
        "category": "Protection Measures",
        "text": "What are the three cardinal principles of radiation protection?",
        "options": ["Time, Distance, and Shielding", "Monitoring, Measuring, and Managing", "Gloves, Gowns, and Masks", "Detection, Diagnosis, and Dosage"],
        "correctAnswer": 0,
        "explanation": "Minimizing time, maximizing distance, and using appropriate shielding are the three fundamental principles."
    },
    {
        "id": 3,
        "category": "Monitoring",
        "text": "Where should a personal radiation dosimeter (badge) generally be worn?",
        "options": ["In a pocket", "On the collar or chest area", "On the belt", "Inside a lead apron"],
        "correctAnswer": 1,
        "explanation": "Dosimeters are typically worn on the front of the body between the neck and waist to estimate the dose to the whole body."
    },
    {
        "id": 4,
        "category": "Shielding",
        "text": "Which material is most commonly used for shielding against X-rays and gamma rays in healthcare settings?",
        "options": ["Aluminum", "Plastic", "Lead", "Wood"],
        "correctAnswer": 2,
        "explanation": "Lead is highly effective at attenuating X-rays and gamma rays due to its high density and atomic number."
    },
    {
        "id": 5,
        "category": "Safety Protocols",
        "text": "What is the primary safety concern regarding pregnant staff members working with radiation?",
        "options": ["Increased risk of infection", "Fetal radiation exposure", "Ergonomic strain", "Chemical exposure"],
        "correctAnswer": 1,
        "explanation": "The fetus is particularly sensitive to ionizing radiation, so strict dose limits and monitoring are required for pregnant workers."
    }
]

# 3. MEDICATION SAFETY GUIDELINES (For Doctors)
MEDICATION_SAFETY_QUESTIONS = [
    {
        "id": 1,
        "category": "Prescribing",
        "text": "Which of the following is a 'High-Alert' medication that carries a heightened risk of causing significant patient harm if used in error?",
        "options": ["Multivitamins", "Insulin", "Normal Saline", "Amoxicillin"],
        "correctAnswer": 1,
        "explanation": "Insulin is classified as a high-alert medication because dosing errors can lead to fatal hypoglycemia."
    },
    {
        "id": 2,
        "category": "Administration",
        "text": "What are the 'Five Rights' of medication administration?",
        "options": ["Right Patient, Drug, Dose, Route, Time", "Right Doctor, Nurse, Pharmacist, Patient, Drug", "Right Hospital, Ward, Bed, Patient, Drug", "Right Price, Brand, Generic, Dose, Route"],
        "correctAnswer": 0,
        "explanation": "The standard 'Five Rights' are Right Patient, Right Drug, Right Dose, Right Route, and Right Time."
    },
    {
        "id": 3,
        "category": "Reconciliation",
        "text": "When should medication reconciliation occur?",
        "options": ["Only at discharge", "Only upon admission", "At every transition of care (admission, transfer, discharge)", "Only when the patient asks"],
        "correctAnswer": 2,
        "explanation": "Medication reconciliation should be done at all points of transition to prevent errors like omissions or duplications."
    },
    {
        "id": 4,
        "category": "Safety Systems",
        "text": "What is the primary purpose of CPOE (Computerized Physician Order Entry)?",
        "options": ["To speed up billing", "To reduce errors associated with handwriting and transcription", "To replace pharmacists", "To allow remote access only"],
        "correctAnswer": 1,
        "explanation": "CPOE significantly reduces medication errors caused by illegible handwriting and transcription mistakes."
    },
    {
        "id": 5,
        "category": "Error Prevention",
        "text": "How should 'Look-Alike, Sound-Alike' (LASA) medications be managed?",
        "options": ["Store them alphabetically side-by-side", "Use 'Tall Man' lettering and physical separation", "Rely on memory", "Remove them from the formulary"],
        "correctAnswer": 1,
        "explanation": "Using 'Tall Man' lettering (e.g., DOPamine vs DOBUTamine) and separating them in storage helps prevent selection errors."
    }
]

# 4. MEDICAL RECORDS DOCUMENTATION (For Doctors)
MEDICAL_RECORDS_QUESTIONS = [
    {
        "id": 1,
        "category": "Documentation Standards",
        "text": "Which format is commonly recommended for structuring clinical progress notes?",
        "options": ["NARRATIVE", "SOAP (Subjective, Objective, Assessment, Plan)", "RANDOM", "CHRONOLOGICAL only"],
        "correctAnswer": 1,
        "explanation": "The SOAP format is a widely accepted standard for organizing patient data in a logical and consistent manner."
    },
    {
        "id": 2,
        "category": "Timeliness",
        "text": "Ideally, when should a procedure note be documented in the medical record?",
        "options": ["Within 24 hours", "Immediately after the procedure", "At the end of the week", "Before discharge"],
        "correctAnswer": 1,
        "explanation": "Documentation should occur as soon as possible after the event to ensure accuracy and continuity of care."
    },
    {
        "id": 3,
        "category": "Error Correction",
        "text": "What is the correct way to correct an error in a written medical record?",
        "options": ["Use white-out/correction fluid", "Scribble it out completely so it can't be read", "Draw a single line through the error, date, and initial it", "Tear out the page"],
        "correctAnswer": 2,
        "explanation": "The original entry must remain visible for legal and audit purposes. A single strike-through with initials and date is the standard."
    },
    {
        "id": 4,
        "category": "Legal",
        "text": "In a malpractice lawsuit, if a care event is not documented in the medical record, the legal assumption is usually:",
        "options": ["It happened but wasn't written down", "The patient is lying", "If it wasn't documented, it wasn't done", "The nurse is responsible"],
        "correctAnswer": 2,
        "explanation": "The legal adage is 'If it wasn't documented, it wasn't done.' Documentation is the proof of care."
    },
    {
        "id": 5,
        "category": "Privacy",
        "text": "Who has the right to access a patient's medical record?",
        "options": ["Any hospital staff member", "Only staff directly involved in the patient's care", "The patient's family members at any time", "Insurance companies without consent"],
        "correctAnswer": 1,
        "explanation": "Access is restricted to those with a 'need to know' for clinical care, payment, or operations, compliant with privacy laws."
    }
]

# 5. PATIENT SAFETY GUIDELINES (For Nurses, Doctors, Technical Staff)
PATIENT_SAFETY_QUESTIONS = [
    {
        "id": 1,
        "category": "Patient Identification",
        "text": "How many patient identifiers are required before administering medication or performing a procedure?",
        "options": ["One (Room number)", "Two (e.g., Name and Date of Birth)", "Three (Name, DOB, Address)", "None if you know the patient"],
        "correctAnswer": 1,
        "explanation": "Joint Commission and other safety bodies mandate using at least two patient identifiers to prevent wrong-patient errors."
    },
    {
        "id": 2,
        "category": "Communication",
        "text": "What does the SBAR communication tool stand for?",
        "options": ["Subject, Body, Action, Response", "Situation, Background, Assessment, Recommendation", "Stop, Breathe, Ask, React", "Safety, Behavior, Attitude, Review"],
        "correctAnswer": 1,
        "explanation": "SBAR is a standardized framework for communicating critical information requiring immediate attention and action."
    },
    {
        "id": 3,
        "category": "Surgical Safety",
        "text": "What is a 'Time Out' in a surgical or procedural setting?",
        "options": ["A break for the staff", "A final verification of correct patient, procedure, and site before starting", "The time anesthesia ends", "A disciplinary action"],
        "correctAnswer": 1,
        "explanation": "A Time Out is the final pause before an incision or procedure to verify all critical details and prevent wrong-site surgery."
    },
    {
        "id": 4,
        "category": "Fall Prevention",
        "text": "Which of the following is a universal fall precaution?",
        "options": ["Restraining all patients", "Keeping the bed in the lowest position with wheels locked", "Keeping the room completely dark", "Removing the call bell"],
        "correctAnswer": 1,
        "explanation": "Keeping the bed low and locked is a fundamental safety measure to reduce the risk and impact of falls."
    },
    {
        "id": 5,
        "category": "Reporting",
        "text": "Why is it important to report 'near misses' (events that could have caused harm but didn't)?",
        "options": ["To punish the staff involved", "To increase paperwork", "To identify system weaknesses and prevent future actual harm", "It is not important"],
        "correctAnswer": 2,
        "explanation": "Reporting near misses provides valuable data to fix system issues before they result in actual patient harm."
    }
]

# 6. PATIENT CONFIDENTIALITY (For Administration Staff)
PATIENT_CONFIDENTIALITY_QUESTIONS = [
    {
        "id": 1,
        "category": "Data Privacy",
        "text": "What is the primary rule regarding discussing patient information in public areas (e.g., elevators, cafeteria)?",
        "options": ["It is allowed if you whisper", "It is strictly prohibited", "It is allowed if you don't use the last name", "It is okay if no one is listening"],
        "correctAnswer": 1,
        "explanation": "Discussing PHI (Protected Health Information) in public areas risks incidental disclosure and is a violation of privacy policies."
    },
    {
        "id": 2,
        "category": "Access Rights",
        "text": "Are you allowed to access the medical records of a VIP patient or a celebrity just out of curiosity?",
        "options": ["Yes, if you work at the hospital", "No, never", "Yes, if you don't tell anyone", "Only if you are a fan"],
        "correctAnswer": 1,
        "explanation": "Accessing records without a legitimate business or clinical reason ('snooping') is a serious privacy violation and a firable offense."
    },
    {
        "id": 3,
        "category": "Security",
        "text": "What should you do if you need to leave your computer workstation for a few minutes?",
        "options": ["Leave it logged in for convenience", "Turn off the monitor", "Lock the screen or log out", "Ask a colleague to watch it"],
        "correctAnswer": 2,
        "explanation": "Locking the screen prevents unauthorized access to sensitive information while you are away."
    },
    {
        "id": 4,
        "category": "Family Access",
        "text": "Can you access your own family member's medical record using your staff login credentials?",
        "options": ["Yes, because I am family", "No, you must go through standard release of information channels", "Yes, if they give verbal permission", "Only in emergencies"],
        "correctAnswer": 1,
        "explanation": "Using staff privileges to access family records bypasses the official request process and is considered a conflict of interest/privacy breach."
    },
    {
        "id": 5,
        "category": "Disposal",
        "text": "How should paper documents containing patient information be disposed of?",
        "options": ["In the regular trash bin", "In the recycle bin", "In a designated shredding bin", "Taken home to burn"],
        "correctAnswer": 2,
        "explanation": "Documents with PHI must be shredded or placed in secure shredding bins to prevent data recovery."
    }
]

# -----------------------------------------------------------------------------
# MAPPINGS
# -----------------------------------------------------------------------------

# Map Module Names to Question Sets
ASSESSMENT_MODULES = {
    "Infection Control Guidelines": INFECTION_CONTROL_QUESTIONS,
    "Radiation Safety Guidelines": RADIATION_SAFETY_QUESTIONS,
    "Medication Safety Guidelines": MEDICATION_SAFETY_QUESTIONS,
    "Medical Records Documentation": MEDICAL_RECORDS_QUESTIONS,
    "Patient Safety Guidelines": PATIENT_SAFETY_QUESTIONS,
    "Patient Confidentiality": PATIENT_CONFIDENTIALITY_QUESTIONS
}

# Map Roles to Eligible Assessment Modules
ROLE_ACCESS = {
    "Infection Control Nurse (ICN)": [
        "Infection Control Guidelines",
        "Patient Safety Guidelines"
    ],
    "Staff Nurse": [
        "Infection Control Guidelines",
        "Patient Safety Guidelines"
    ],
    "Physician / Doctor": [
        "Medication Safety Guidelines",
        "Medical Records Documentation",
        "Patient Safety Guidelines"
    ],
    "Technician / Allied Health": [
        "Radiation Safety Guidelines",
        "Patient Safety Guidelines"
    ],
    "Nursing Assistant / Support Staff": [
        "Infection Control Guidelines",
        "Patient Safety Guidelines"
    ],
    "Administrative Personnel": [
        "Patient Confidentiality"
    ],
    "Student": [
        "Infection Control Guidelines",
        "Patient Safety Guidelines"
    ],
    "Other": [
        "Infection Control Guidelines",
        "Patient Safety Guidelines",
        "Patient Confidentiality"
    ]
}

# Legacy Export (for backward compatibility if needed, though we will update app logic)
# We can effectively ignore ASSESSMENTS dictionary now or make it a flat map of all available
ASSESSMENTS = ASSESSMENT_MODULES
