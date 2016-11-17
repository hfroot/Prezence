# -*- encoding: UTF-8 -*- 

import math
# import almath as m # python's wrapping of almath
import sys
from naoqi import ALProxy


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def StiffnessOff(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 0.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def StandUp(proxy):
    proxy.goToPosture("StandInit", 1.0)

def SitDown(proxy):
    proxy.goToPosture("Sit", 1.0)

def Walk(proxy,x,y,theta):
    proxy.moveTo(x, y, theta)
    self.onStopped()

def main(robotIP,robotPort):

    #Setting the Proxies
    try:
        motionProxy = ALProxy("ALMotion", robotIP, robotPort)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        ttsProxy = ALProxy("ALTextToSpeech", robotIP, robotPort)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, robotPort)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e


    # Turn on the Motors
    StiffnessOn(motionProxy)

    #StandUp
    StandUp(postureProxy)

    #Walk 1 Meter
    Walk(motionProxy,1,0,0)


    #Sit Down
    SitDown(postureProxy)

    # Turn off the Motors
    StiffnessOff(motionProxy)



if __name__ == "__main__":
    robotIp = "127.0.0.1" #Set a default IP here
    robotPort = 1234 #Set default POort here


    if len(sys.argv) < 2:
        print "Usage python robotIP please"
    else:
        robotIp = sys.argv[1]

    if len(sys.argv) > 2:
        print "Usage python robotPort please"
    else:
        robotPort = int(sys.argv[2])

    main(robotIp, robotPort)