#PNG com menos de 4Mb, com a mesma lagura e altura
import openai
import base64
from IPython.display import display
from PIL import Image

#Chave de autenticação
openai.api_key = "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"
response = openai.Image.create(
    prompt='crie uma imagem do sobre um usuário utilizando o metaverso',
    size='512x512',
    n=1,
    response_format='b64_json'
)
#recebe a resposta
imagem = response['data'][0]['b64_json']
#transforma em imagem
imagem = base64.b64decode(imagem)

with open('userMetaverso.png', 'wb') as f:
    f.write(imagem)

display(Image.open('userMetaverso.png'))
