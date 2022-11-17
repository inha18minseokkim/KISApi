import requests.json
import json
URL_BASE = "https://openapivts.koreainvestment.com:29443"
PATH = "uapi/domestic-stock/v1/trading/order-cash"
URL = f"{URL_BASE}/{PATH}"
class TraderModule:
    def __init__(self,apikey,apisecret,token,cano,acnt):
        self.apikey = apikey
        self.apisecret = apisecret
        self.token = token
        self.cano = cano
        self.acnt = acnt
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
        return res.json()
        