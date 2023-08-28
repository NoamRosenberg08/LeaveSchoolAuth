'''
to start the API type
    $ uvicorn main:app --reload

'''


from fastapi import FastAPI
import subprocess
import redis

app = FastAPI()
db = redis.Redis(host='localhost', port=6379, decode_responses=True)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/data/")
def addItem(q: str, v : int):
    return {"query": addData(q, v)}


@app.get("/data/")
def getItem(q: str):
    return {"data": getDataValue(q)}


# DB funcs

def addData(key: str, value: int):
    db.set(key, value)


def getDataValue(key: str):
    return db.get(key)
