from typing import Annotated


from .conector import *
from .fakeentry import *
from fastapi import FastAPI, Depends, status

app = FastAPI()


def get_settings():
    return Settings()


@app.post("/markey")
async def request(data: RequestModel, credenciales: Annotated[Settings, Depends(get_settings)]):
    request = ProcessOrganizer(data.dni, credenciales)
    return request.validate_data()

@app.get("/llamador", status_code=status.HTTP_200_OK)
def fake_entry(consultorio: str, display: str, token: str, turno: str,
               server: str = "debqclients") -> None:
    display = DisplayParser().parse(pantallas=display)
    return Debmedia().fake_entry(consultorio=consultorio, token=token, pantallas=display, turno=turno,
                          server=server)

