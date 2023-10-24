import os
import openai
import PDFreader

openai.api_key = os.getenv("OPENAI_API_KEY")

def respond35(question):
  response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=question,
    max_tokens=100
  )

  return response['choices'][0]['text']

def respond4(question):
  response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": question}
    ])

  return (response['choices'][0]['message']['content'])


