import random
import os
import time

f = open('output/volume.txt', 'w', os.O_NONBLOCK)
sf = open('output/sync.txt', 'w')
hf = open('output/head_gaze.txt', 'w', os.O_NONBLOCK)
speedf = open('output/speed.txt', 'w', os.O_NONBLOCK)
af = open('output/clarity.txt', 'w', os.O_NONBLOCK)
gf = open('output/gesture.txt', 'w', os.O_NONBLOCK)
sf.write("start\n")
sf.flush()
sf.close()
time.sleep(2)
for i in range(15):
	print "data to files"
	f.write(str(time.time())+" "+str(random.randrange(50,110))+"\n")
	f.flush()
	hf.write(str(time.time())+" "+str(random.randrange(50,250))+"\n")
	hf.flush()
	speedf.write(str(time.time())+" "+str(random.randrange(130,190))+"\n")
	speedf.flush()
	af.write(str(time.time())+" "+str(random.random())+"\n")
	af.flush()
	if(i%3==0):
		gf.write(str(time.time())+" "+"poor_posture"+"\n")
	if(i%4==0):
		gf.write(str(time.time())+" "+"folding_arms"+"\n")
	if(i%5==0):
		gf.write(str(time.time())+" "+"covering_mouth"+"\n")
	time.sleep(1)

sf = open('output/sync.txt', 'w')
sf.write("stop\n")
sf.close()
f.close()
af.close()
gf.close()
speedf.close()
hf.close()