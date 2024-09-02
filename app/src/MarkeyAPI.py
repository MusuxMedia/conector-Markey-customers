import json
import requests


class MarkeyAPI:
    def __init__(self):
        self.url = "https://australQA.markey.com.ar/APIMarkeyV2/obtener"
        self.token = 'UZN9291llgxWJ93uzilrmantG6t20r0v8kwrihYXmZl1EO8irdhT0gFK0tFAlv3m'
        self.apikey = "933ec3bb-91c7-4ca5-bcdd-5220778c0f36"

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
