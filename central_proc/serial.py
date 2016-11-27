import os
import time
from interruptingcow import timeout
TIMEOUT = 60

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

def readFiles(outputs):
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
            if line.rstrip('\n') == "stop":
                return 1
            if "checkType" in info:
                checkType = info["checkType"]
                if checkType == "min":
                    if float(line.rstrip('\n')) < info["data"]:
                        print name+" is too low!"
                elif checkType == "inRange":
                    if float(line.rstrip('\n')) < info["data"][0] or float(line.rstrip('\n')) > info["data"][1]:
                        print name+" is out of range!"
    return 0

def main():
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
    # using solution given by andresfp to add a timeout: http://stackoverflow.com/a/13293360/3845770
    try:
        with timeout(TIMEOUT, exception=RuntimeError):
            stop = 0
            while not stop: # safety to stop loop
                stop = readFiles(outputs)
            print "Stopping: Module called for stop"
    except RuntimeError:
        print "Stopping: timeout (greater than "+str(float(TIMEOUT/60))+" minutes)"
        pass

    for name, info in outputs.iteritems():
        info["file"].close()
    return 0

main()