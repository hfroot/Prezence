def SitDown(proxy):

    proxy.goToPosture("Crouch", 1.0)
	proxy.goToPosture("LyingBack", 1.0)
	proxy.goToPosture("LyingBelly", 1.0)
	proxy.goToPosture("Sit", 1.0)
	proxy.goToPosture("SitRelax", 1.0)
	proxy.goToPosture("Stand", 1.0)
    proxy.goToPosture("StandZero", 1.0)





   #Wake up robot

       motionProxy.wakeUp()

     #Turn motor off
       motionProxy.rest()