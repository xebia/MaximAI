from fastapi import FastAPI

from maximai.langchain import create_context_aware_chatbot
from maximai.schemas import Prompt

app = FastAPI(title="Retrieval App")

chatbot = create_context_aware_chatbot()


def get_context(user_id: str) -> str:
    info = {
        "sander": "pizza",
        "shu": "donuts",
        "julian": "british scones",
    }
    return info[user_id]


# Define a route to handle API calls
@app.post("/chat")
async def root(prompt: Prompt):
    output = chatbot.invoke(
        {"input": prompt.text, "context": get_context(prompt.user_id)},
        config={"configurable": {"user_id": prompt.user_id}},
    )
    return {"message": output.content}
