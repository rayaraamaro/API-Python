from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API funcionando!"}

@app.get("/consulta_cep/{cep}")
async def consulta_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        return dados
    else:
        return {"erro": "Não foi possível realizar a consulta."}
