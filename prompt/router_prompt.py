from langchain_core.prompts import ChatPromptTemplate

prompt_text = """
You are a query classifier for a wedding planner assistant.
Classify the user's query into one of the following categories:
- fashion: wedding outfits, attire, dress, suit,kurta, shervani, groom outfit, bride dress, styling
- venue: location, hall, place, resort, banquet, venue
- catering: food, menu, catering, dining, cuisine, restaurant, meals
- photographer: photography, photos, cameraman, wedding shoot, pre-wedding, candid, video, album, photo package

If it doesn't match any category, reply with 'general'.

Rules:
- If user asks for "more options", "alternatives", "same" 
- use the category from previous conversation
- Consider follow-up context from chat history
-Output only the category.
chat_history={chat_history}
"""

router_prompt = ChatPromptTemplate(
    [
        ("system",prompt_text),
        ("human","Query : {query}")
    ]
    )


# from langchain_core.prompts import PromptTemplate

# router_prompt = ChatPromptTemplate.from_messages("""
# Classify this wedding planning query based on current input and conversation history.

# Chat History: {chat_history}
# Current Query: {query}

# Classification Rules:
# 1. Follow-up indicators ("more options", "alternatives", "same", "different") → Use previous category
# 2. Fashion keywords (outfit, dress, suit, attire, groom, bride, styling) → fashion  
# 3. Food keywords (catering, menu, food, dining, cuisine, meals) → catering
# 4. Location keywords (venue, hall, place, location, destination) → venue
# 5. Photo keywords (photographer, photos, pictures, videographer) → photography
# 6. Default → general

# Return only: fashion, catering, venue, photography, or general
# """
# )

# from langchain.prompts import ChatPromptTemplate
 
# router_prompt = ChatPromptTemplate.from_messages([
#     ("system",
#      """
# Classify this wedding planning query based on current input and conversation history.

# Classification Rules:
# 1. Follow-up indicators ("more options", "alternatives", "same", "different") → Use previous category
# 2. Fashion keywords (outfit, dress, suit, attire, groom, bride, styling) → fashion  
# 3. Food keywords (catering, menu, food, dining, cuisine, meals) → catering
# 4. Location keywords (venue, hall, place, location, destination) → venue
# 5. Photo keywords (photographer, photos, pictures, videographer) → photography
# 6. Default → general

# Return only: fashion, catering, venue, photography, or general
# """
#      "Recent History:{chat_history}"),
#     ("user", "{query}"),
# ])