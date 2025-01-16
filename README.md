# Technical Support AI Agent 🤖

A powerful AI-powered technical support agent built with Streamlit, Gemini AI, and LangChain. This agent helps developers and technical users by providing documentation, code examples, troubleshooting assistance, and best practices.

## Features 🌟

- **Interactive Chat Interface**: Real-time conversation with the AI agent
- **Technical Documentation Search**: Find relevant documentation and API references
- **Code Examples**: Get practical implementation examples
- **Error Resolution**: Troubleshoot technical issues and debug errors
- **Conversation Memory**: Maintains context for better follow-up responses
- **User-Friendly Interface**: Clean and intuitive Streamlit-based UI

## Technologies Used 🛠️

- **Streamlit**: For the web interface
- **Google Gemini AI**: Advanced language model for understanding and generating responses
- **LangChain**: For agent orchestration and tool management
- **DuckDuckGo Search**: For real-time information retrieval
- **Python**: Core programming language

## Prerequisites 📋

- Python 3.8 or higher
- Google Gemini API key

## Installation 💻

1. Clone the repository:
```bash
git clone <repository-url>
cd customer-support
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Gemini API key:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

## Running the Application 🚀

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

## Usage Examples 📝

The agent can help with various technical queries such as:

1. **Documentation Search**:
   ```
   "How do I use Python's requests library?"
   ```

2. **Code Examples**:
   ```
   "Show me an example of async/await in Python"
   ```

3. **Error Resolution**:
   ```
   "How do I fix ModuleNotFoundError in Python?"
   ```

4. **Best Practices**:
   ```
   "What are the best practices for REST API security?"
   ```

## Project Structure 📁

```
customer-support/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
└── README.md          # Project documentation
```

## Features in Detail 🔍

### 1. Technical Documentation Search
- Searches through technical documentation
- Finds API references
- Locates programming guides

### 2. Code Support
- Provides relevant code examples
- Explains implementation patterns
- Offers best practices

### 3. Troubleshooting
- Helps debug error messages
- Suggests potential fixes
- Guides through solution implementation

### 4. Learning Resources
- Recommends tutorials
- Links to official documentation
- Suggests learning paths

## Configuration Options ⚙️

The agent can be configured through various parameters:

```python
# Model Configuration
temperature=0.7        # Controls response creativity
max_output_tokens=2048 # Maximum response length
top_p=0.8             # Nucleus sampling parameter
top_k=40              # Top-k sampling parameter
```

## Error Handling 🔧

The application includes robust error handling for:
- Invalid API keys
- Network connectivity issues
- Rate limiting
- Invalid queries

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting 🛠️

If you encounter issues:

1. Verify your API key in the `.env` file
2. Check your internet connection
3. Ensure all dependencies are installed
4. Try restarting the application

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 👏

- Google Gemini AI for the language model
- Streamlit for the web framework
- LangChain for agent capabilities
- DuckDuckGo for search functionality 