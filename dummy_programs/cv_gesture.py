import random
import os
import time

gestures = ["shifting weight", "moving", "waving"]

f = open(os.path.dirname(os.path.realpath(__file__))+'/output/cv_gesture.txt', 'w')
for i in range(5):
	f.write(gestures[random.randrange(0,3)]+"\n")
	time.sleep(1)

f.close()