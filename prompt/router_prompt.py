from langchain_core.prompts import ChatPromptTemplate

prompt_text = """
You are a query classifier for a wedding planner assistant.
Classify the user's query into one of the following categories:
- fashion
- venue
- catering
If it doesn't match any category, reply with 'general'.

Output only the category.
"""

router_prompt = ChatPromptTemplate(
    [
        ("system",prompt_text),
        ("human","Query : {query}")
    ]
    )




