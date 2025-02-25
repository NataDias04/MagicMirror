import openai
import pygame
import os
import time
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def gerar_audio(texto):
    """ Usa a API da OpenAI para converter texto em fala e reproduzir """
    try:
        response = openai.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=texto
        )

        filename = "resposta.mp3"
        
        with open(filename, "wb") as f:
            f.write(response.content)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()
        os.remove(filename)

    except Exception as e:
        print(f"Erro ao gerar áudio: {e}")
