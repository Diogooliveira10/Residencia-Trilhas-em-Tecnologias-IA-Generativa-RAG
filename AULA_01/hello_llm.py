import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv('OPENAI_MODEL')
)

# Usa o modelo definido no .env ou um valor padrão
modelo = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {"role": "user", "content": "Qual a capital do Brasil?"}
    ],
    store=True,
)

print(response.choices[0].message.content)
