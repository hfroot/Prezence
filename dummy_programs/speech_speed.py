import random
import os
import time

f = open('output/speed.txt', 'w')
for i in range(5):
	f.write(str(i)+" "+str(random.randrange(130,190))+"\n")
	time.sleep(0.5)

f.close()