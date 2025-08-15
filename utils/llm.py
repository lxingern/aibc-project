import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

if load_dotenv('.env'):
  OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
else: 
  OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

client = OpenAI(api_key=OPENAI_API_KEY)

def get_completion(prompt, model='gpt-4o-mini', temperature=0, top_p=1.0, max_tokens=1024, n=1):
  messages = [{'role': 'user', 'content': prompt}]
  response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature,
    top_p=top_p,
    max_tokens=max_tokens,
    n=1
  )
  return response.choices[0].message.content