from pydantic import BaseModel, Field


class Prompt(BaseModel):
    text: str
    user_id: str


class symptom_eval(BaseModel):
    patient_feels_nausia: bool = Field("The patient feels nausia")
    patient_feels_pain: bool = Field("The patient feels pain")
    patient_feels_anxiety: bool = Field("The patient is anxious")


class pizza_eval(BaseModel):
    pizza: bool = Field("Whether is ")
