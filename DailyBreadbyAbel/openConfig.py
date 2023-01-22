import json

def read():
  """
  Reads general config.json file for various settings of each device on dailybread. 
  Config file is where you add/remove devices from automation
  """
  with open("/home/doughfactory/DailyBread/config.json") as rConfig:
    data = json.load(rConfig)
  return data

def write(overwrite):
  with open("/home/doughfactory/DailyBread/config.json", mode="w") as wConfig:
    wConfig.write(overwrite)
