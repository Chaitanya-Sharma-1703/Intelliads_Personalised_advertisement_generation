import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def answer_prompt_bard(query):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    return response.text

def create_prompt_from_description(product_name, product_desc, customer_name, customer_interests,
                                   delivery_platform="WhatsApp"):
    prompt = "Generate a detailed creative personalized according to customer's interests' short text-based advertisement to " \
             "be delivered on '" + delivery_platform + "' including emojis for the product - '" + product_name + "' with " \
                                                                                                                 " the description - '" + product_desc + "'. The advertisement is to be delivered to the customer named '" + customer_name + \
             "' whose interests are as follows - '" + customer_interests + "'. No need of Hashtags. No need of product " \
                                                                           "link. Start with response directly. "
    return prompt