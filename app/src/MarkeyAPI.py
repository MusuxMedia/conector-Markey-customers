import json
import requests
from fastapi import status, HTTPException


class MarkeyAPI:
    def __init__(self, credenciales):
        self.url = credenciales.MARKEY_URL
        self.token = credenciales.MARKEY_TOKEN
        self.apikey = credenciales.MARKEY_API_KEY

    def getResponse(self, dni):
        r =requests.request("GET", self.url, headers=self.__getHeaders(), data=self.__getPayload(dni))
        if r.status_code != 200:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token o Apikey de Markey Incorrecta")
        return r.json()


    def __getHeaders(self):
        return {
            'token': self.token,
            'Content-Type': 'application/json'
        }

    def __getPayload(self, dni):
        return json.dumps({
            "aplicacion": "HUAHIS",
            "operacion": "apiObtenerPaciente",
            "apiKey": self.apikey,
            "filtro": {
                "persNroDocumento": dni
            }
        })
