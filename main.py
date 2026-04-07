import openai
from gtts import gTTS
import os

# Coloque aqui sua chave da API da OpenAI
openai.api_key = "SUA_CHAVE_API"

def conversar_com_chatgpt(texto):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":texto}]
    )
    return resposta.choices[0].message["content"]

def falar_resposta(resposta):
    tts = gTTS(resposta, lang="pt")
    tts.save("resposta.mp3")
    os.system("start resposta.mp3")  # Windows

if __name__ == "__main__":
    pergunta = input("Digite sua pergunta: ")
    resposta = conversar_com_chatgpt(pergunta)
    print("ChatGPT:", resposta)
    falar_resposta(resposta)
