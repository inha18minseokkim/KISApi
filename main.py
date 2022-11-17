from fastapi import FastAPI
from pydantic import BaseModel
from User import UserInfo
from Trader import TraderModule
app = FastAPI()


        
@app.get("/")
async def hello():
    return "Hello World!"

@app.post("/buyStock/{code}/{quantity}")
async def buyStock(code:str,quantity:int,item: UserInfo):
    print(item)
    print(code,quantity)
    tm = TraderModule(item)
    res = tm.buy(code,quantity)
    return res

@app.post("/sellStock/{code}/{quantity}")
async def sellStock(code:str,quantity:int,item: UserInfo):
    print(item)
    print(code,quantity)
    tm = TraderModule(item)
    res = tm.sell(code,quantity)
    return res
@app.get("/accountInfo")
async def getaccountInfo():
    return ""