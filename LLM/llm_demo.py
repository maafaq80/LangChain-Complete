from dotenv import load_dotenv
import os
from langchain_openai import OpenAI 

# Load environment variables from .env file
load_dotenv()

# Get your API key from the environment
api_key = os.getenv("OPEN_AI_API_KEY")

# Use it to initialize the LLM
llm = OpenAI(
    model="gpt-4o-mini",
    api_key=api_key
)

# Test the LLM (optional)
response = llm.invoke("What is the capital of Pakistan")
print(response)
