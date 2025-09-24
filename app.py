
# import streamlit as st
# import time
# from workflow import build_workflow
# from loguru import logger
# import traceback
# import random

# # Configure page
# st.set_page_config(
#     page_title="Wedding Planner Chatbot",
#     page_icon="💍",
#     layout="wide"
# )

# # Custom CSS for chat UI
# st.markdown("""
# <style>
# .main-header {
#     text-align: center;
#     color: #ffffff;
#     font-size: 2.5rem;
#     margin-bottom: 0rem;
#     background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
#     padding: 1rem;
#     border-radius: 10px;
# }

# .chat-container {
#     height: 400px;
#     overflow-y: auto;
#     padding: 1rem;
#     background-color: #2e3440;
#     border-radius: 10px;
#     margin-bottom: 1rem;
# }

# .user-message {
#     background-color: #5e81ac;
#     color: white;
#     padding: 0.8rem 1rem;
#     border-radius: 18px;
#     margin: 0.5rem 0;
#     margin-left: 20%;
#     word-wrap: break-word;
# }

# .bot-message {
#     background-color: #4c566a;
#     color: white;
#     padding: 0.8rem 1rem;
#     border-radius: 18px;
#     margin: 0.5rem 0;
#     margin-right: 20%;
#     word-wrap: break-word;
# }

# .message-info {
#     font-size: 0.8rem;
#     color: #88c0d0;
#     margin: 0.2rem 1rem;
# }

# .user-info {
#     text-align: right;
#     margin-right: 20%;
# }

# .bot-info {
#     text-align: left;
#     margin-left: 0;
# }

# .stChatInput {
#     position: fixed;
#     bottom: 0;
#     left: 0;
#     right: 0;
#     background-color: white;
#     padding: 1rem;
#     border-top: 1px solid #ddd;
# }
# </style>
# """, unsafe_allow_html=True)

# def initialize_workflow():
#     """Initialize the workflow once and cache it."""
#     try:
#         with st.spinner("Initializing Wedding Planner workflow..."):
#             workflow = build_workflow()
#         return workflow
#     except Exception as e:
#         st.error(f"Failed to initialize workflow: {str(e)}")
#         logger.error(f"Workflow initialization error: {traceback.format_exc()}")
#         return None

# def display_chat_history():
#     """Display chat history in a chat-like interface."""
#     st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
#     if 'chat_history' in st.session_state and st.session_state.chat_history:
#         for i, (user_msg, bot_msg, intent, thread_id) in enumerate(st.session_state.chat_history):
#             # User message
#             st.markdown(f'<div class="user-message">👤 {user_msg}</div>', unsafe_allow_html=True)
            
#             # Bot message
#             st.markdown(f'<div class="bot-message">🤖 {bot_msg}</div>', unsafe_allow_html=True)
            
#             # Message info
#             st.markdown(f'<div class="message-info bot-info">Intent: {intent} | Thread: {thread_id}</div>', unsafe_allow_html=True)
            
#             # Add some spacing between conversations
#             if i < len(st.session_state.chat_history) - 1:
#                 st.markdown('<hr style="border-color: #4c566a; margin: 1rem 0;">', unsafe_allow_html=True)
#     else:
#         st.markdown('<div class="bot-message">🤖 Hello! How can I assist you with your wedding planning today?</div>', unsafe_allow_html=True)
    
#     st.markdown('</div>', unsafe_allow_html=True)

# def process_query(query, thread_id):
#     """Process the user query through the workflow with memory."""
    
#     try:
#         # Create initial state
#         initial_state = {
#             "query": query,
#             "intent": "",
#             "response": "",
#             "messages": []
#         }
        
#         # Create thread config for memory
#         thread_config = {"configurable": {"thread_id": thread_id}}
        
#         # Invoke workflow with thread_id for memory
#         result = st.session_state.workflow.invoke(initial_state, config=thread_config)
        
#         # Extract response and intent
#         intent = result.get("intent", "unknown")
#         response = result.get("response", "No response generated")
        
#         return response, intent
        
#     except Exception as e:
#         logger.error(f"Query processing error: {traceback.format_exc()}")
#         return f"Sorry, I encountered an error: {str(e)}", "error"

# def main():
#     # Header
#     st.markdown('<h1 class="main-header">💍 Wedding Planner Chatbot</h1>', unsafe_allow_html=True)
    
#     # Initialize workflow
#     if 'workflow' not in st.session_state:
#         st.session_state.workflow = initialize_workflow()
    
#     if st.session_state.workflow is None:
#         st.error("⚠️ Could not initialize the workflow. Please check your configuration.")
#         return

#     # Initialize chat history and thread_id
#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history = []
    
#     if 'thread_id' not in st.session_state:
#         st.session_state.thread_id = str(random.randint(1000, 9999))

#     # Display chat history
#     st.markdown("")  # Minimal spacing
#     display_chat_history()
    
#     # Chat input
#     user_input = st.chat_input("Ask about your wedding...")
    
#     # Process new message
#     if user_input:
#         # Show processing spinner
#         with st.spinner("🤖 Thinking..."):
#             # Process query with memory (same thread_id for conversation continuity)
#             bot_response, intent = process_query(user_input, st.session_state.thread_id)
        
#         # Add to chat history
#         st.session_state.chat_history.append((user_input, bot_response, intent, st.session_state.thread_id))
        
#         # Rerun to update the display
#         st.rerun()

# if __name__ == "__main__":
#     main()



import streamlit as st
import time
from workflow import build_workflow
from loguru import logger
import traceback
import random

# Configure page
st.set_page_config(
    page_title="Wedding Planner Chatbot",
    page_icon="💍",
    layout="wide"
)

# Custom CSS for chat UI
st.markdown("""
<style>
.main-header {
    text-align: center;
    color: #ffffff;
    font-size: 2.5rem;
    margin-bottom: 0rem;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    padding: 1rem;
    border-radius: 10px;
}

.chat-container {
    height: 400px;
    overflow-y: auto;
    padding: 1rem;
    background-color: #2e3440;
    border-radius: 10px;
    margin-bottom: 1rem;
}

.user-message {
    background-color: #5e81ac;
    color: white;
    padding: 0.8rem 1rem;
    border-radius: 18px;
    margin: 0.5rem 0;
    margin-left: 20%;
    word-wrap: break-word;
}

.bot-message {
    background-color: #4c566a;
    color: white;
    padding: 0.8rem 1rem;
    border-radius: 18px;
    margin: 0.5rem 0;
    margin-right: 20%;
    word-wrap: break-word;
}

.message-info {
    font-size: 0.8rem;
    color: #88c0d0;
    margin: 0.2rem 1rem;
}

.user-info {
    text-align: right;
    margin-right: 20%;
}

.bot-info {
    text-align: left;
    margin-left: 0;
}

.stChatInput {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: white;
    padding: 1rem;
    border-top: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

def initialize_workflow():
    """Initialize the workflow once and cache it."""
    try:
        with st.spinner("Initializing Wedding Planner workflow..."):
            workflow = build_workflow()
        return workflow
    except Exception as e:
        st.error(f"Failed to initialize workflow: {str(e)}")
        logger.error(f"Workflow initialization error: {traceback.format_exc()}")
        return None

def display_chat_history():
    """Display chat history in a chat-like interface."""
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    if 'chat_history' in st.session_state and st.session_state.chat_history:
        for i, (user_msg, bot_msg, intent, thread_id) in enumerate(st.session_state.chat_history):
            # User message
            st.markdown(f'<div class="user-message">👤 {user_msg}</div>', unsafe_allow_html=True)
            
            # Bot message
            st.markdown(f'<div class="bot-message">🤖 {bot_msg}</div>', unsafe_allow_html=True)
            
            # Message info
            st.markdown(f'<div class="message-info bot-info">Intent: {intent} | Thread: {thread_id}</div>', unsafe_allow_html=True)
            
            # Add some spacing between conversations
            if i < len(st.session_state.chat_history) - 1:
                st.markdown('<hr style="border-color: #4c566a; margin: 1rem 0;">', unsafe_allow_html=True)
    else:
        st.markdown('<div class="bot-message">🤖 Hello! How can I assist you with your wedding planning today?</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def process_query(query, thread_id):
    """Process the user query through the workflow with memory."""
    
    try:
        # Get existing conversation history from session state
        if 'conversation_messages' not in st.session_state:
            st.session_state.conversation_messages = []
        
        # Create initial state with existing conversation history
        initial_state = {
            "query": query,
            "intent": "",
            "response": "",
            "messages": st.session_state.conversation_messages.copy()  # Start with existing history
        }
        
        # Create thread config for checkpointer
        thread_config = {"configurable": {"thread_id": thread_id}}
        
        # Invoke workflow - agents will append to messages directly
        result = st.session_state.workflow.invoke(initial_state, config=thread_config)
        
        # Update session state with the new conversation history
        st.session_state.conversation_messages = result['messages']
        
        # Extract response and intent
        intent = result.get("intent", "unknown")
        response = result.get("response", "No response generated")
        
        return response, intent
        
    except Exception as e:
        logger.error(f"Query processing error: {traceback.format_exc()}")
        return f"Sorry, I encountered an error: {str(e)}", "error"

def main():
    # Header
    st.markdown('<h1 class="main-header">💍 Wedding Planner Chatbot</h1>', unsafe_allow_html=True)
    
    # Initialize workflow
    if 'workflow' not in st.session_state:
        st.session_state.workflow = initialize_workflow()
    
    if st.session_state.workflow is None:
        st.error("⚠️ Could not initialize the workflow. Please check your configuration.")
        return

    # Initialize chat history and thread_id
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    if 'conversation_messages' not in st.session_state:
        st.session_state.conversation_messages = []
    
    if 'thread_id' not in st.session_state:
        st.session_state.thread_id = str(random.randint(1000, 9999))

    # Display chat history
    st.markdown("")  # Minimal spacing
    display_chat_history()
    
    # Chat input
    user_input = st.chat_input("Ask about your wedding...")
    
    # Process new message
    if user_input:
        # Show processing spinner
        with st.spinner("🤖 Thinking..."):
            # Process query with memory (same thread_id for conversation continuity)
            bot_response, intent = process_query(user_input, st.session_state.thread_id)
        
        # Add to chat history
        st.session_state.chat_history.append((user_input, bot_response, intent, st.session_state.thread_id))
        
        # Rerun to update the display
        st.rerun()

if __name__ == "__main__":
    main()