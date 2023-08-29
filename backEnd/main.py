"""

start the mariaDB database
    $ systemctl restart mariadb.service

start the redis database
    $ systemctl restart redis.service


to start the API type
    $ uvicorn main:app --reload


"""
import sys as system
from fastapi import FastAPI
import json
import redis
import mariadb

app = FastAPI()
db = redis.Redis(host='localhost', port=6379, decode_responses=True)

try:

    connection = mariadb.connect(
        user="admin",
        password="4590GSA_AdmiN!",
        host="localhost",
        port=3306,
        database="exit_logs"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    system.exit(1)

cur = connection.cursor()


@app.post("/data/redis")
def addItem(q: str, v: int):
    return {"query": addData(q, v)}


@app.get("/data/redis")
def getItem(q: str):
    return {"data": getDataValue(q)}


@app.get("/data/mariaDB")
def getDB():
    return getTable("exit_logger")


# DB funcs


# maria db (mysql)
def getTable(table: str):
    try:
        connection.reconnect()
        cur.execute("SELECT * FROM exit_logger")
        # fetch all the matching rows
        result = cur.fetchall()
        # loop through the rows
        returnResult = ""
        return result

    except mariadb.Error as error:
        return {"Error": error}


# redis
def addData(key: str, value: int):
    db.set(key, value)


def getDataValue(key: str):
    return db.get(key)


def flush():
    db.flushall()


def getKeys():
    return db.keys()
