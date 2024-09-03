import json
import requests



class MarkeyAPI:
    def __init__(self, credenciales):
        self.url = credenciales.MARKEY_URL
        self.token = credenciales.MARKEY_TOKEN
        self.apikey = credenciales.MARKEY_API_KEY

    def getResponse(self, dni):
        return requests.request("GET", self.url, headers=self.__getHeaders(), data=self.__getPayload(dni)).json()

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
