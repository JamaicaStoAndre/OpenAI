import openai
openai.api_key = "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"
response = openai.Image.create_edit(
    image=open('userMetaverso.png','rb'),
    mask=open('Imagem-com-a-mascara.png','rb'),
    prompt='crie uma imagem com uma avião grande',
    size='512x512',
    n=1,
    response_format='url'
)
print(response['data'][0]['url'])
