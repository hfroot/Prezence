import os
import time

# output data structure:
# name of output (eg speech_speed), file, check type (eg "min", "inRange", "dict"?), data
# outputs = {
#     "speech_speed": {
#         "file": opened file from files txt,
#         "checkType": from config,
#         "data": from config
#     },
#     "speech_accuracy": {...}
# }

# set up outputs dictionary
outputs = {}
outputDir = 'dummy_programs/output/'
configFile = open(os.path.dirname(os.path.realpath(__file__))+'/config.txt', 'r')
for config in configFile:
    config = config.split()
    name = config[0]
    outputs[name] = { "file": open(outputDir+name+'.txt', 'r') }
    if len(config) > 1:
        outputs[name]["checkType"] = config[1]
        if config[1] == "inRange":
            outputs[name]["data"] = [config[2], config[3]]
        else:
            outputs[name]["data"] = config[2]
configFile.close()

# read and check outputs
i = 0
while i < 10: # safety to stop loop
    for name, info in outputs.iteritems():
        # the following inspired by the soln: http://code.activestate.com/recipes/157035-tail-f-in-python/
        f = info["file"];
        where = f.tell()
        line = f.readline()
        if not line or line in ['\n', '\r\n']:
            time.sleep(1)
            f.seek(where)
        else:
            print name+': '+str(line), # already has newline
            if "checkType" in info:
                checkType = info["checkType"]
                if checkType == "min":
                    if float(line.rstrip('\n')) < info["data"]:
                        print name+" is too low!"
                elif checkType == "inRange":
                    if float(line.rstrip('\n')) < info["data"][0] or float(line.rstrip('\n')) > info["data"][1]:
                        print name+" is out of range!"
    i+=1

for name, info in outputs.iteritems():
    info["file"].close()

print "Finished loop"