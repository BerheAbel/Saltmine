#! /usr/bin/python3
import os, subprocess, json

# this file obsolete now

def discover():
  #have to adb connect to all the android devices too
#  subprocess.call("adb connect 192.168.1.9:5555", shell=True)
  subprocess.call("echo CLI version:; yts --version; yts discover", shell=True)
  os.chdir("/home/pi")
  try:
    jsonFile = open(".local/share/yts_server/devices.json")
    data = json.load(jsonFile)
    devices = []
    for i in data:
      deviceType = i['deviceType']
      if "location" in i:
        deviceIP = i['location'] 
      else:
        deviceIP = i['deviceId'] 
      devices.append(deviceType+':'+deviceIP)
  except:
    print('Trouble reading or opening file @ ~/.local/share/yts_server/devices.json')
  finally:
    jsonFile.close()

  return devices

