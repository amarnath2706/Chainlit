import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import instruction

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

#user_message = "Please provide me the menu"



def ask_bot(user_message):
    messages=[{"role": "system", "content":instruction},
         {"role": "user", "content":user_message}]
    #llm=ChatGoogleGenerativeAI(model="gemini-pro")
    llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    responses=llm.invoke(messages)
    return responses

"""if __name__=="__main__":
    user_message = "hi how are you?"
    responses = ask_bot(user_message)
    print(responses.content)"""


