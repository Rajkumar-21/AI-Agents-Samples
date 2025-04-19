from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
# print("API Key:", os.environ.get("GROQ_API_KEY"))
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful AI assistant that users to answer questions and provide information.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)