from reconhecimento import ouvir_comando
from emocao import detectar_emocao, gerar_mensagem
from audio import gerar_audio
from chat import responder
from spotify import tocar_musica  # Controle do Spotify por voz
import time
import re  # Para extrair nome da música e artista

def extrair_musica_artista(comando):
    """Extrai o nome da música e do artista do comando de voz."""
    padrao = re.search(r"tocar\s+(.*?)\s+de\s+(.*)", comando, re.IGNORECASE)
    
    if padrao:
        musica = padrao.group(1).strip()
        artista = padrao.group(2).strip()
        return musica, artista
    else:
        # Se não encontrar "de [artista]", tenta buscar só pelo nome da música
        musica = comando.replace("tocar", "").strip()
        return musica, None

def modo_assistente():
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
                    elif comando.startswith("tocar"):
                        musica, artista = extrair_musica_artista(comando)
                        if musica:
                            print(f"Procurando por {musica} no Spotify...")
                            resultado = tocar_musica(musica, artista)
                            if resultado:
                                gerar_audio(f"Tocando {musica}")
                            else:
                                gerar_audio(f"Não encontrei {musica}. Tente novamente.")
                        else:
                            gerar_audio("Por favor, diga o nome da música que deseja ouvir.")
                        continue
                    elif comando == "analisar":
                        emocao = detectar_emocao()
                        mensagem = gerar_mensagem(emocao)
                        print(f"Assistente: {mensagem}")
                        gerar_audio(mensagem)
                    else:
                        resposta = responder(comando, "neutral")
                        print(f"Assistente: {resposta}")
                        gerar_audio(resposta)
                
                time.sleep(1)

if __name__ == "__main__":
    modo_assistente()
