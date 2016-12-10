import random
import os
import time

f = open('output/volume.txt', 'w')
sf = open('output/sync.txt', 'w')
hf = open('output/head_gaze.txt', 'w')
speedf = open('output/speed.txt', 'w')
af = open('output/accuracy.txt', 'w')
time.sleep(2)
sf.write("start\n")
sf.close()
for i in range(5):
	f.write(str(time.time())+" "+str(random.randrange(50,110))+"\n")
	hf.write(str(time.time())+" "+str(random.randrange(50,250))+"\n")
	speedf.write(str(time.time())+" "+str(random.randrange(130,190))+"\n")
	af.write(str(time.time())+" "+str(random.random())+"\n")
	time.sleep(0.5)

f.close()