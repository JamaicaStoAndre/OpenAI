import openai

class MyOpenAi:
    def __int__(self, prompt, model, n, maxtokens, temperature, key):
        self.prompt = prompt
        self.model = model
        self.n = n
        self.maxtokens = maxtokens
        self.temperature = temperature
        openai.api_key = self.key

    def callgpt(self):
        response = openai.Completion.create(
            model=self.model,
            prompt=self.prompt,
            temperature=self.temperature,
            max_tokens=self.maxtokens,
            n=self.n,
        )
        resposta = []
        for a in range(len(response.choices)):
            resposta.append(response.choice[a].text)
            return resposta
