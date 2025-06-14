from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")
model=ChatOpenAI(model="gpt-4o-mini",api_key=api_key , max_completion_tokens=2)

response=model.invoke("What is the capital of Pakistan tell in single word")
print(response.content)