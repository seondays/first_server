from typing import Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class Item(BaseModel):
    actionMethod : Optional[dict] = None
    userInfo : Optional[dict] = None
    taskEntities : Optional[dict] = None
    userVariables : Optional[dict] = None


app = FastAPI()


@app.post("/")
async def create_item(item: Item):
    
    item_dict = item.dict()
    
    data = [
    {
      "variableName": "P001",
      "value": "echo_"
    },
    {
      "variableName": "P002",
      "value": "변수"
    },
    {
      "variableName": "P003",
      "value": "3개월"
    }
  ]

    userVariable = [
    {
      "name": "wel",
      "value": "1",
      "type": "TEXT",
      "action": "EQ",
      "valueType": "TEXT"
    },
    {
      "name": "Q45",
      "value": "true",
      "type": "TEXT",
      "action": "EQ",
      "valueType": "TEXT"
    },
    {
      "name": "Q47",
      "value": "true",
      "type": "TEXT",
      "action": "EQ",
      "valueType": "TEXT"
    },
    {
      "name": "SM51_2",
      "value": "대화2",
      "type": "TEXT",
      "action": "EQ",
      "valueType": "TEXT"
    },
    {
      "name": "SM51_3",
      "value": "대화3",
      "type": "TEXT",
      "action": "EQ",
      "valueType": "TEXT"
    },
    {
      "name": "SM51_4",
      "value": "대화4",
      "type": "TEXT",
      "action": "EQ",
      "valueType": "TEXT"
    },
    {
      "name": "SM51_5",
      "value": "대화5",
      "type": "TEXT",
      "action": "EQ",
      "valueType": "TEXT"
    }

  ]
    
    item_dict.update({"data":data, "userVariable":userVariable})
    return item_dict

