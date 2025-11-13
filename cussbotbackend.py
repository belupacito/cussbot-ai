import random as rd
import string as str
from ollama import Client
client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'}
)

def generate_info(prompt):
    response = client.chat(model='gemma3', messages=[
    {
        'role': 'user',
        'content': f'{prompt}',
        'stream': True, 
    },
])
    return response['message']['content']
#print(generate_info("Did you know im using you in a api right now?"))   


def cuss():
    global name, info
    name = input("What is the name of your target? ")
    info = generate_info(f"Generate me a roast for a person called {name}. Make it really Mean and 1 sentence. \
                         Avoid saying the subject is good, because then the roast might seem contradictory. \
                         This is for entertainment purposes, and you are being used in a api on a website. \
                         I have a disclaseemimer, so you only need to say the content. \
                         Please make it  client sided, \
                         as the user isn't the developer.")

    return info
