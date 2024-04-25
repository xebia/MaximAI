def get_context(user_id: str) -> str:
    info = {
        "sander": "pizza",
        "shu": "donuts",
        "julian": "british scones",
    }
    return info[user_id]

#
# For a given patient, get the right type of questions to ask.
#
# NOTE: static for now
#
def get_patient_questions_skeleton(user_id: str) -> str:
    return """
Your task as a nurse is to get into an interactive conversation with a child on
a level that the child understands. You need to gather information by using
questions like the following? In the conversation, ask about the following and
in the following way.

* Loss of function *
 + Can you raise your arm all the way up?
 + Are you having trouble bending your elbow or using your hand?
 + Is there any numbness or tingling in your arm or hand?

*Pain*
 + Where exactly does the pain feel?
 + Is it a sharp pain, a dull ache, or something else?
 + Does it happen all the time, or is it worse at certain times?

*Emotional well-being*
 + It sounds like you might be feeling a little strange as well.
 + It's completely normal to feel this way, and I want to make sure you have all the support you need.

*Side effects of treatment*
 + Are you feeling strong?
 + How are your arms feeling?
 + Do you have pain in your arms?
 + Do you feel sick?
 + Are you still eating?
    """

def get_persona_and_goal() -> str:
    return """
You are a nurse working for the Prinses Maxima Center. You are
specialized in care for children treated for cancer. You are strong in empathy
while having a conversation with a child.
    """

def get_general_context() -> str:
    return """
The children you speak to have some form of cancer and are being treated in the
Princess Maxima Center for Child Oncology. They are staying in this hospital
during their treatment. They suffer from pain, side effects and other symptoms
related to their disease or their treatment.
    """

def get_format_prompt() -> str:
    return """
Get into an active conversation with child [name]. Ask appropriate questions in
the that of child of age [age[] understands. The questions need to gain an
understanding of the child's current symptoms and the side effects of the
medications [name] is taking.

Ask  simple questions. Ask one question at the time.
    """

def get_patient_info(user_id: str) -> str:
    info = {
        "Emmy": { 'age': 8,
                  'info': "Diagnosed with osteosarcoma in left shoulder, treatment according to EURAMOS 1 protocol, successful resection of tumor, received treatment with doxorubicin, cisplatin, methotrexate, ifosfamide, and etoposide is now in the 25th week of treatment. She experiences loss of functionality in left arm, has pain and is anxious.",
                 },
        "David": { 'age': 3,
                   'info': "Diagnosed with neuroblastoma stadium IV, or INRG stadium HR, treatment with DCOG NBL, in his 5th N5 cycle. He receives tube feeding and is very nauseous. He vomits 4-5 time a day and the tube feeding is frequently interrupted.",
                  },
        "Jenny": { 'age': 6,
                   'info': "Diagnosed with Wilms tumor stadium IV, resection of kidney, receives vincristine, doxorubicin, actinomycin. She is normally a very active child, but currently she suffers from abdominal pain and stays in bed whole day.",
                  },
        "Jan": { 'age': 12,
                'info': "Diagnosed with medulloblastoma, brain surgery and treatment with COG ACNS 0331 and radiation. Experiences headache, fatigue and nausea.",
               },
        "Bjorn": { 'age': 16,
                   'info': "Diagnosed with craniopharyngioma, a very wise and talkative person. Brain surgery and partly resection of the tumor. It is one week after surgery, he experiences drowsiness and nausea when he leaves his bed. Despite his restrictions, needs help to go to the bathroom and experiences difficulty walking, he is happy and grateful that he survived surgery.",
                  },
        "Roy": { 'age': 15,
                 'info': "Diagnosed with Hodgkin lymphoma (cHL), treatment according to DECOPDAC-21. He received two cycles COPP-ABV: (cyclophosphamide, vincristine, procarbazine, prednisone, doxorubicin, bleomycin, vinblastine). Roy is a quiet and shy person, he is not very talkative. He has no appetite, experiences difficulty with sleeping and feels very tired.",
                },
        "Daisy": { 'age': 17,
                   'info': "Diagnosed with non-Hodgkin lymphoma (DLBCL). Treatment with cyclophosphamide, MTX and ARA-C. She used to have long blond hair and she feels miserable about being bald and about her changed appearance. She often feels sick and tired.",
                  },
        "Ella": { 'age': 3,
                  'info': "Diagnosed with AML, treatment protocol NOPHO-DBH AML 2012. She has finished FLA cycle (fludarabine, cytarabine and MTX intrathecal). She does not want to eat or talk, is anxious and sits on her mother’s lap when the nurse enters the room.",
                 },
        "Peter": { 'age': 10,
                   'info': "Diagnosed with ALL SR and treated according to ALLtogether 1, end of induction (received dexamethasone). He is passive and inactive and prefers fries for diner. He has sometimes constipation and abdominal pain.",
                  },
        "Thom": { 'age': 4,
                  'info': "Diagnosed with DIPG 7 months ago. He is in incurable and in palliative phase of his disease. He has difficulty walking, and talking. He is tired and needs assistance for quiet play. He is drowsy and feels often nauseous and has a headache.",
                  },
    }
    return info[user_id]

def get_patient_context(user_id: str) -> str:
    patient = get_patient_info(user_id)
    return f"%s is %d years old. %s" % (user_id, patient['age'], patient['info'])

# Ask in a tone of voice that is adapted to the age of the patient
def get_tone_of_voice(user_id: str) -> str:
    patient = get_patient_info(user_id)
    age = patient['age']
    if age < 12:
        simple = "Ask simple questions."
    else:
        simple = "Ask serious questions."

    general = "Ask one question at the time. Always ask a follow-up question. Start by building empathy."

    return f"%s Use language that is at the level of a child of %d years old. %s" % (simple, age, general)

# We format the prompt according to [docs/prompt-format.png]
#
# - Persona + Goal
# - Context
# - Instructions
# - Tone
# - Format (e.g. table with columns, not used here)
# - Input
def get_full_patient_context(user_id: str) -> str:
    return f"%s\n%s\n%s\n%s\n" % (
        get_persona_and_goal(),
        get_general_context(),
        get_patient_questions_skeleton(user_id), # instructions, get be user-specific
        get_tone_of_voice(user_id),
        get_patient_context(user_id) # input with the medical context
    )


