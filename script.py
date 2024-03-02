import datetime
import platform 

artifact_file = "artifact.txt"

with open(artifact_file, "w") as f:
    f.write("DATE/TIME: " + str(datetime.datetime.now())+"\n")
    f.write("OS INFO: " + str(platform.system())+str(platform.version())+"\n")