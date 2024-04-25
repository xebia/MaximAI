from fastapi import FastAPI

from maximai.langchain import create_context_aware_chatbot
from maximai.context import get_patient_context
from maximai.schemas import Prompt

app = FastAPI(title="MaximAI Chat App")

chatbot = create_context_aware_chatbot()


# Define a route to handle API calls
@app.post("/chat")
async def root(prompt: Prompt):
    output = chatbot.invoke(
        {"input": prompt.text, "context": get_patient_context(prompt.user_id)},
        config={"configurable": {"user_id": prompt.user_id}},
    )
    output = output["output"]
    return {
        "input_message": prompt.text,
        "output_message": output.content,
        "user_id": prompt.user_id,
    }
