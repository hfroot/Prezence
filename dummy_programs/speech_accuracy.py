import random
import os
import time

f = open('output/accuracy.txt', 'w')
for i in range(5):
	f.write(str(i)+" "+str(random.random())+"\n")
	time.sleep(1)

f.close()