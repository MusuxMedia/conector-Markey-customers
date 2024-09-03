import json
import requests
from fastapi import status, HTTPException


class MarkeyAPI:
    def __init__(self, credenciales):
        self.url = credenciales.MARKEY_URL
        self.token = credenciales.MARKEY_TOKEN
        self.apikey = credenciales.MARKEY_API_KEY

    def getResponse(self, dni):
        try:
            return requests.request("GET", self.url, headers=self.__getHeaders(), data=self.__getPayload(dni)).json()
        except requests.exceptions.RequestException:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token o APIKey de Markey incorrecta")

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
