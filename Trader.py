import requests
import json
from loguru import logger
from User import UserInfo
URL_BASE = "https://openapivts.koreainvestment.com:29443"
PATH = "uapi/domestic-stock/v1/trading/order-cash"
URL = f"{URL_BASE}/{PATH}"
class TraderModule:
    def __init__(self, userinfo : UserInfo):
        self.apikey = userinfo.apikey
        self.apisecret = userinfo.apisecret
        self.token = userinfo.token
        self.cano = userinfo.cano
        self.acnt = userinfo.acnt
        logger.debug(f"{self.apikey} {self.apisecret} \n {self.token} \n {self.cano} {self.acnt} 생성 완료")
    def buy(self,code: str,quantity: int):
        global URL
        headers = {"Content-Type":"application/json", 
           "authorization":f"Bearer {self.token}",
           "appKey": self.apikey,
           "appSecret":self.apisecret,
           "tr_id":"VTTC0802U",
           "custtype":"P",
           }
        data = {
            "CANO": self.cano,
            "ACNT_PRDT_CD": self.acnt,
            "PDNO": code,
            "ORD_DVSN": "01",
            "ORD_QTY": str(quantity),
            "ORD_UNPR": "0",
        }
        res = requests.post(URL, headers=headers, data=json.dumps(data))
        logger.debug(f"{res.json()}")
        return res.json()
    def sell(self,code: str,quantity: int):
        global URL
        headers = {
            "Content-Type":"application/json", 
           "authorization":f"Bearer {self.token}",
           "appKey": self.apikey,
           "appSecret": self.apisecret,
           "tr_id":"VTTC0801U",
           "custtype":"P",
           }
        data = {
            "CANO": self.cano,
            "ACNT_PRDT_CD": self.acnt,
            "PDNO": code,
            "ORD_DVSN": "01",
            "ORD_QTY": str(quantity),
            "ORD_UNPR": "0",
        }
        res = requests.post(URL, headers=headers, data=json.dumps(data))
        logger.debug(f"{res.json()}")
        return res.json()

if __name__ == "__main__":
    tm = TraderModule("PSIDcUD8nfSa8FyG7UkM9QxY4vS2u5rBBTaY",
                      "h9fkvIHeX8IP97+WmySbme5g5yuuSrq/LjBeFBMfcZF6e3XShxb+o28nATtQIoYfqDpbiTKBgVI/qoFA/10GtvrWSjKVh5IpSdVqyhbC3ZR3MjOpvyl3T+x2xzOG92t1Xl+ek2ZXcnZpyKB57SLkFCuAFhZIe8X7NJcs2Y0RcFeUNGJrBMo=",
                     "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6IjljNzkwZDJlLTk2NjktNGY5OC1hNTFjLTUzMzY0YjM3YjU3NyIsImlzcyI6InVub2d3IiwiZXhwIjoxNjY4NzcxMDM5LCJpYXQiOjE2Njg2ODQ2MzksImp0aSI6IlBTSURjVUQ4bmZTYThGeUc3VWtNOVF4WTR2UzJ1NXJCQlRhWSJ9.Z4fgGnqQAgXOT0dgmLg0m53hThDHxPynkdEDrEgLDf7SoqmeYPQ_gavg2GNwjflJ16itHGLybJe57BBdX3i8Ow","50071508","01")
    print(tm.buy("005930",1))