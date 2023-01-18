from myopenai import MyOpenAi
chat =  MyOpenAi('Como ajusta blocos adsense em um thema wordpress astra','text-davinci-003',1000,1,'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')
resposta = chat.callgpt()
for x in resposta:
    print(x)
