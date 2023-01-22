import json, subprocess
import openConfig

def getDevVer():
  """
  Grabs current DEV version and returns it for firmware interpolation 
  """
  b = subprocess.check_output("curl https://dev.yts.devicecertification.youtube/version", shell=True)
  tVer = b.decode('UTF-8')
  return tVer

#this function obsolete now
def replaceFW(brand):
  data = openConfig.read()
  ua=""
  for n in range(len(data)):
    if brand in data[n]:
      ua=(data[n][brand]['UA'])
  ua = ua.replace("firmware", getDevVer())
  return ua

