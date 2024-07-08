def create_prompt_from_desc(product_name, product_desc, customer_name, customer_desc):
    prompt = "Create a creative personalised advertisement to be sent on Whatsapp for the product " + product_name + "with product Description as follows - " + product_desc+". The details of the customer are as follows - " + "Customer Name - " + customer_name+"Description - " + customer_desc
    prompt1 = "Generate a short creative and personalised text advertisement with emojis for product -  Coding Ninjas DSA Course,  with product description - Data Structures and Algorithms in Java for begineers and newbies. Customer Name - Samarth , Customer Interest -  Watching Cricket"
    return prompt1

from openai import OpenAI

def create_ad(prompt):

    client = OpenAI(
        api_key="<KEY_HERE>"
    )

    response = client.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt=prompt
    )

    return response