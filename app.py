import torch 
from dotenv import find_dotenv, load_dotenv
from langchain import PromptTemplate, LLMChain, OpenAI
from transformers import pipeline
import requests, os



load_dotenv(find_dotenv())

"""image to text model"""
def image2text(url):
    image_to_text = pipeline('image-to-text', model="Salesforce/blip-image-captioning-base")

    text= image_to_text(url)[0]['generated_text']
    print(text)
    return text


image2text('montreal.jpg')

def generate_story(scenario):


    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": "Can you please let us know more details about your ",
    })