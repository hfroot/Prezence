import os
import time
from interruptingcow import timeout
start_time = 0
ROBOT_DELAY = 7
lastFeedback = 0
FEEDBACK_MAP = {
    "head_gaze_low": 1,
    "gestures_high": 2,
    "posture_low": 3,
    "clarity_low": 4,
    "speed_high": 5,
    "volume_high": 7,
    "speed_low": 6,
    "volume_low": 8
}
# this central processor is tailored to the modules we are expecting.
# the modules to read:
    # speed
    # clarity
    # volume
    # head gaze
    # gestures

# fuction: configure
def configure(metrics):
    # this reads the configure file to set the thresholds for the metrics
    outputDir = 'output/'
    configFile = open(os.path.dirname(os.path.realpath(__file__))+'/config.txt', 'r', os.O_NONBLOCK)
    for line in configFile:
        configData = line.rstrip('\n').split()
        m = configData[0]
        metrics[m]["file"] = open(outputDir+m+".txt", 'r', os.O_NONBLOCK)
        i = 1
        while i < len(configData):
            metrics[m][configData[i]] = float(configData[i+1])
            # print m+" "+configData[i]+" "+configData[i+1]
            i += 2
    configFile.close()

# function: makeFeedbackDecision
def makeFeedbackDecision(metrics, concerningData, feedbackFile):
    # this function analyses concerningData to determine the best feedback to give
    expireTime=10
    currentPriority=100
    currentFeedback=""
    currentMetric=""
    for m, info in concerningData.iteritems():
        for i in info:
            # expire old feedback - THIS COULD BE MORE SOPHISTICATED
            if time.time()-i['timestamp'] > expireTime:
                info.remove(i)
                # print "Removing a concern from "+m
            # it compares the data to the allowance and priority given in config
            # and finds the item that is the greatest outside the allowance and has the highest priority and flags this
            # print m+" "+str(len(info))+" "+str(metrics[m]['priority'])
            if len(info) > metrics[m]['allowance']:
                if metrics[m]['priority'] < currentPriority:
                    currentFeedback=m+"_"+i['issue']
                    currentPriority=metrics[m]['priority']
                    currentMetric=m
    print "Feedback will be for: "+currentFeedback
    global lastFeedback
    if currentFeedback != "":
        # at the end, the flagged data is used to look up the correct response from the feedbackMap and writes to the file
        lastFeedback = time.time()
        feedbackFile.write(str(FEEDBACK_MAP[currentFeedback])+"\n")
        feedbackFile.flush()
        # want to remove all the previous concerns about this issue because theoretically they've learned now
        concerningData[currentMetric] = []

# function: giveKineticFeedback
def giveKineticFeedback(syncFile, metrics, historicalData, feedbackFile):
    global start_time
    # this function givesKineticFeedback based on the inputs
    concerningData = {
        "speed": [],
        "clarity": [],
        "volume": [],
        "head_gaze": []
        # "gestures": []
    }
    stop = False
    # while not told to stop:
    while not stop:
        concern = False
        for m, info in metrics.iteritems():
            # then reads in the latest data for all the files
            f = info['file']
            where = f.tell()
            line = f.readline()
            while not (not line or line in ['\n', '\r\n']):
                # Sometimes the whole line isn't read, this fixes the error
                if not line.endswith('\n'):
                    suffix = f.readline()
                    line = line + suffix
                    f.seek(f.tell())
                    continue
                data = line.rstrip('\n').split()
                if len(data) < 2:
                    print "There was an issue with line: "+line
                    line = f.readline()
                    f.seek(f.tell())
                    continue
                historicalData[m].append(float(data[1]))
                print "reading "+m+" "+str(time.time()-float(data[0]))+" seconds after writing"
                # checks it against thresholds, adds to concerningData if a problem
                maybeAppend = {"timestamp": float(data[0]), "data": float(data[1])}
                if "min" in metrics[m]:
                    if float(data[1]) < metrics[m]['min']:
                        concern = True
                        maybeAppend['issue'] = "low"
                        concerningData[m].append(maybeAppend)
                        print m+" concerningly low"
                if "max" in metrics[m]:
                    if float(data[1]) > metrics[m]['max']:
                        concern = True
                        maybeAppend['issue'] = "high"
                        concerningData[m].append(maybeAppend)
                        print m+" concerningly high"
                line = f.readline()
                f.seek(f.tell())
        global lastFeedback
        if concern:
            if time.time() - lastFeedback > ROBOT_DELAY:
                makeFeedbackDecision(metrics, concerningData, feedbackFile)
            else:
                print "Robot probably not ready"
        # check if sync has said to stop
        syncFileStop = open("output/sync.txt", 'r')
        for sline in syncFileStop:
            if sline.rstrip('\n') == "stop":
                stop = True
                print "User called for stop"
        syncFileStop.close()
# function: givePostFeedback
def givePostFeedback(historicalData, metrics):
    # this function aggregates the historical data
    # then fills in string templates with the relevant data
    feedbackList = []
    for m, dataList in historicalData.iteritems():
        print m
        print len(dataList)
        if m == "head_gaze":
            total = 0
            for d in dataList:
                total += ( d > metrics[m]["min"] ) # sum the number of times it is above the min
            percent = int(round(float(total)/len(dataList) * 100))
            feedbackList.append("You looked at me " + str(percent) + " percent of the time.\n")
        elif m == "speed":
            total = 0
            for d in dataList:
                total += d
            avg = int(round(total/len(dataList)))
            feedbackList.append("On average, you spoke at " + str(avg) + " words per minute.\n")
        elif m == "volume":
            totalLow = 0
            totalHigh = 0
            for d in dataList:
                totalLow += ( d < metrics[m]["min"] )
                totalHigh += ( d > metrics[m]["max"] )
            pLow = int(round(float(totalLow)/len(dataList)*100))
            pHigh = int(round(float(totalHigh)/len(dataList)*100))
            threshold = 5 # a certain amount of allowance
            if pLow > threshold and totalLow > totalHigh:
                feedbackList.append("You spoke too quietly "+str(pLow)+" percent of the time, you can improve!")
            elif pHigh > threshold and totalHigh > totalLow:
                feedbackList.append("You spoke too loudly "+str(pHigh)+" percent of the time, you can improve!")
        elif m == "clarity":
            total = 0
            for d in dataList:
                total += ( d < metrics[m]["min"] )
            percent = int(round(float(total)/len(dataList) * 100))
            threshold = 1
            if percent > threshold:
                feedbackList.append("I couldn't understand you "+str(percent)+" of the time, be careful!")
    overallGoodThreshold = 1
    overallMedThreshold = 2
    overallBadThreshold = 3
    numberOfIssues = len(feedbackList)
    if numberOfIssues < overallGoodThreshold:
        feedbackList.append("That was really good, keep it up!")
    elif numberOfIssues < overallMedThreshold:
        feedbackList.append("Well done, but keep in mind the feedback for next time.")
    elif numberOfIssues < overallBadThreshold:
        feedbackList.append("You can do better! Think about my feedback and try again.")
    # and writes these strings to file
    file = open("output/postspeech_feedback.txt", 'w')
    for f in feedbackList:
        file.write(f)
    file.close()

# function: main
def main():
    # this function is the main control
    global start_time
    metrics = {
        "speed": {},
        "clarity": {},
        "volume": {},
        "head_gaze": {}
        # "gestures": {}
    }
    historicalData = {
        "speed": [],
        "clarity": [],
        "volume": [],
        "head_gaze": []
        # "gestures": []
    }

    maxtime = 60 # in seconds
    try: # do the following unless maxtime is reached:
        with timeout(maxtime, exception=RuntimeError):
            # it calls configure, passing in the metrics structure
            configure(metrics)
            start = False
            syncFile = open('output/sync.txt', 'r', os.O_NONBLOCK)
            feedbackFile = open('output/kinetic_feedback.txt', 'w', os.O_NONBLOCK)
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
            start_time = time.time()
            giveKineticFeedback(syncFile, metrics, historicalData, feedbackFile)
    except RuntimeError:
        print "Stopping: run time exceeded "+str(maxtime)+" seconds"
        pass

    syncFile.close()
    feedbackFile.close()
    givePostFeedback(historicalData, metrics)

main()
