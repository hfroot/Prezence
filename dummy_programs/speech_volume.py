import random
import os
import time

f = open(os.path.dirname(os.path.realpath(__file__))+'/output/speech_volume.txt', 'w')
for i in range(5):
	f.write(str(random.randrange(50,110))+"\n")
	time.sleep(0.5)

f.close()