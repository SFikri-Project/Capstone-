import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(
    api_key=API_KEY
)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]
model = genai.GenerativeModel(
    model_name='gemini-pro'
    )
chat = model.start_chat(history=[])
instruction = "Awali percakapan dengan memperkenalkan bahwa diri anda adalah MateBot dan siap untuk menanggapi cerita atau perasaan hati pengguna untuk memperbaiki moodnya.  "

while(True):
    question = input("Kamu: ")

    if(question.strip() == ''):
        break

    response = chat.send_message(question)
    print('\n')
    print(f"MateBot: {response.text}")
    print('\n')
    instruction = ''