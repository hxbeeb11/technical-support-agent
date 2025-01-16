import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool

# Load environment variables
load_dotenv()

# Configure page settings
st.set_page_config(
    page_title="Technical Support Agent",
    page_icon="🤖",
    layout="wide"
)

# Initialize Gemini model
def init_llm():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please add it to your .env file.")
    
    llm = GoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=api_key,
        temperature=0.7,
        max_output_tokens=2048,
        top_p=0.8,
        top_k=40
    )
    return llm

# Initialize conversation memory
def init_memory():
    return ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

# Initialize custom tools
def init_tools(llm):
    # DuckDuckGo search tool for documentation and resources
    search = DuckDuckGoSearchRun()
    
    # Custom tools for specific technical domains
    tools = [
        Tool(
            name="Technical Documentation Search",
            func=search.run,
            description="Useful for finding technical documentation, API references, and programming guides. Use this when you need to find specific technical information."
        ),
        Tool(
            name="Code Example Search",
            func=search.run,
            description="Search for code examples and implementation patterns. Use this when you need to find specific coding examples or patterns."
        ),
        Tool(
            name="Error Resolution",
            func=search.run,
            description="Search for solutions to technical errors and bugs. Use this when troubleshooting specific error messages or technical issues."
        )
    ]
    
    return tools

# Initialize the agent
def init_agent():
    try:
        llm = init_llm()
        memory = init_memory()
        tools = init_tools(llm)
        
        return initialize_agent(
            tools,
            llm,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            memory=memory,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=3,
            early_stopping_method="generate"
        )
    except Exception as e:
        st.error(f"Error initializing agent: {str(e)}")
        st.error("Please check your API key and internet connection.")
        return None

# Initialize session state
if "agent" not in st.session_state:
    st.session_state.agent = init_agent()

# Main UI
st.title("🤖 Technical Support Agent")

try:
    # Initialize agent if not already initialized
    if "agent" not in st.session_state or st.session_state.agent is None:
        st.session_state.agent = init_agent()
    
    if st.session_state.agent is None:
        st.warning("Agent initialization failed. Please check your configuration and try again.")
    else:
        st.markdown("""
        This agent can:
        - Search technical documentation and resources
        - Find relevant code examples
        - Debug errors and provide solutions
        - Execute Python code to verify solutions
        - Guide you through complex technical problems
        """)

        # Chat interface
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("What technical challenge can I help you with?"):
            # Display user message
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Get agent response
            with st.chat_message("assistant"):
                with st.spinner("Working on it..."):
                    try:
                        response = st.session_state.agent.run(prompt)
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                    except Exception as e:
                        error_message = f"An error occurred: {str(e)}"
                        st.error(error_message)
                        st.session_state.messages.append({"role": "assistant", "content": error_message})

except Exception as e:
    st.error(f"Application Error: {str(e)}")
    st.markdown("""
    ### Troubleshooting Steps:
    1. Verify your API key in the `.env` file
    2. Check your internet connection
    3. Make sure you have all required dependencies installed
    4. Try restarting the application
    
    If the problem persists, please check the error message above for more details.
    """)

# Sidebar with additional information
with st.sidebar:
    st.header("Agent Capabilities")
    st.markdown("""
    This Technical Support Agent can:
    
    🔍 **Research & Documentation**
    - Search technical documentation
    - Find API references
    - Locate programming guides
    
    💻 **Code Support**
    - Find relevant code examples
    - Execute Python code
    - Verify solutions
    
    🐛 **Troubleshooting**
    - Debug error messages
    - Suggest fixes
    - Guide through solutions
    
    📚 **Learning Resources**
    - Recommend tutorials
    - Link to documentation
    - Suggest best practices
    """) 