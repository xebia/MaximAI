from langchain.output_parsers import PydanticOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
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
from langchain_google_vertexai import ChatVertexAI
from maximai.schemas import symptom_eval


store = {}


def get_user_history(user_id: str) -> BaseChatMessageHistory:
    if user_id not in store:
        store[user_id] = ChatMessageHistory()
    return store[user_id]


def create_chat_chain() -> Runnable:
    """
    Creates a chat chain with a prompt template that is can be used to personalize contexts.

    Returns:
        Runnable: Simple conversational chain.
    """
    interact_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "{context}",
            ),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )

    eval_prompt_template = PromptTemplate.from_template(
        template="""
        You are getting a conversation as input.
        
        Output whether the user experiences any side effects
        
        user last message is:
        {input}
        
        Chat History is:
        {history}
        
        {format_instructions}
        """
    )
    parser = PydanticOutputParser(pydantic_object=symptom_eval)
    eval_prompt = eval_prompt_template.partial(
        format_instructions=parser.get_format_instructions()
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

    llm = ChatVertexAI(model_name="gemini-1.0-pro")
    return RunnableParallel(
        {
            "eval": eval_prompt | llm | parser | RunnableLambda(debug_convo),
            "output": interact_prompt | llm,
        }
    )


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
