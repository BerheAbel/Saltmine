import subprocess

#install oauth2l github.com/google/oauth2l so that token isn't forgotten
#copy over secret.json for api call

#information about api call to update: http://google3/google/internal/youtube/saltmine/v2/saltmine_service.proto;l=469;rcl=417908507

#Command to auth refresh
#~/go/bin/oauth2l header --json ~/Downloads/secret.json https://www.googleapis.com/auth/device-certification.frontend email

def freshPlan(data):
    """
    Refreshes test plan for every device in config.json file; The subprocess.run command has a check=True flag enabled to restrict continuation of script if one of the devices fails to refresh
    """
    for n in range(len(data)):
      for key in (data[n]):
        program = "ATV" if data[n][key]["ip"][0:3] == "adb"  else "CE"
        subprocess.run("""curl -X PATCH -H "$(~/go/bin/oauth2l header --json /home/doughfactory/Downloads/secret.json https://www.googleapis.com/auth/device-certification.frontend email --refresh)" https://autopush-saltmine-pa.sandbox.googleapis.com/v2/testPlans/%s -H "Content-Type: application/json" -d '{"device_series":"deviceSeries/%s", "certification_program":"%s"}'""" % (data[n][key]["testPlan"], data[n][key]["deviceID"], program), shell=True, check=True)
        
