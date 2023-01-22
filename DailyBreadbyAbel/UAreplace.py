import re, subprocess
import openConfig, updateFW

def getRealUA(d, b, n):
  grepStr = 'user_agent.*'
  userAg = subprocess.check_output("yts test %s ' ' --json-output=/tmp/tmp_%s.json" % (d[n][b]["ip"], n), shell=True) 
  userAg = subprocess.check_output("grep '%s' /tmp/tmp_%s.json" % (grepStr, n), shell=True) 
  userAg = userAg.decode('UTF-8')[14:len(userAg)-2]
  return userAg 

def replace(data, b, n):
  """
  Uses getRealUA to get its UA from device and modify it by changing the firmware, brand, and model
  """
  userAgent = getRealUA(data, b, n)
  new = re.findall(r"\([a-zA-Z0-9].+?\)", userAgent)
  if re.match("^\(%s," % (b), new[2], re.IGNORECASE):
    if b == "google" or "insignia": 
        userAgent = re.sub(" com.*$", "", userAgent) 
    last_char_index = userAgent.rfind("/")
    newUA = userAgent[:last_char_index+1]+updateFW.getDevVer()+" "+data[n][b]['UA']
  print(replace)

