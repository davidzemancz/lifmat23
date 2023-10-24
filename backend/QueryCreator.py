import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_query():

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {
                "role": "user", 
                "content": "Hello world"
            }
    ])
    print(completion.choices[0].message.content)
