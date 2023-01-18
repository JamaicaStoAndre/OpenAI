#Lembrar de instalar o Flask e o CORS
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)
def mychat(prompt):
    openai.api_key = "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"
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=2048
    )
    return response.choices[0].text
@app.route('/chatbot')
def chatbot():
    try:
        pergunta = request.args.get('pergunta')
        resposta = mychat(pergunta)
    except Exception as e:
        resposta = '!Ops! Ocorreu um erro e não pude retornar: {}'.format(e)
    return jsonify(resposta=resposta)

app.run()
