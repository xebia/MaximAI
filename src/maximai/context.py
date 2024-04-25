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
In the conversation, ask about the following and in the following way.
•	Loss of function:
o	Can you raise your arm all the way up?
o	Are you having trouble bending your elbow or using your hand?
o	Is there any numbness or tingling in your arm or hand?
•	Pain:
o	Where exactly does the pain feel?
o	Is it a sharp pain, a dull ache, or something else?
o	Does it happen all the time, or is it worse at certain times?
j
Assess emotional well-being:
•	It sounds like you might be feeling a little anxious too. Is there anything specific that's making you anxious, or is it just the whole situation?
•	It's completely normal to feel this way, and I want to make sure you have all the support you need.

Understanding the Causes,
symptoms could be related to a few things:
•	Side effects of treatment: The chemotherapy medications she received (doxorubicin, cisplatin) can sometimes cause weakness, pain, and nerve damage, which could be affecting her arm function.
•	Surgery: The surgery to remove the tumor might have involved some muscle or nerve tissue, which could also be contributing to her pain and weakness.

Reassurance:
It's important to reassure  symptoms are common and treatable. We'll work together to manage her pain and help her regain function in her arm.

Next Steps:
Based on the answers, I might recommend:
•	Physical therapy: This can help her regain strength and movement in her arm.
•	Pain medication: There are medications that can help manage her pain and improve her comfort.
•	Occupational therapy:
    """



def get_persona_and_goal() -> str:
    return """
You are a nurse having a conversation with a child named [name] who is
[age] years old. You adapt your language to suit the child's age. As a nurse,
you begin by asking what [name] did today. Then, you ask [name] how [name] is
feeling now. Engage in an interactive conversation with [name].
    """

def get_format_prompt() -> str:
    return """
Get into an active conversation with child [name]. Ask appropriate questions in
the that of child of age [age[] understands. The questions need to gain an
understanding of the child's current symptoms and the side effects of the
medications [name] is taking.

Ask  simple questions. Ask one question at the time.
    """

def get_patient_context(user_id: str) -> str:
    info = {
        "Emmy": "Emmy, 8 years old, diagnosed with osteosarcoma in left shoulder, treatment according to EURAMOS 1 protocol, successful resection of tumor, received treatment with doxorubicin, cisplatin, methotrexate, ifosfamide, and etoposide is now in the 25th week of treatment. She experiences loss of functionality in left arm, has pain and is anxious.",
        "David": "David, 3 years old, diagnosed with neuroblastoma stadium IV, or INRG stadium HR, treatment with DCOG NBL, in his 5th N5 cycle. He receives tube feeding and is very nauseous. He vomits 4-5 time a day and the tube feeding is frequently interrupted.",
        "Jenny": "Jenny, 6 years old, diagnosed with Wilms tumor stadium IV, resection of kidney, receives vincristine, doxorubicin, actinomycin. She is normally a very active child, but currently she suffers from abdominal pain and stays in bed whole day.",
        "Jan": "Jan, a 12 years old boy with medulloblastoma, brain surgery and treatment with COG ACNS 0331 and radiation. Experiences headache, fatigue and nausea.",
        "Bjorn": "Bjorn, 16 years old, diagnosed with craniopharyngioma, a very wise and talkative person. Brain surgery and partly resection of the tumor. It is one week after surgery, he experiences drowsiness and nausea when he leaves his bed. Despite his restrictions, needs help to go to the bathroom and experiences difficulty walking, he is happy and grateful that he survived surgery.",
        "Roy": "Roy, 15 years, diagnosed with Hodgkin lymphoma (cHL), treatment according to DECOPDAC-21. He received two cycles COPP-ABV: (cyclophosphamide, vincristine, procarbazine, prednisone, doxorubicin, bleomycin, vinblastine). Roy is a quiet and shy person, he is not very talkative. He has no appetite, experiences difficulty with sleeping and feels very tired.",
        "Daisy": "Daisy, 17 years, diagnosed with non-Hodgkin lymphoma (DLBCL). Treatment with cyclophosphamide, MTX and ARA-C. She used to have long blond hair and she feels miserable about being bald and about her changed appearance. She often feels sick and tired.",
        "Ella": "Ella, 3 years, diagnosed with AML, treatment protocol NOPHO-DBH AML 2012. She has finished FLA cycle (fludarabine, cytarabine and MTX intrathecal). She does not want to eat or talk, is anxious and sits on her mother’s lap when the nurse enters the room.",
        "Peter": "Peter, 10 years old, diagnosed with ALL SR and treated according to ALLtogether 1, end of induction (received dexamethasone). He is passive and inactive and prefers fries for diner. He has sometimes constipation and abdominal pain.",
        "Thom": "Thom, 4 years old, diagnosed with DIPG 7 months ago. He is in incurable and in palliative phase of his disease. He has difficulty walking, and talking. He is tired and needs assistance for quiet play. He is drowsy and feels often nauseous and has a headache.",
    }
    return info[user_id]

def get_format_prompt(user_id: str) -> str:
    return """

    You are a nurse having a conversation with a child named [name] who is
    [age] years old. You adapt your language to suit the child's age. As a nurse,
    you begin by asking what [name] did today. Then, you ask [name] how [name] is
    feeling now. Engage in an interactive conversation with [name].

    Get into an active conversation with child [name]. Ask appropriate questions in
    the that of child of age [age[] understands. The questions need to gain an
    understanding of the child's current symptoms and the side effects of the
    medications [name] is taking.

    Ask  simple questions. Ask one question at the time.

    """

def get_full_patient_context(user_id: str) -> str:
    return f"%s\n%s\n%s\n%s\n" % (
        get_persona_and_goal(),
        get_patient_questions_skeleton(user_id),
        get_format_prompt(),
        get_patient_context(user_id)
    )


