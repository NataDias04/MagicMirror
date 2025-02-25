import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def responder(pergunta, emocao):
    """ Envia a pergunta para a OpenAI e retorna a resposta ajustada à emoção """
    prompt = f"Usuário parece {emocao}. Responda de forma apropriada. Pergunta: {pergunta}"
    try:
        resposta = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        print(f"Erro ao obter resposta: {e}")
        return "Desculpe, ocorreu um erro."
