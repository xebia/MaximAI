from fastapi import FastAPI

from maximai.langchain import create_context_aware_chatbot, get_context
from maximai.schemas import Prompt

app = FastAPI(title="Retrieval App")

chatbot = create_context_aware_chatbot()


# Define a route to handle API calls
@app.post("/chat")
async def root(prompt: Prompt):
    output = chatbot.invoke(
        {"input": prompt.text, "context": get_context(prompt.user_id)},
        config={"configurable": {"user_id": prompt.user_id}},
    )
    return {"message": output.content}
