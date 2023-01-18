import openai

openai.api_key = "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"
response = openai.Image.create_variation(
    image=open('userMetaverso.png','rb'),
    #prompt='crie uma imagem do supermario bross em cima do yoshi e bantendo no comelo peidao',
    size='512x512',
    n=1,
    response_format='url'
)
print(response['data'][0]['url'])
