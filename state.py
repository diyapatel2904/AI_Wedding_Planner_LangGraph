from typing import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages

class WeddingState(TypedDict):
    query: str
    intent: str     # What kind of request it is (fashion, venue, etc.)
    response: str 
    messages: Annotated[list, add_messages]
