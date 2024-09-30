from typing import Annotated

import status

from .src import *
from .fakeentry import *
from fastapi import FastAPI, Depends, status

app = FastAPI()


def get_settings():
    return Settings()


@app.post("/markey")
async def request(data: RequestModel, credenciales: Annotated[Settings, Depends(get_settings)]):
    request = ProcessOrganizer(data.dni, credenciales)
    return request.validate_data()

@app.get("/llamador", status_code=status.HTTP_204_NO_CONTENT)
def fake_entry(consultorio: str, display: str, token: str, nombre: str = "", turno: str = "",
               server: str = "debqclients") -> None:
    display = DisplayParser().parse(pantallas=display)
    Debmedia().fake_entry(consultorio=consultorio, token=token, pantallas=display, paciente=nombre, turno=turno,
                          server=server)
