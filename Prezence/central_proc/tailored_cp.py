import os
import time
from interruptingcow import timeout
startTime = 0
ROBOT_DELAY = 10
lastFeedback = 0
TIME_DELAY_MAX = 1
FEEDBACK_MAP = {
    "head_gaze_low": 1,
    "covering_mouth_high": 2,
    # "posture_low": 3,
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
        filename = ""
        if configData[0] == "gesture":
            m = configData[1]
            filename = outputDir+"gesture.txt"
            # metrics[m] = { "file": open(outputDir+"gesture.txt", 'r', os.O_NONBLOCK) }
            i = 2
        else:
            m = configData[0]
            filename = outputDir+m+".txt"
            # metrics[m] = { "file": open(outputDir+m+".txt", 'r', os.O_NONBLOCK) }
            i = 1
        metrics[m] = { "file": open(filename, 'r', os.O_NONBLOCK) }
        while i < len(configData):
            metrics[m][configData[i]] = float(configData[i+1])
            print m+" "+configData[i]+" "+configData[i+1]
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
        # if m == "gesture":
        #     coveringMouthTotal = 0
        #     for i in info:
        #         if i['data'] == "covering_mouth":
        #             coveringMouthTotal += 1

        # else: 
        coveringMouthTotal = 0
        for i in info:
            # expire old feedback - THIS COULD BE MORE SOPHISTICATED
            if time.time()-i['timestamp'] > expireTime:
                info.remove(i)
                print "Removing a concern from "+m
            if m == "gesture":
                if i['data'] == "covering_mouth":
                    coveringMouthTotal += 1
            # it compares the data to the allowance and priority given in config
            # and finds the item that is the greatest outside the allowance and has the highest priority and flags this
            # print m+" "+str(len(info))+" "+str(metrics[m]['priority'])
        # print coveringMouthTotal
        problemMetric = ""
        if m == "gesture":
            if len(info) > 0:
                gestureName = info[0]['data']
                if coveringMouthTotal > metrics[gestureName]['allowance']:
                    problemMetric = gestureName
        elif len(info) > metrics[m]['allowance']:
            if metrics[m]['priority'] < currentPriority:
                problemMetric = m
        if not problemMetric == "" and metrics[problemMetric]['priority'] < currentPriority:
            currentFeedback=problemMetric+"_"+i['issue']
            currentPriority=metrics[problemMetric]['priority']
            currentMetric=problemMetric
    print "Feedback will be for: "+currentFeedback
    global lastFeedback
    if currentFeedback != "":
        # at the end, the flagged data is used to look up the correct response from the feedbackMap and writes to the file
        lastFeedback = time.time()
        feedbackFile.write(str(FEEDBACK_MAP[currentFeedback])+"\n")
        feedbackFile.flush()
        # want to remove all the previous concerns about this issue because theoretically they've learned now
        if isGesture(currentMetric):
            # print concerningData["gesture"]
            concerningData["gesture"][:] = [d for d in concerningData["gesture"] if d.get('data') != currentMetric]
            # print concerningData["gesture"]
            # for gestureInfo in concerningData["gesture"]:
            #     if gestureInfo['data'] == currentMetric:
            #         del concerningData["gesture"][gestureInfo]
        else:
            concerningData[currentMetric] = []

def isGesture(metric):
    return not (metric == "clarity" or metric == "speed" or metric == "volume" or metric == "head_gaze")

# function: giveKineticFeedback
def giveKineticFeedback(syncFile, metrics, historicalData, feedbackFile):
    global startTime
    # this function givesKineticFeedback based on the inputs
    concerningData = { "gesture": [] }
    historicalData["gesture"] = []
    for m in metrics:
        if not isGesture(m):
            concerningData[m] = []
            historicalData[m] = []

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
                    # print "There was an issue with line: "+line
                    line = f.readline()
                    f.seek(f.tell())
                    continue
                value = 0
                metric = ""
                timeDelay = time.time()-float(data[0])
                # print "reading "+m+" "+str(timeDelay)+" seconds after writing"
                if not isGesture(m):
                    value = float(data[1])
                    metric = m
                    # checks it against thresholds, adds to concerningData if a problem
                    maybeAppend = {"timestamp": float(data[0]), "data": value}
                    if "min" in metrics[m]:
                        if value < metrics[m]['min']:
                            concern = True
                            maybeAppend['issue'] = "low"
                            concerningData[m].append(maybeAppend)
                            print m+" concerningly low"
                    if "max" in metrics[m]:
                        if value > metrics[m]['max']:
                            concern = True
                            maybeAppend['issue'] = "high"
                            concerningData[m].append(maybeAppend)
                            print m+" concerningly high"
                else:
                    value = data[1]
                    metric = "gesture"
                    maybeAppend = {"timestamp": float(data[0]), "data": value}
                    if value == "covering_mouth":
                        concern = True
                        maybeAppend["issue"] = "high"
                        if not maybeAppend in concerningData[metric]:
                            concerningData[metric].append(maybeAppend)
                historicalData[metric].append(value)
                timeDelay = time.time()-float(data[0])
                if timeDelay > TIME_DELAY_MAX:
                    print "reading "+m+" "+str(timeDelay)+" seconds after writing"

                line = f.readline()
                f.seek(f.tell())
        global lastFeedback
        if concern > 0:
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

def generateGestureFeedback(m, dataList, feedbackList, gestureCount):
    feedback = ""
    totals = {}
    for d in dataList:
        if d in totals:
            totals[d] += 1
        else:
            totals[d] = 1
    for d in dataList:
        if d in totals:
            total = totals[d]
            percent = int(round(float(total)/gestureCount * 100))
            action = d.split('_')
            if d == "folding_arms" or d == "covering_mouth":
                feedback = "You were "+action[0]+" your "+action[1]+" "+str(percent)+" percent of the time.\n"
            elif d == "poor_posture":
                feedback = "You had "+action[0]+" "+action[1]+" "+str(percent)+" percent of the time.\n"
            elif d == "turning_away":
                feedback = "You were "+action[0]+" "+action[1]+" "+str(percent)+" percent of the time.\n"
            threshold = 10
            if percent > threshold:
                feedbackList.append(feedback)
            del totals[d]

# function: givePostFeedback
def givePostFeedback(historicalData, metrics, timeTaken):
    # this function aggregates the historical data
    # then fills in string templates with the relevant data
    feedbackList = []
    feedbackList.append("Your speech was "+str(int(round(timeTaken)/60))+" minutes and "+str(int(round(timeTaken)%60))+" seconds long.\n")
    gestureCount = 0
    for m, dataList in historicalData.iteritems():
        if isGesture(m):
            gestureCount += len(dataList)
    for m, dataList in historicalData.iteritems():
        print m
        print len(dataList)
        # print dataList
        if len(dataList) > 0:
            if m == "head_gaze":
                total = 0
                for d in dataList:
                    total += ( d < metrics[m]["min"] ) # sum the number of times it is above the min
                percent = int(round(float(total)/len(dataList) * 100))
                threshold = 5
                if percent > threshold:
                    feedbackList.append("You were looking down " + str(percent) + " percent of the time.\n")
            elif m == "speed":
                # totalSlow = 0
                # totalFast = 0
                # for d in dataList:
                #     totalSlow += ( d < metrics[m]["min"] ) # sum the number of times it is above the min
                #     totalFast += ( d > metrics[m]["max"] ) # sum the number of times it is above the max
                # avgSlow = int(round(totalSlow/len(dataList)))
                # avgFast = int(round(totalFast/len(dataList)))
                # feedbackList.append("On average, you spoke at " + str(avg) + " words per minute.\n")
                totalLow = 0
                totalHigh = 0
                for d in dataList:
                    totalLow += ( d < metrics[m]["min"] )
                    totalHigh += ( d > metrics[m]["max"] )
                pLow = int(round(float(totalLow)/len(dataList)*100))
                pHigh = int(round(float(totalHigh)/len(dataList)*100))
                threshold = 5 # a certain amount of allowance
                if pLow > threshold and totalLow > totalHigh:
                    feedbackList.append("You spoke too slowly "+str(pLow)+" percent of the time.\n")
                elif pHigh > threshold and totalHigh > totalLow:
                    feedbackList.append("You spoke too quickly "+str(pHigh)+" percent of the time.\n")
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
                    feedbackList.append("You spoke too quietly "+str(pLow)+" percent of the time.\n")
                elif pHigh > threshold and totalHigh > totalLow:
                    feedbackList.append("You spoke too loudly "+str(pHigh)+" percent of the time.\n")
            elif m == "clarity":
                total = 0
                for d in dataList:
                    total += ( d < metrics[m]["min"] ) # sum the number of times it is below the min
                percent = int(round(float(total)/len(dataList) * 100))
                feedbackList.append("I could not understand you " + str(percent) + " percent of the time.\n")
            else:
                generateGestureFeedback(m, dataList, feedbackList, gestureCount)
            
    overallGoodThreshold = 2
    overallMedThreshold = 4
    numberOfIssues = len(feedbackList)
    if numberOfIssues < overallGoodThreshold:
        feedbackList.append("That was really good, keep it up!\n")
    elif numberOfIssues < overallMedThreshold:
        feedbackList.append("Well done, but keep in mind the feedback for next time.\n")
    else:
        feedbackList.append("You can do better! Think about my feedback and try again.\n")
    # and writes these strings to file
    file = open("output/postspeech_feedback.txt", 'w')
    for f in feedbackList:
        file.write(f)
    file.close()

# function: main
def main():
    # this function is the main control
    global startTime
    metrics = {}
    historicalData = {}

    maxtime = 80*60 # in seconds
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
            startTime = time.time()
            time.sleep(9)
            giveKineticFeedback(syncFile, metrics, historicalData, feedbackFile)
    except RuntimeError:
        print "Stopping: run time exceeded "+str(maxtime)+" seconds"
        pass
    endTime = time.time()
    syncFile.close()
    feedbackFile.close()
    givePostFeedback(historicalData, metrics, endTime-startTime)

main()
