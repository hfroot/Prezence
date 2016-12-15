import random
import os
import time

gestures = ["shifting weight", "moving", "waving", "stop"]

f = open(os.path.dirname(os.path.realpath(__file__))+'/output/cv_gesture.txt', 'w')
stop = False
while 1:
	gesture = gestures[random.randrange(0,4)]
	f.write(gesture+"\n")
	if gesture == "stop":
		break
	time.sleep(1)

f.close()