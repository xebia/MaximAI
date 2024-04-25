from pydantic import BaseModel, Field

class Prompt(BaseModel):
    text: str
    user_id: str


class symptom_eval(BaseModel):
    nausia: bool = Field("The patient feels nausius")
    pain: bool = Field("The patient has pain")
    anxiety: bool = Field("The patient is anxious")
