import json
from fastapi import HTTPException
import requests





class Debmedia:
    def fake_entry(self, consultorio: str, token: str, pantallas: list[int], server: str,
                   turno: str = ""):
        url = self.validar_url(server)

        payload = self.__get_payload(screen_ids=pantallas, turno=turno, puesto=consultorio)
        headers = {
            'x-api-key': token,
            'Content-Type': 'application/json'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except requests.RequestException:
            raise HTTPException(status_code=404, detail="Server Incorrecto")
        self.validar_response(response)
        return self.llamadorResponse(turno=turno, consultorio=consultorio)

    def __get_payload(self, screen_ids: list[int], turno: str, puesto: str):
        return json.dumps({
            "screen.ids": screen_ids,
            "column2": puesto,
            "column0": turno,
        })

    def validar_response(self, response: requests.Response):
        if response.status_code == 401:
            raise HTTPException(status_code=401, detail="Token incorrecto")

    def validar_url(self, server: str):
        return f"https://{server}.debmedia.com/api/screen/fakeentry"

    def llamadorResponse(self, turno:str, consultorio:str):
        return  {f"nombrePaciente":turno,"consultorio":consultorio,"resultado":"OK"}
