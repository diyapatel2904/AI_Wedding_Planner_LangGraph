from langchain_core.prompts import ChatPromptTemplate

prompt_text=""" 
    "You are a helpful wedding planning assistant.
    If the query does not fit fashion, venue, or catering, provide general advice, \
    tips, or answers about weddings.
"""

general_prompt = ChatPromptTemplate([
    ("system", prompt_text),
    ("human", "{query}")
])
