from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 

api_key=os.getenv("GOOGLE_API_KEY")
model=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

result=model.invoke("What is the capital of Pakistan")
print(result.content)
