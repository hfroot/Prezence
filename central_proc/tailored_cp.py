import os
import time
from interruptingcow import timeout

# this central processor is tailored to the modules we are expecting.
# the modules to read:
    # speed
    # accuracy
    # volume
    # head gaze
    # gestures

# fuction: configure
def configure(metrics):
    # this reads the configure file to set the thresholds for the metrics
    outputDir = 'output/'
    configFile = open(os.path.dirname(os.path.realpath(__file__))+'/config.txt', 'r')
    for line in configFile:
        configData = line.rstrip('\n').split()
        m = configData[0]
        metrics[m]["file"] = open(outputDir+m+".txt", 'r')
        i = 1
        while i < len(configData):
            metrics[m][configData[i]] = configData[i+1]
            print m+" "+configData[i]+" "+metrics[m][configData[i]]
            i += 2
    configFile.close()

# function: makeFeedbackDecision
def makeFeedbackDecision(metrics, concerningData):
    # this function analyses concerningData to determine the best feedback to give
    print "need to make a decision"
    expireTime=4
    for m, info in concerningData.iteritems():
        if(info['timestamp']-)
        # it compares the data to the allowance and priority given in config
        # it finds the item that is the greatest outside the allowance and has the highest priority and flags this
    # at the end, the flagged data is used to look up the correct response from the feedbackMap and writes to the file

# function: giveKineticFeedback
def giveKineticFeedback(syncFile, metrics, historicalData):
    # this function givesKineticFeedback based on the inputs
    concerningData = historicalData # there won't be any data at this point so it's fine
    stop = False
    # while not told to stop:
    while not stop:
        concern = False
        for m, info in metrics.iteritems():
            # then reads in the latest data for all the files
            f = info['file']
            where = f.tell()
            line = f.readline()
            if not line or line in ['\n', '\r\n']:
                time.sleep(1)
                f.seek(where)
            else:
                # saves this data for historical record
                data = line.rstrip('\n').split()
                historicalData[m].append(data[1])
                # checks it against thresholds, adds to concerningData if a problem
                maybeAppend = {"timestamp": data[0], "data": data[1]}
                if "min" in metrics[m]:
                    if float(data[1]) < metrics[m]['min']:
                        concern = True
                        concerningData[m].append(maybeAppend)
                        print "concerningly low"
                if "max" in metrics[m]:
                    if float(data[1]) < metrics[m]['max']:
                        concern = True
                        concerningData[m].append(maybeAppend)
                        print "concerningly high"
        if concern:
            makeFeedbackDecision(metrics, concerningData)
        # check if sync has said to stop
        swhere = syncFile.tell()
        sline = syncFile.readline()
        if not line or line in ['\n', '\r\n']:
            time.sleep(1)
            syncFile.seek(where)
        else:
            if line.rstrip('\n') == "stop":
                stop = True

# function: givePostFeedback
    # this function aggregates the historical data
    # then fills in string templates with the relevant data
    # and writes these strings to file

# function: main
def main():
    # this function is the main control
    metrics = {
        "speed": {},
        "accuracy": {},
        "volume": {},
        "head_gaze": {}
        # "gestures": {}
    }
    historicalData = {
        "speed": [],
        "accuracy": [],
        "volume": [],
        "head_gaze": []
        # "gestures": []
    }
    feedbackMap = {
        "head_gaze_low": 1,
        "gestures_high": 2,
        "posture_low": 3,
        "accuracy_low": 4,
        "speed_high": 5,
        "volume_high": 7,
        "speed_low": 6,
        "volume_low": 8
    }

    maxtime = 30 # in seconds
    try: # do the following unless maxtime is reached:
        with timeout(maxtime, exception=RuntimeError):
            # it calls configure, passing in the metrics structure
            configure(metrics)
            start = False
            syncFile = open('output/sync.txt', 'r')
            while not start:
                # read sync
                where = syncFile.tell()
                line = syncFile.readline()
                if not line or line in ['\n', '\r\n']:
                    time.sleep(1)
                    syncFile.seek(where)
                else:
                    if line.rstrip('\n') == "start":
                        start = True
            print "starting"
            giveKineticFeedback(syncFile, metrics, historicalData)
    except RuntimeError:
        print "Stopping: run time exceeded "+str(maxtime)+" seconds"
        pass

    syncFile.close()
    # givePostFeedback(historicalData)

main()
