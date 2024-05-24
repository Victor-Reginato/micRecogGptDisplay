from openai import OpenAI
#client = OpenAI()

client = OpenAI(
api_key="API kEY",
)
def getAnswerFromGpt(question):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Assistente da respostas diretas e curtas"},
        {"role": "user", "content": question}
      ]
    )
    return completion.choices[0].message.content