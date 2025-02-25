from flask import Flask, request, jsonify
from flask_cors import CORS
from reconhecimento import ouvir_comando
from emocao import detectar_emocao, gerar_mensagem
from audio import gerar_audio
from chat import responder

app = Flask(_name_)  # Correção aqui
CORS(app)  # Permite chamadas do frontend

assistente_ativo = False  # Estado do assistente

@app.route('/ativar', methods=['POST'])
def ativar_assistente():
    """Ativa o assistente"""
    global assistente_ativo
    assistente_ativo = True
    return jsonify({"status": "Assistente ativado"}), 200

@app.route('/desativar', methods=['POST'])
def desativar_assistente():
    """Desativa o assistente"""
    global assistente_ativo
    assistente_ativo = False
    return jsonify({"status": "Assistente desativado"}), 200

@app.route('/comando', methods=['POST'])
def processar_comando():
    """Processa comandos enviados pelo frontend"""
    if not assistente_ativo:
        return jsonify({"status": "Assistente inativo"}), 400

    data = request.json
    comando = data.get("comando", "").lower()

    if not comando:
        return jsonify({"erro": "Comando vazio"}), 400

    if comando == "sair":
        desativar_assistente()
        return jsonify({"resposta": "Assistente desligado"}), 200

    elif comando == "analisar":
        emocao = detectar_emocao()
        mensagem = gerar_mensagem(emocao)
        gerar_audio(mensagem)
        return jsonify({"resposta": mensagem, "emocao": emocao}), 200

    else:
        resposta = responder(comando, "neutral")
        gerar_audio(resposta)
        return jsonify({"resposta": resposta}), 200

@app.route('/estado', methods=['GET'])
def estado_assistente():
    """Retorna o estado do assistente"""
    return jsonify({"assistente_ativo": assistente_ativo})

if _name_ == '_main_':  # Correção aqui
    app.run(debug=True, host='0.0.0.0', port=5000)