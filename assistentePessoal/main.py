from reconhecimento import ouvir_comando
from emocao import detectar_emocao, gerar_mensagem
from audio import gerar_audio
from chat import responder
import time

def modo_assistente():
    """ Executa o assistente pessoal ativado por comando de voz """
    print("Assistente ativado! Diga 'espelho' para iniciar e 'sair' para encerrar.")

    while True:
        comando = ouvir_comando()
        if comando == "espelho":
            print("Assistente pronto! Faça sua pergunta.")
            gerar_audio("Estou ouvindo.")

            while True:
                comando = ouvir_comando()
                if comando:
                    if comando == "sair":
                        print("Encerrando assistente. Até mais!")
                        gerar_audio("Encerrando assistente. Até mais!")
                        return
                    elif comando == "analisar":
                        emocao = detectar_emocao()
                        mensagem = gerar_mensagem(emocao)
                        print(f"Assistente: {mensagem}")
                        gerar_audio(mensagem)
                    else:
                        resposta = responder(comando, "neutral")
                        print(f"Assistente: {resposta}")
                        gerar_audio(resposta)

def main():
    modo_assistente()
    print("Programa encerrado.")

if __name__ == "__main__":
    main()