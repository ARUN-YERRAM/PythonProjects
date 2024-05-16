# import openai

# # openai.api_key = "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"

# # openai.api_key = "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"

# # openai.api_key = "sk-pCHM1WYt1Ivr4keV3vidT3BlbkFJzTnGfTepX1Cx2yuwATvmP"
# openai.api_key = "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"

# messages = []
# system_msg = input("What type of chatbot would you like to create?\n")
# messages.append({"role": "system", "content": system_msg})

# print("Your new assistant is ready!")
# while input != "quit()":
#     message = input()
#     messages.append({"role": "user", "content": message})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages)
#     reply = response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": reply})
#     print("\n" + reply + "\n")


import openai
from gtts import gTTS
import os

import pyttsx3

# def speak(text):
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()
# Set your OpenAI API key

# openai.api_key = "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"
# openai.api_key = "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"

# openai.api_key = "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"

# openai.api_key = "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"


# openai.api_key = "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"

openai.api_key = "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"

# openai.api_key = "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"

# Initialize the messages list
messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")

while True:
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    # def speak(reply):
        # engine = pyttsx3.init()
        # engine.say(text)
        # engine.runAndWait()
        
        # Print the response
    print("\n" + reply + "\n")

    # Convert the response to speech and play it
    tts = gTTS(text=reply, lang="en")
    tts.save("assistant_response.mp3")
    os.system("mpg123 assistant_response.mp3")  # You need to install mpg123 or use another player

    # def speak(reply):
        # engine = pyttsx3.init()
        # engine.say(text)
        # engine.runAndWait()


    # Delete the temporary audio file
    os.remove("assistant_response.mp3")

    # Check if the user wants to quit
    if message == "quit()":
        break
