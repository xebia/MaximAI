def get_context(user_id: str) -> str:
    info = {
        "sander": "pizza",
        "shu": "donuts",
        "julian": "british scones",
    }
    return info[user_id]


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
