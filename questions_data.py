
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
    },
    {
        "id": 6,
        "category": "Waste Management",
        "text": "How should radioactive waste be disposed of?",
        "options": ["In the regular trash", "Down the sink", "In designated, labeled radioactive waste containers", "In biohazard bags"],
        "correctAnswer": 2,
        "explanation": "Radioactive waste requires segregation in specific shielded containers to prevent environmental contamination."
    },
    {
        "id": 7,
        "category": "Physics",
        "text": "According to the Inverse Square Law, if you double your distance from a radiation source, your exposure is reduced to:",
        "options": ["One half (1/2)", "One quarter (1/4)", "One eighth (1/8)", "Zero"],
        "correctAnswer": 1,
        "explanation": "Intensity is inversely proportional to the square of the distance. Doubling distance reduces intensity by factor of 4."
    },
    {
        "id": 8,
        "category": "Signage",
        "text": "What symbol typically identifies areas where radioactive materials are used?",
        "options": ["Skull and crossbones", "Biohazard symbol", "Trefoil (Radiation symbol)", "High voltage sign"],
        "correctAnswer": 2,
        "explanation": "The magenta or black trefoil on a yellow background is the universal radiation warning symbol."
    },
    {
        "id": 9,
        "category": "Limits",
        "text": "What is the annual occupational dose limit for the whole body for radiation workers?",
        "options": ["50 mSv (5 rem)", "5 mSv (0.5 rem)", "1 mSv (0.1 rem)", "500 mSv (50 rem)"],
        "correctAnswer": 0,
        "explanation": "The standard annual limit for occupational exposure is typically 50 mSv (5 rem)."
    },
    {
        "id": 10,
        "category": "Emergency",
        "text": "What is the first step if a radioactive liquid is spilled?",
        "options": ["Clean it up with paper towels immediately", "Evacuate the area and notify the Radiation Safety Officer", "Pour water on it", "Ignore it if it's small"],
        "correctAnswer": 1,
        "explanation": "Immediate safety priority is to secure the area and notify experts (RSO) to manage decontamination."
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
    },
    {
        "id": 6,
        "category": "Verbal Orders",
        "text": "What is the critical step when receiving a verbal medication order?",
        "options": ["Write it down later", "Read back the order to the prescriber for verification", "Assume you heard it correctly", "Ask a colleague to listen"],
        "correctAnswer": 1,
        "explanation": "Reading back the order confirms accurate transmission and transcription of verbal instructions."
    },
    {
        "id": 7,
        "category": "Allergies",
        "text": "Before prescribing or administering a new medication, what must always be checked?",
        "options": ["The cost of the drug", "The patient's allergy status", "The expiration date of the patent", "The color of the pill"],
        "correctAnswer": 1,
        "explanation": "Verifying allergies is a critical safety step to prevent life-threatening anaphylactic reactions."
    },
    {
        "id": 8,
        "category": "Controlled Substances",
        "text": "How should narcotics and controlled substances typically be stored?",
        "options": ["On the counter for easy access", "In a double-locked cabinet or secure automated dispensing system", "In the patient's room", "In the fridge with food"],
        "correctAnswer": 1,
        "explanation": "Controlled substances require strict security, typically involving double-locked storage and inventory logs."
    },
    {
        "id": 9,
        "category": "Patient Education",
        "text": "When discharging a patient with new medications, what is essential to ensure safety?",
        "options": ["Handing them the prescription and leaving", "Educating the patient on the name, purpose, dose, and side effects", "Telling them to look it up online", "Assuming the pharmacist will explain it"],
        "correctAnswer": 1,
        "explanation": "Patient education reduces the risk of non-compliance and adverse events at home."
    },
    {
        "id": 10,
        "category": "Adverse Events",
        "text": "If a patient experiences an unexpected severe reaction to a drug, what should be done?",
        "options": ["Ignore it if it stops", "Document it as an adverse drug reaction and report it", "Blame the pharmacy", "Tell the patient it's normal"],
        "correctAnswer": 1,
        "explanation": "Adverse drug reactions must be documented and reported to prevent future administration and improve safety monitoring."
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
    },
    {
        "id": 6,
        "category": "Safety",
        "text": "Which of the following abbreviations is considered 'dangerous' and should be avoided?",
        "options": ["mg (milligram)", "mL (milliliter)", "U (Unit)", "BP (Blood Pressure)"],
        "correctAnswer": 2,
        "explanation": "'U' can be mistaken for '0' (zero), '4' (four), or 'cc'. Write 'unit' instead."
    },
    {
        "id": 7,
        "category": "Security",
        "text": "What is the best practice when you finish using an electronic medical record (EMR) terminal?",
        "options": ["Turn off the monitor", "Log out completely", "Minimize the window", "Ask the next person to log out for you"],
        "correctAnswer": 1,
        "explanation": "Logging out prevents unauthorized access under your user ID."
    },
    {
        "id": 8,
        "category": "Integrity",
        "text": "Is it acceptable to document care before you actually provide it (pre-charting)?",
        "options": ["Yes, to save time", "No, this is falsification of records", "Only for routine vitals", "If you are sure you will do it"],
        "correctAnswer": 1,
        "explanation": "Documentation must reflect care that has already been delivered. Pre-charting is inaccurate and legally risky."
    },
    {
        "id": 9,
        "category": "Consent",
        "text": "Where should the signed informed consent form be filed?",
        "options": ["In the patient's bedside drawer", "In the medical record prior to the procedure", "With the billing department", "Nowhere, verbal is enough"],
        "correctAnswer": 1,
        "explanation": "The signed consent form must be part of the permanent medical record to prove authorization."
    },
    {
        "id": 10,
        "category": "Patient Rights",
        "text": "Do patients have the right to request amendments to their medical records?",
        "options": ["No, the record is final", "Yes, they can request corrections if they believe there is an error", "Only if the doctor agrees", "Only for billing errors"],
        "correctAnswer": 1,
        "explanation": "HIPAA and other laws grant patients the right to request amendments to their health information."
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
    },
    {
        "id": 6,
        "category": "Alarm Safety",
        "text": "What is 'alarm fatigue'?",
        "options": ["Being tired from waking up early", "Desensitization to safety alarms due to their frequency, leading to missed responses", "A malfunction of the alarm system", "The sound of an alarm"],
        "correctAnswer": 1,
        "explanation": "Alarm fatigue occurs when staff are exposed to so many alarms that they become desensitized, potentially missing critical alerts."
    },
    {
        "id": 7,
        "category": "Fire Safety",
        "text": "In the event of a fire, what does the acronym RACE stand for?",
        "options": ["Run, Ask, Call, Escape", "Rescue, Alarm, Contain, Extinguish/Evacuate", "Report, Act, Control, Exit", "React, Assess, Call, End"],
        "correctAnswer": 1,
        "explanation": "RACE: Rescue patients, Activate Alarm, Contain fire (close doors), Extinguish or Evacuate."
    },
    {
        "id": 8,
        "category": "Infection Control",
        "text": "How does hand hygiene contribute to patient safety?",
        "options": ["It smells good", "It reduces the risk of healthcare-associated infections (HAIs)", "It keeps hands soft", "It is just a formality"],
        "correctAnswer": 1,
        "explanation": "Proper hand hygiene is the most effective way to prevent the spread of infections to patients."
    },
    {
        "id": 9,
        "category": "Patient Engagement",
        "text": "Why should patients be encouraged to 'Speak Up' about their care?",
        "options": ["To be annoying", "To serve as an extra check on safety and prevent errors", "So they don't get bored", "To distract the nurse"],
        "correctAnswer": 1,
        "explanation": "Engaged patients who ask questions can help identify errors and ensure they understand their care plan."
    },
    {
        "id": 10,
        "category": "Handoffs",
        "text": "What is a primary cause of medical errors during patient handoffs (shift changes)?",
        "options": ["Talking too much", "Incomplete or unclear communication of information", "Using a computer", "Being too detailed"],
        "correctAnswer": 1,
        "explanation": "Communication failures during handoffs are a leading cause of sentinel events."
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
    },
    {
        "id": 6,
        "category": "Social Media",
        "text": "Is it acceptable to post a photo of a patient on social media if their face is covered?",
        "options": ["Yes, if they can't be identified", "No, it is a privacy violation and unprofessional", "Only if the patient agrees", "Only if it's a success story"],
        "correctAnswer": 1,
        "explanation": "Posting any patient information or photos, even if de-identified, can violate privacy policies and ethical standards."
    },
    {
        "id": 7,
        "category": "Password Security",
        "text": "What is the rule regarding sharing your computer password with a coworker?",
        "options": ["Allowed if they are temporary staff", "Allowed if they forgot theirs", "Never share your password with anyone", "Allowed if your supervisor says so"],
        "correctAnswer": 2,
        "explanation": "Passwords are unique identifiers. Sharing them compromises accountability and security."
    },
    {
        "id": 8,
        "category": "Breach Reporting",
        "text": "What should you do if you suspect a privacy breach has occurred?",
        "options": ["Ignore it", "Report it immediately to the Privacy Officer or supervisor", "Try to fix it yourself", "Wait to see if anyone notices"],
        "correctAnswer": 1,
        "explanation": "Immediate reporting allows the organization to mitigate harm and comply with legal notification timelines."
    },
    {
        "id": 9,
        "category": "Email",
        "text": "When emailing patient information outside the organization's network, what must you ensure?",
        "options": ["That the email is encrypted", "That you use a catchy subject line", "That you blind copy (BCC) everyone", "That you send it from your personal email"],
        "correctAnswer": 0,
        "explanation": "External emails containing PHI must be encrypted to prevent interception."
    },
    {
        "id": 10,
        "category": "Telephone",
        "text": "When leaving a voicemail for a patient, what information should you leave?",
        "options": ["Detailed test results", "Your name, number, and a request to call back", "The full diagnosis", "Nothing, keep calling"],
        "correctAnswer": 1,
        "explanation": "Limit voicemail messages to the minimum necessary (name and number) to avoid disclosing sensitive info to others."
    }
]

# 7. LABORATORY QUALITY MANAGEMENT (For Lab Technicians)
LAB_QUALITY_QUESTIONS = [
    {
        "id": 1,
        "category": "Quality Control",
        "text": "What is the primary purpose of Internal Quality Control (IQC) in the laboratory?",
        "options": ["To check if the staff is working", "To ensure daily precision and accuracy of test results", "To save reagents", "To impress the patients"],
        "correctAnswer": 1,
        "explanation": "IQC is performed daily to monitor the precision and accuracy of the analytical phase."
    },
    {
        "id": 2,
        "category": "Pre-Analytical",
        "text": "Which of the following is a common cause of pre-analytical error?",
        "options": ["Instrument malfunction", "Wrong calculation", "Hemolyzed sample due to improper collection", "Reporting wrong units"],
        "correctAnswer": 2,
        "explanation": "Hemolysis during collection is a pre-analytical error that can significantly alter test results (e.g., Potassium)."
    },
    {
        "id": 3,
        "category": "Critical Values",
        "text": "What is the immediate action required when a 'Critical Value' is obtained?",
        "options": ["Repeat the test next week", "Inform the clinician/nurse immediately and document the read-back", "Mail the report", "Ignore it if the patient looks fine"],
        "correctAnswer": 1,
        "explanation": "Critical values indicate a life-threatening state; immediate notification and read-back verification are mandatory."
    },
    {
        "id": 4,
        "category": "External Quality Assurance",
        "text": "What does EQAS (External Quality Assurance Scheme) assess?",
        "options": ["The lab's performance compared to other peer laboratories", "The cost of tests", "The speed of the internet", "The attendance of staff"],
        "correctAnswer": 0,
        "explanation": "EQAS involves blinded samples sent by an external agency to compare the lab's accuracy against peer group performance."
    },
    {
        "id": 5,
        "category": "Sample Rejection",
        "text": "A blood sample for coagulation studies (PT/APTT) is collected in a simplified tube but is clotted. What should you do?",
        "options": ["Run the test anyway", "Try to remove the clot", "Reject the sample and request a recollect", "Add heparin"],
        "correctAnswer": 2,
        "explanation": "Clotted samples in coagulation tubes invalidate the results. The sample must be rejected and recollected."
    },
    {
        "id": 6,
        "category": "Calibration",
        "text": "When should instrument calibration typically be performed?",
        "options": ["Only when the machine breaks", "According to manufacturer guidelines or when QC fails repeatedly", "Once every 10 years", "Never"],
        "correctAnswer": 1,
        "explanation": "Calibration establishes the relationship between instrument signal and analyte concentration and is needed regularly or when QC shifts."
    },
    {
        "id": 7,
        "category": "Turnaround Time",
        "text": "Turnaround Time (TAT) is defined as:",
        "options": ["Time from sample collection to report dispatch", "Time taken to eat lunch", "Time taken to print the report", "Time the patient waits in the lobby"],
        "correctAnswer": 0,
        "explanation": "TAT is a key quality indicator measuring the total time from request/collection to result availability."
    },
    {
        "id": 8,
        "category": "Reagent Management",
        "text": "What is the 'First-In, First-Out' (FIFO) principle in reagent inventory?",
        "options": ["Use the newest reagents first", "Use the oldest stock (closest to expiry) first", "Use whatever is closest to your hand", "Don't use reagents"],
        "correctAnswer": 1,
        "explanation": "FIFO ensures that older stock is used before it expires, reducing wastage."
    },
    {
        "id": 9,
        "category": "Biomedical Waste",
        "text": "In which color bag should blood-contaminated waste (e.g., cotton, gauze) be segregated?",
        "options": ["Black", "Blue", "Yellow", "Red"],
        "correctAnswer": 2,
        "explanation": "Yellow bags are typically used for infectious waste like human anatomical waste and items contaminated with blood/body fluids (varies by region, but standard medical waste color)."
    },
    {
        "id": 10,
        "category": "Maintenance",
        "text": "Why is a daily maintenance log important?",
        "options": ["To make the lab look busy", "To provide a trail of evidence that equipment is functioning correctly", "It is not important", "To use up paper"],
        "correctAnswer": 1,
        "explanation": "Maintenance logs prove that equipment was checked and safe to use, which is critical for accreditation and quality assurance."
    }
]

# 8. RADIOLOGY IMAGING QUALITY MANAGEMENT (For Radiology Technicians)
RADIOLOGY_QUALITY_QUESTIONS = [
    {
        "id": 1,
        "category": "Image Quality",
        "text": "What is the most common cause of a blurred X-ray image?",
        "options": ["Patient motion", "Old film", "High kVp", "Low mAs"],
        "correctAnswer": 0,
        "explanation": "Patient movement during exposure is the leading cause of image blur/unsharpness."
    },
    {
        "id": 2,
        "category": "Radiation Safety (ALARA)",
        "text": "To improve image quality while following ALARA, you should use:",
        "options": ["The highest possible dose", "Collimation to restrict the beam to the area of interest", "No shielding", "Multiple exposures"],
        "correctAnswer": 1,
        "explanation": "Collimation improves image contrast by reducing scatter and reduces patient dose, aligning with ALARA."
    },
    {
        "id": 3,
        "category": "Artifacts",
        "text": "What does a 'jewelry artifact' look like on an X-ray?",
        "options": ["A black hole", "A white (radiopaque) shadow obscuring anatomy", "A blur", "A red spot"],
        "correctAnswer": 1,
        "explanation": "Metal objects like jewelry block X-rays, appearing white and potentially hiding pathology."
    },
    {
        "id": 4,
        "category": "Patient Identification",
        "text": "Before performing an X-ray, you notice the request form name does not match the patient's wristband. What do you do?",
        "options": ["Do the X-ray anyway", "Change the name on the form yourself", "Stop and resolve the discrepancy before proceeding", "Ask the patient if they have a nickname"],
        "correctAnswer": 2,
        "explanation": "Correct patient identification is critical. Any discrepancy must be resolved before exposure."
    },
    {
        "id": 5,
        "category": "MRI Safety",
        "text": "Which of the following is strictly prohibited in the MRI magnet room (Zone IV)?",
        "options": ["Cotton clothing", "Ferromagnetic metal objects (e.g., oxygen tanks, scissors)", "Plastic cups", "Paper forms"],
        "correctAnswer": 1,
        "explanation": "The powerful magnet can turn ferromagnetic objects into dangerous projectiles."
    },
    {
        "id": 6,
        "category": "Pregnancy Screening",
        "text": "What is the standard protocol for female patients of childbearing age before an X-ray of the abdomen/pelvis?",
        "options": ["Ask about Last Menstrual Period (LMP) and possibility of pregnancy", "Assume they are not pregnant", "Only ask if they look pregnant", "X-rays are safe for all pregnancies"],
        "correctAnswer": 0,
        "explanation": "Screening for pregnancy is essential to prevent accidental fetal radiation exposure."
    },
    {
        "id": 7,
        "category": "Reject Analysis",
        "text": "What is the purpose of a Reject Analysis Program?",
        "options": ["To fire technicians who make mistakes", "To identify reasons for repeated exams and reduce unnecessary radiation/cost", "To save digital space", "To recycle films"],
        "correctAnswer": 1,
        "explanation": "Analyzing rejected/repeated images helps identify training needs or equipment issues to improve quality."
    },
    {
        "id": 8,
        "category": "Contrast Safety",
        "text": "Before administering IV contrast media, what kidney function test is commonly checked?",
        "options": ["Liver enzymes", "Creatinine / eGFR", "Cholesterol", "Blood sugar"],
        "correctAnswer": 1,
        "explanation": "Creatinine/eGFR levels indicate kidney function; poor function increases the risk of Contrast-Induced Nephropathy."
    },
    {
        "id": 9,
        "category": "PPE Maintenance",
        "text": "How often should lead aprons be checked for cracks/integrity?",
        "options": ["Never", "Annually (or as per policy) via fluoroscopy or tactile inspection", "Every day", "Only when they look torn"],
        "correctAnswer": 1,
        "explanation": "Regular inspection ensures the lead shielding is intact and providing protection."
    },
    {
        "id": 10,
        "category": "Infection Control",
        "text": "After an X-ray on a patient with a contact isolation infection, what should be done to the cassette/detector?",
        "options": ["Wipe it with an approved disinfectant", "Put it back in the pile", "Wash it with soap and water", "Leave it in the sun"],
        "correctAnswer": 0,
        "explanation": "Equipment in contact with patients must be disinfected between uses to prevent cross-contamination."
    }
]

# 9. CRITICAL CARE NURSING COMPETENCY ASSESSMENT
CRITICAL_CARE_QUESTIONS = [
    {
        "id": 1,
        "category": "Hemodynamics",
        "text": "What is the normal range for Mean Arterial Pressure (MAP) required to maintain adequate organ perfusion?",
        "options": ["40-50 mmHg", "65-100 mmHg", "110-130 mmHg", "20-30 mmHg"],
        "correctAnswer": 1,
        "explanation": "A MAP of at least 65 mmHg is generally considered necessary to maintain adequate tissue perfusion."
    },
    {
        "id": 2,
        "category": "Neurological Monitoring",
        "text": "What is the primary purpose of the Glasgow Coma Scale (GCS)?",
        "options": ["To assess pain level", "To assess level of consciousness", "To assess respiratory rate", "To assess muscle strength"],
        "correctAnswer": 1,
        "explanation": "GCS provides a standardized method for assessing the level of consciousness in patients with acute brain injury."
    },
    {
        "id": 3,
        "category": "Ventilation",
        "text": "Which ventilator alarm indicates high pressure in the circuit, potentially due to secretions or biting the tube?",
        "options": ["Low Tidal Volume", "High Pressure Limit / High Peak Pressure", "Low Battery", "Apnea"],
        "correctAnswer": 1,
        "explanation": "High Peak Pressure alarms are triggered by increased resistance (kinks, secretions, biting) or decreased compliance."
    },
    {
        "id": 4,
        "category": "ABG Interpretation",
        "text": "A pH of 7.25, PaCO2 of 60 mmHg, and HCO3 of 24 mEq/L indicates:",
        "options": ["Respiratory Acidosis", "Respiratory Alkalosis", "Metabolic Acidosis", "Metabolic Alkalosis"],
        "correctAnswer": 0,
        "explanation": "Low pH (<7.35) and high PaCO2 (>45) indicate Respiratory Acidosis."
    },
    {
        "id": 5,
        "category": "Vasoactive Drugs",
        "text": "Norepinephrine (Levophed) is primarily used in septic shock to:",
        "options": ["Decrease heart rate", "Increase blood pressure via vasoconstriction", "Increase urine output", "Sedate the patient"],
        "correctAnswer": 1,
        "explanation": "Norepinephrine is a potent vasoconstrictor used as the first-line vasopressor to increase MAP in septic shock."
    },
    {
        "id": 6,
        "category": "ECG Interpretation",
        "text": "Which rhythm is characterized by a chaotic, irregular baseline with no discernible P waves and an irregular R-R interval?",
        "options": ["Sinus Bradycardia", "Atrial Fibrillation", "Ventricular Tachycardia", "First Degree Block"],
        "correctAnswer": 1,
        "explanation": "Atrial Fibrillation is defined by an irregularly irregular rhythm and absence of P waves."
    },
    {
        "id": 7,
        "category": "Sepsis",
        "text": "What is the 'Golden Hour' priority in severe sepsis management?",
        "options": ["Physical therapy", "Antibiotic administration and fluid resuscitation", "Feeding the patient", "Changing the bed linens"],
        "correctAnswer": 1,
        "explanation": "Early administration of broad-spectrum antibiotics and fluids within the first hour significantly reduces mortality."
    },
    {
        "id": 8,
        "category": "ICP Monitoring",
        "text": "What is a normal Intracranial Pressure (ICP) range?",
        "options": ["0-10 mmHg", "5-15 mmHg", "20-40 mmHg", "50-100 mmHg"],
        "correctAnswer": 1,
        "explanation": "Normal ICP is typically 5-15 mmHg. Sustained pressure >20 mmHg is pathological."
    },
    {
        "id": 9,
        "category": "Sedation",
        "text": "The RASS score is used to assess:",
        "options": ["Pain", "Agitation and Sedation levels", "Delirium", "Risk of falls"],
        "correctAnswer": 1,
        "explanation": "The Richmond Agitation-Sedation Scale (RASS) measures the depth of sedation or level of agitation."
    },
    {
        "id": 10,
        "category": "End of Life",
        "text": "What is the primary goal of palliative care in the ICU?",
        "options": ["To cure the disease", "Symptom management and quality of life", "To hasten death", "To ignore the family"],
        "correctAnswer": 1,
        "explanation": "Palliative care focuses on relieving symptoms (pain, dyspnea) and supporting the patient/family, regardless of prognosis."
    }
]

# 10. INTENSIVE CARE COMPETENCY ASSESSMENT
INTENSIVE_CARE_QUESTIONS = [
    {
        "id": 1,
        "category": "VAP Bundle",
        "text": "Which of the following is a key component of the Ventilator-Associated Pneumonia (VAP) prevention bundle?",
        "options": ["Keeping the patient flat", "Head of bed elevation (30-45 degrees)", "Changing circuits daily", "Deep sedation"],
        "correctAnswer": 1,
        "explanation": "Elevating the head of the bed reduces aspiration risk, a key factor in VAP prevention."
    },
    {
        "id": 2,
        "category": "CLABSI Prevention",
        "text": "When accessing a central line, how long should you 'scrub the hub'?",
        "options": ["1 second", "It is not necessary", "15-30 seconds (or per policy)", "5 minutes"],
        "correctAnswer": 2,
        "explanation": "Vigorous friction for 15-30 seconds (using alcohol/chlorhexidine) is critical to prevent CLABSI."
    },
    {
        "id": 3,
        "category": "Delirium",
        "text": "The CAM-ICU tool is used to screen for:",
        "options": ["Depression", "Delirium", "Dementia", "Diabetes"],
        "correctAnswer": 1,
        "explanation": "CAM-ICU (Confusion Assessment Method for the ICU) is the standard tool for detecting delirium."
    },
    {
        "id": 4,
        "category": "Nutrition",
        "text": "Why is early enteral nutrition (within 24-48 hours) preferred in critically ill patients?",
        "options": ["It is cheaper", "It preserves gut mucosal integrity and immune function", "It is easier for nurses", "It prevents diarrhea"],
        "correctAnswer": 1,
        "explanation": "Enteral feeding helps maintain the gut barrier and reduces infectious complications compared to TPN."
    },
    {
        "id": 5,
        "category": "Stress Ulcer Prophylaxis",
        "text": "Which medication class is commonly used for stress ulcer prophylaxis in ICU patients?",
        "options": ["Antibiotics", "Proton Pump Inhibitors (PPIs) or H2 Blockers", "Beta Blockers", "Diuretics"],
        "correctAnswer": 1,
        "explanation": "PPIs (e.g., Pantoprazole) or H2 blockers prevent stress-related mucosal damage/bleeding."
    },
    {
        "id": 6,
        "category": "Glycemic Control",
        "text": "What is the generally recommended target blood glucose range for critically ill patients?",
        "options": ["80-110 mg/dL", "140-180 mg/dL", "200-300 mg/dL", "< 60 mg/dL"],
        "correctAnswer": 1,
        "explanation": "Current guidelines suggest a target of 140-180 mg/dL to avoid hypoglycemia while managing stress hyperglycemia."
    },
    {
        "id": 7,
        "category": "Mobility",
        "text": "What is a benefit of early mobilization in the ICU?",
        "options": ["Increases length of stay", "Reduces ICU-acquired weakness and delirium", "Increases ventilator days", "Makes the patient tired"],
        "correctAnswer": 1,
        "explanation": "Early mobility is proven to improve functional outcomes and reduce delirium and duration of mechanical ventilation."
    },
    {
        "id": 8,
        "category": "Renal Replacement",
        "text": "CRRT (Continuous Renal Replacement Therapy) is indicated for:",
        "options": ["Stable patients with kidney failure", "Hemodynamically unstable patients with AKI", "Routine dialysis", "Dehydration"],
        "correctAnswer": 1,
        "explanation": "CRRT provides slow, continuous fluid/solute removal, making it safer for hemodynamically unstable patients than intermittent hemodialysis."
    },
    {
        "id": 9,
        "category": "DVT Prophylaxis",
        "text": "Unless contraindicated, what is the standard pharmacological DVT prophylaxis in ICU?",
        "options": ["Aspirin", "Low Molecular Weight Heparin (e.g., Enoxaparin) or Heparin", "Warfarin", "TPA"],
        "correctAnswer": 1,
        "explanation": "LMWH or unfractionated heparin are standard for preventing venous thromboembolism in immobile ICU patients."
    },
    {
        "id": 10,
        "category": "Code Blue",
        "text": "During CPR, what is the correct compression rate?",
        "options": ["60-80 per minute", "100-120 per minute", "140-160 per minute", "As fast as possible"],
        "correctAnswer": 1,
        "explanation": "High-quality CPR requires a rate of 100-120 compressions per minute."
    }
]

# 11. EMERGENCY CARE COMPETENCY ASSESSMENT
EMERGENCY_CARE_QUESTIONS = [
    {
        "id": 1,
        "category": "Triage",
        "text": "Using a 5-level triage system (e.g., ESI), a patient requiring immediate life-saving intervention is Level:",
        "options": ["1 (Resuscitation)", "3 (Urgent)", "5 (Non-urgent)", "2 (Emergent)"],
        "correctAnswer": 0,
        "explanation": "Level 1 indicates an immediate threat to life requiring instant intervention (e.g., cardiac arrest)."
    },
    {
        "id": 2,
        "category": "Stroke",
        "text": "What does the FAST acronym stand for in stroke assessment?",
        "options": ["Face, Arm, Speech, Time", "Fast, Action, Save, Time", "Face, Airway, Shock, Trauma", "Feet, Arms, Stomach, Toes"],
        "correctAnswer": 0,
        "explanation": "Face drooping, Arm weakness, Speech difficulty, Time to call emergency services."
    },
    {
        "id": 3,
        "category": "Trauma",
        "text": "In the Primary Survey of trauma, 'A' stands for:",
        "options": ["Alertness", "Airway with C-spine protection", "Allergies", "Assessment"],
        "correctAnswer": 1,
        "explanation": "The Primary Survey ABCDE starts with Airway maintenance with Cervical spine protection."
    },
    {
        "id": 4,
        "category": "ACLS",
        "text": "Which of the following is a shockable rhythm in cardiac arrest?",
        "options": ["Asystole", "Pulseless Electrical Activity (PEA)", "Ventricular Fibrillation (VF)", "Sinus Rhythm"],
        "correctAnswer": 2,
        "explanation": "VF and Pulseless VT are shockable rhythms. Asystole and PEA are not."
    },
    {
        "id": 5,
        "category": "Chest Pain",
        "text": "The standard door-to-ECG time for a patient presenting with chest pain is:",
        "options": ["Within 10 minutes", "Within 30 minutes", "Within 1 hour", "Whenever a doctor sees them"],
        "correctAnswer": 0,
        "explanation": "An ECG should be obtained and interpreted within 10 minutes to identify STEMI."
    },
    {
        "id": 6,
        "category": "Anaphylaxis",
        "text": "What is the first-line medication for anaphylaxis?",
        "options": ["Benadryl (Diphenhydramine)", "Epinephrine (Adrenaline) IM", "Steroids", "Albuterol"],
        "correctAnswer": 1,
        "explanation": "IM Epinephrine is the only medication that reverses the physiological changes of anaphylaxis and must be given immediately."
    },
    {
        "id": 7,
        "category": "Sepsis",
        "text": "A qSOFA score includes which three criteria?",
        "options": ["Fever, WBC, HR", "Altered mental status, Systolic BP <= 100, RR >= 22", "Lactate, BP, Urine output", "HR, O2 Sat, Temp"],
        "correctAnswer": 1,
        "explanation": "qSOFA (quick Sepsis Related Organ Failure Assessment) uses Altered mental status, SBP <= 100, and RR >= 22."
    },
    {
        "id": 8,
        "category": "Toxicology",
        "text": "What is the antidote for Opioid overdose?",
        "options": ["Flumazenil", "Naloxone (Narcan)", "Acetylcysteine", "Atropine"],
        "correctAnswer": 1,
        "explanation": "Naloxone is the specific antagonist for opioids."
    },
    {
        "id": 9,
        "category": "Burns",
        "text": "The 'Rule of Nines' is used to estimate:",
        "options": ["Depth of burn", "Total Body Surface Area (TBSA) burned", "Fluid requirements", "Pain level"],
        "correctAnswer": 1,
        "explanation": "Rule of Nines estimates TBSA to guide fluid resuscitation."
    },
    {
        "id": 10,
        "category": "Pediatrics",
        "text": "What tool is commonly used in the ED to estimate weight and equipment sizes for children?",
        "options": ["Broselow Tape", "BMI Chart", "Guessing", "Adult scales"],
        "correctAnswer": 0,
        "explanation": "The Broselow Tape uses length to estimate weight and appropriate drug doses/equipment sizes for pediatric resuscitation."
    }
]

# 12. PEDIATRIC NURSING CARE COMPETENCY ASSESSMENT
PEDIATRIC_NURSING_QUESTIONS = [
    {
        "id": 1,
        "category": "Assessment",
        "text": "The Pediatric Assessment Triangle (PAT) consists of:",
        "options": ["Appearance, Work of Breathing, Circulation to Skin", "Airway, Breathing, Circulation", "Alertness, Behavior, Crying", "Age, Weight, Height"],
        "correctAnswer": 0,
        "explanation": "PAT provides a rapid visual assessment of a sick child using Appearance, Work of Breathing, and Circulation."
    },
    {
        "id": 2,
        "category": "Vitals",
        "text": "Compared to adults, a normal heart rate for an infant is:",
        "options": ["Slower", "Faster", "The same", "Irregular"],
        "correctAnswer": 1,
        "explanation": "Infants have a much higher metabolic rate and cardiac output demand, leading to higher resting heart rates (e.g., 100-160)."
    },
    {
        "id": 3,
        "category": "Fluid Therapy",
        "text": "Daily maintenance fluid requirements for children are often calculated using the:",
        "options": ["Rule of Nines", "Holliday-Segar (4-2-1) Rule", "Parkland Formula", "Fixed rate of 100ml/hr"],
        "correctAnswer": 1,
        "explanation": "The 4-2-1 rule calculates fluid needs based on weight (4ml/kg for first 10kg, etc.)."
    },
    {
        "id": 4,
        "category": "Medication Safety",
        "text": "Why are pediatric medication calculations considered high-risk?",
        "options": ["Children don't like medicine", "Doses are weight-based (mg/kg), increasing calculation error risk", "Drugs are different", "Syringes are small"],
        "correctAnswer": 1,
        "explanation": "Weight-based dosing requires precise calculation; a decimal point error can be fatal (10-fold overdose)."
    },
    {
        "id": 5,
        "category": "Pain Assessment",
        "text": "Which pain scale is appropriate for a non-verbal infant or toddler?",
        "options": ["Numeric (0-10)", "FLACC Scale", "Visual Analog Scale", "Asking them"],
        "correctAnswer": 1,
        "explanation": "FLACC (Face, Legs, Activity, Cry, Consolability) observes behaviors to assess pain in non-verbal children."
    },
    {
        "id": 6,
        "category": "Respiratory",
        "text": "Which of the following is an early sign of respiratory distress in an infant?",
        "options": ["Cyanosis", "Nasal flaring and retractions", "Apnea", "Sleeping"],
        "correctAnswer": 1,
        "explanation": "Nasal flaring, retractions, and grunting are compensatory mechanisms indicating respiratory distress."
    },
    {
        "id": 7,
        "category": "Development",
        "text": "Separation anxiety typically peaks around what age?",
        "options": ["1 month", "6-18 months", "5 years", "Teenagers"],
        "correctAnswer": 1,
        "explanation": "Separation anxiety is a normal developmental stage peaking in older infants and toddlers."
    },
    {
        "id": 8,
        "category": "Safety",
        "text": "When leaving a toddler in a crib, the side rails should be:",
        "options": ["All the way down", "Halfway up", "All the way up and secured", "Removed"],
        "correctAnswer": 2,
        "explanation": "Rails must be fully up and locked to prevent falls."
    },
    {
        "id": 9,
        "category": "Dehydration",
        "text": "A sunken fontanelle in an infant is a sign of:",
        "options": ["Overhydration", "Dehydration", "Increased intracranial pressure", "Normal finding"],
        "correctAnswer": 1,
        "explanation": "A depressed or sunken anterior fontanelle suggests significant volume depletion."
    },
    {
        "id": 10,
        "category": "Family Centered Care",
        "text": "Family-Centered Care implies:",
        "options": ["The family does all the work", "Parents are visitors", "Collaboration between healthcare staff and the family as partners in care", "Family is excluded from rounds"],
        "correctAnswer": 2,
        "explanation": "It recognizes the family as the constant in the child's life and partners with them in decision-making and care."
    }
]

# -----------------------------------------------------------------------------
# MAPPINGS
# -----------------------------------------------------------------------------

# Subset for Technicians / Allied Health (Focus on Equipment, PPE, Precautions)
# Using IDs: 1, 3, 5, 6, 8, 10, 13, 14, 15, 20 from Infection Control
TECHNICIAN_IC_IDS = [1, 3, 5, 6, 8, 10, 13, 14, 15, 20]
TECHNICIAN_INFECTION_CONTROL_QUESTIONS = [q for q in INFECTION_CONTROL_QUESTIONS if q['id'] in TECHNICIAN_IC_IDS]

# Map Module Names to Question Sets
ASSESSMENT_MODULES = {
    "Infection Control Guidelines": INFECTION_CONTROL_QUESTIONS,
    "Basic Infection Control (Technician)": TECHNICIAN_INFECTION_CONTROL_QUESTIONS,
    "Radiation Safety Guidelines": RADIATION_SAFETY_QUESTIONS,
    "Medication Safety Guidelines": MEDICATION_SAFETY_QUESTIONS,
    "Medical Records Documentation": MEDICAL_RECORDS_QUESTIONS,
    "Patient Safety Guidelines": PATIENT_SAFETY_QUESTIONS,
    "Patient Confidentiality": PATIENT_CONFIDENTIALITY_QUESTIONS,
    "Laboratory Quality Management Competency Assessment": LAB_QUALITY_QUESTIONS,
    "Radiology Imaging Quality Management Competency Assessment": RADIOLOGY_QUALITY_QUESTIONS,
    "Critical Care Nursing Competency Assessment": CRITICAL_CARE_QUESTIONS,
    "Intensive Care Competency Assessment": INTENSIVE_CARE_QUESTIONS,
    "Emergency Care Competency Assessment": EMERGENCY_CARE_QUESTIONS,
    "Pediatric Nursing Care Competency Assessment": PEDIATRIC_NURSING_QUESTIONS
}

# Map Roles to Eligible Assessment Modules
ROLE_ACCESS = {
    "Infection Control Nurse (ICN)": [
        "Infection Control Guidelines",
        "Patient Safety Guidelines",
        "Critical Care Nursing Competency Assessment",
        "Intensive Care Competency Assessment"
    ],
    "Staff Nurse": [
        "Infection Control Guidelines",
        "Patient Safety Guidelines",
        "Critical Care Nursing Competency Assessment",
        "Intensive Care Competency Assessment",
        "Emergency Care Competency Assessment",
        "Pediatric Nursing Care Competency Assessment"
    ],
    "Physician / Doctor": [
        "Medication Safety Guidelines",
        "Medical Records Documentation",
        "Patient Safety Guidelines"
    ],
    "Technician / Allied Health": [
        "Basic Infection Control (Technician)",
        "Radiation Safety Guidelines",
        "Patient Safety Guidelines"
    ],
    "Laboratory Technician": [
        "Laboratory Quality Management Competency Assessment",
        "Basic Infection Control (Technician)",
        "Patient Safety Guidelines"
    ],
    "Radiology & Imageology Technician": [
        "Radiology Imaging Quality Management Competency Assessment",
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
