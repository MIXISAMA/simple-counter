import os
import aiofiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import PlainTextResponse

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def _():
    async with aiofiles.open('count.txt', mode='r+') as file:
        contents = await file.read()
        count = int(contents) + 1
        await file.seek(0, os.SEEK_SET)
        await file.write(str(count))
    # return str(count)
    return count

