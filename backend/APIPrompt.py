import os
import openai
import PDFreader

openai.api_key = os.getenv("OPENAI_API_KEY")

def respond(question):
  response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=question,
    max_tokens=50
  )

  print(response['choices'][0]['text'])

prompt=PDFreader.read_chapter(2, "test_pdfs/warfarin.pdf")
question="Jaká gramáž warfarinu je zmíněná v následujícím textu?"

# prompt="From the following text, find how many tables of paralen should I take: Paralen is medical drug. You should take 1-2 tablets of paralen. Never take more than 5 tablets."

respond(question+prompt)

