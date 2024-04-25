from langchain.output_parsers import PydanticOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.runnables import (
    ConfigurableFieldSpec,
    Runnable,
    RunnableLambda,
    RunnableParallel,
)
from langchain_core.runnables.history import (
    RunnableWithMessageHistory,
)
from langchain_google_vertexai import ChatVertexAI, HarmBlockThreshold, HarmCategory

from maximai.schemas import symptom_eval
from maximai.template import get_eval_prompt
from maximai.utils import debug

store = {}

llm = ChatVertexAI(
    model_name="gemini-1.0-pro",
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_NONE,
    },
)

def debug(x):
    print(x)
    return x

def debug_convo(x):
    if nausia := x.nausia:
        print(f"YES, nausia is mentioned! Pydantic output == {nausia}")
    if pain := x.pain:
        print(f"YES, pain is mentioned! Pydantic output == {pain}")
    if anxiety := x.anxiety:
        print(f"YES, anxiety is mentioned! Pydantic output == {anxiety}")
    return x

def get_user_history(user_id: str) -> BaseChatMessageHistory:
    if user_id not in store:
        store[user_id] = ChatMessageHistory()
    return store[user_id]

def create_eval_chain() -> Runnable:
    parser = PydanticOutputParser(pydantic_object=symptom_eval)

    eval = get_eval_prompt()
    eval_prompt = eval.partial(format_instructions=parser.get_format_instructions())
    return eval_prompt | llm | parser | RunnableLambda(debug)


def create_interaction_chain() -> Runnable:
    interact_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{context}"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )
    return interact_prompt | llm


def create_chat_chain() -> Runnable:
    """
    Creates a chat chain with a prompt template that is can be used to personalize contexts.

    Returns:
        Runnable: Simple conversational chain.
    """
    
    interact_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "{context}. If one if the sympoms in the Pydantic schema {eval} is true, react to the symptom that are true"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )
    
    parser = PydanticOutputParser(pydantic_object=symptom_eval)
    
    eval = get_eval_prompt()
    eval_prompt = eval.partial(
        format_instructions=parser.get_format_instructions()
    )
    return RunnableParallel({
        "eval": eval_prompt | llm | parser, 
        "context": RunnableLambda(lambda x : x["context"]),
        "input": RunnableLambda(lambda x : x["input"]),
        "history": RunnableLambda(lambda x : x["history"])
    }) | interact_prompt | llm


def create_context_aware_chatbot() -> Runnable:
    """
    Creates a context-aware chatbot that persists conversations of different users in memory.

    Returns:
        Runnable: LangChain runnable that is used for conversations.
    """
    return RunnableWithMessageHistory(
        create_chat_chain(),
        get_user_history,
        input_messages_key="input",
        history_messages_key="history",
        history_factory_config=[
            ConfigurableFieldSpec(
                id="user_id",
                annotation=str,
                name="User ID",
                description="Unique identifier for the user.",
                default="",
                is_shared=True,
            )
        ],
    )
