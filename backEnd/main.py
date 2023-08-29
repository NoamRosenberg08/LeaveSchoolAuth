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
import mariadb
from DBs.RedisDB import RedisDB

app = FastAPI()
redisDB = RedisDB.__init__()

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
    return {"query": redisDB.addData(q, v)}


@app.get("/data/redis")
def getItem(q: str):
    return {"data": redisDB.getValueFromKey(q)}


@app.get("/data/mariaDB")
def getDB():
    return getTable("exit_logger")


# DB funcs


# maria db (mysql)
def getTable(table: str):
    try:
        connection.reconnect()
        cur.execute("SELECT * FROM exit_logger")

        return cur.fetchall()

    except mariadb.Error as error:
        return {"Error": error}


