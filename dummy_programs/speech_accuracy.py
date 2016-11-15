import random
import os
import time

f = open(os.path.dirname(os.path.realpath(__file__))+'/output/speech_accuracy.txt', 'w')
for i in range(5):
	f.write(str(random.random())+"\n")
	time.sleep(1)

f.close()