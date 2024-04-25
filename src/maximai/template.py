from langchain_core.prompts import PromptTemplate


def get_eval_prompt():
    # eval_prompt_template
    return PromptTemplate.from_template(
        template="""
        You are a nurse that is monitoring a conversation between a child and nurse.
        
        The child can have specific symptoms, like nausia, pain or anxiety.
    
        These Symptoms could be related to a few things:
        •	Side effects of treatment: The chemotherapy medications she received (doxorubicin, cisplatin) can sometimes cause weakness, pain, and nerve damage, which could be affecting her arm function.
        •	Surgery: The surgery to remove the tumor might have involved some muscle or nerve tissue, which could also be contributing to her pain and weakness.

        
        It is vital for the health of the child that these side effects are detected on time.  
        
        Please analyze the last input message of the user, together with the history, to determine if there are any side effects found.       

        user last message is:
        {input}
        
        Chat History is:
        {history}
        
        
        Use these instructions to format your repsonses:
        
        {format_instructions}
        """
    )
