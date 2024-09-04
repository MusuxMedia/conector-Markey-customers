from typing import Annotated

from .src import *

from fastapi import FastAPI, Depends

app = FastAPI()


def get_settings():
    return Settings()


@app.post("/markey")
async def request(data: RequestModel, credenciales: Annotated[Settings, Depends(get_settings)]):
    request = ProcessOrganizer(data.dni, credenciales)
    return request.validate_data()
