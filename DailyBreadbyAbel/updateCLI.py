import os

def update():
  """
  Updates CLI to YTS nightly build
  """
  os.chdir("/home/doughfactory/") 
  os.system("curl -O -L https://dev.yts.devicecertification.youtube/yts_server.zip; rm -rf yts_server; unzip yts_server.zip -d yts_server")
