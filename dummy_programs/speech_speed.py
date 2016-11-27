import random
import os
import time

f = open(os.path.dirname(os.path.realpath(__file__))+'/output/speech_speed.txt', 'w')
for i in range(5):
	f.write(str(random.randrange(130,190))+"\n")
	time.sleep(0.5)

f.close()