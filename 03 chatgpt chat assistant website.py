import openai
    # """
    # # The above code defines a function called `CustomChatGPT` that uses OpenAI's GPT-3.5-turbo model to
    # # generate responses in a chat-like conversation. The function takes user input as an argument and
    # # returns a response generated by the model. The conversation history is stored in the `messages`
    # # list, which is updated with each user input and model response. The `gradio` library is used to
    # create a user interface for interacting with the chatbot.
    # 
    # # :param user_input: The user_input parameter represents the input message from the user. It is the
    # text that the user enters to communicate with the chatbot
    # # :return: The code is creating a chatbot interface using the Gradio library. The `CustomChatGPT`
    # # function takes user input, appends it to the `messages` list, and sends it to the OpenAI Chat API to
    # # get a response. The response is then appended to the `messages` list and returned as the output of
    # the function.
    # """
import gradio

# openai.api_key = "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"
# The line `openai.api_key =  "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"` is setting the
# API key for the OpenAI API. The API key is used to authenticate and authorize access to the OpenAI
# services. It allows the code to make requests to the OpenAI Chat API and retrieve responses from the
# GPT-3.5-turbo model.
# 
# openai.api_key =  "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"
# openai.api_key = "sk-pCHM1WYt1Ivr4keV3vidT3BlbkFJzTnGfTepX1Cx2yuwATvmP"
openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)