import openai
#chave de autenticação
openai.api_key = "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"
resposta = openai.Completion.create(
    model = "text-davinci-003",
    prompt = "qual o direitorio correto para ser inserido um arquivo chamado  index.html para ser exibido pelo flask? ",
    max_tokens=1000
    )
print(resposta.choices[0].text)
