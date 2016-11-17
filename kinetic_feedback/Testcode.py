import math

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box

        #Initialising         
        ttsProxy = ALProxy("ALTextToSpeech")
        motionProxy=ALProxy("ALMotion")
        postureProxy=ALProxy("ALRobotPosture")
        
        #Turning on da motors
        pNames = "Body"
        pStiffnessLists = 1.0
        pTimeLists = 1.0
        motionProxy.stiffnessInterpolation(pNames, pStiffnessLists,
        pTimeLists)
        
        #Stand Up
        postureProxy.goToPosture("Sit", 1.0)
        postureProxy.goToPosture("StandInit", 1.0)
        
        #Walk 1 Metre
        x  = 1
        y  = 0
        theta  = 0
        motionProxy.moveTo(x, y, theta)
        self.onStopped()
        
        #Sit Down
        postureProxy.goToPosture("Sit", 1.0)
        
        
        #Turning off the motors
        pNames = "Body"
        pStiffnessLists = 0.0
        pTimeLists = 1.0
        motionProxy.stiffnessInterpolation(pNames, pStiffnessLists,
        pTimeLists)
    # Will block until move Task is finished

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
