from fastapi import FastAPI

from maximai.context import get_full_patient_context
from maximai.langchain import create_context_aware_chatbot
from maximai.schemas import Prompt

app = FastAPI(title="MaximAI Chat App")

# et_debug(True)

chatbot = create_context_aware_chatbot()


# Define a route to handle API calls
@app.post("/chat")
async def root(prompt: Prompt):
    context = get_full_patient_context(prompt.user_id)
    print(context)
    output = chatbot.invoke(
        {"input": prompt.text, "context": context},
        config={"configurable": {"user_id": prompt.user_id}},
    )
    # output = output["content"]
    return {
        "input_message": prompt.text,
        "output_message": output.content,
        "user_id": prompt.user_id,
    }
