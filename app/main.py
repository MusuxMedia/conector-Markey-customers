from .src import *

from fastapi import FastAPI

app = FastAPI()


def get_settings():
    return Settings()


@app.post("/markey")
async def request(data: RequestModel):
    request = ProcessOrganizer(data.dni, get_settings())
    return request.validate_data()
