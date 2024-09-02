from .src import *

from fastapi import FastAPI

app = FastAPI()


@app.post("/markey")
async def request(data: RequestModel):
    request = ProcessOrganizer(data.dni)
    return request.validate_data()
