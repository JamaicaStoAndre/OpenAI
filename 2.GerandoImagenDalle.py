from io import BytesIO
import openai
import requests
from openai import Image
from PIL import Image

#chave de autenticação
openai.api_key = "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"
response = openai.Image.create(
    prompt='crie uma imagem do supermario bross em cima do yoshi e bantendo no comelo peidao',
    size='512x512',
    n=1,
    response_format='url'
)
response = requests.get(response['data'][0]['url'])
Image.open(BytesIO(response.content))
