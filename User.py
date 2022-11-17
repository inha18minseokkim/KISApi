from pydantic import BaseModel
class UserInfo(BaseModel):
    apikey: str
    apisecret: str
    token: str
    cano: str
    acnt: str