

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os
from pprint import pprint
import audioop
import re #to do regex
import time #to do timer

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    timer_HCR = os.getenv('timer' , 5) #time to listen for in seconds
    timer_HCR=int(timer_HCR)
    audio = r.record(source,duration=timer_HCR)
	
##########################Trying Loudness stuff####################################################################
    audioasstring = audio.get_raw_data()
    loudness = audioop.rms(audioasstring, 2) #2 means 2 bytes per sample i.e 16-bit audio
    noisefloor = audioop.minmax(audioasstring, 2)
    print ("how loud: " + str(loudness) + " " + str(noisefloor))
##################################################################################################################

# recognize speech using Sphinx
# try:
    # print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
    # print("Sphinx could not understand audio")
# except sr.RequestError as e:
    # print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
	print("Google \n")
	print("Google Speech Recognition thinks you said " + r.recognize_google(audio) + "\n") 
	
	msg_json=r.recognize_google(audio,show_all=True)
	try:
		number=(msg_json['alternative'][0]['confidence'])
		rec=str(msg_json['alternative'][0]['transcript'])
	except:
		rec=(msg_json['alternative'][0]['transcript'])
		number="0"

#########################CHECK FOR START AND STOP#############################################################################		
	#Check if user has said "Prezence start" (google thinks Prezence is Presents)
	starting = re.search('presents? start|presence start', rec, flags=re.I) #flag to ignore any upper or lower-casing the speech recogniser
	#Check if user said "Prezence stop"
	ending = re.search('presents? stop|presence stop', rec, flags=re.I)
	if(starting != None):
		try:
			startfile = open('startrobot.txt', 'w')
			startfile.write(str(long(float(time.time()))))
			print 'startfile created'
			startfile.close()
		except IOError:
			print "creating startfile went wrong"
			sys.exit(1)
	elif(ending != None):
		try:
			startfile = open('startrobot.txt','r')
			endfile = open('endrobot.txt', 'w')
			endtime = long(float(time.time()))
			starttime = long(startfile.readline())
			endfile.write(str(endtime))
			startfile.close()
			endfile.close()
			
			timediff = endtime - starttime
			timediff_min = long(timediff / 60)
			timediff_sec = timediff % 60
			print 'endfile created'
			print 'It took ' + str(timediff_min) + 'min' + str(timediff_sec) + 'sec'
			
		except IOError:
			print "creating endfile went wrong"
			sys.exit(1)
	#else:
	#	try:
	#		os.remove('startrobot.txt')
	#	except OSError:
	#		print "startrobot doesn't exist"
	#	
	#	try:
	#		os.remove('endrobot.txt')
	#	except OSError:
	#		print "endrobot doesn't exist"
################END OF START STOP#############################################################################

	try:
	    f = open ("speechout.txt", "w")
	except IOError:
		print "Could not open file"
		sys.exit(1)
		
	print("confice level is:" + str(number) +" for " + rec )
	f.write("confice level is:" + str(number) + '\n')
	f.write(rec + '\n')
	
	#fast/slow speaking
	space_split=len(rec.split(" "))
	print(space_split)
	
	if(space_split> (2*timer_HCR) ):
		print("you are speaking too fast")
		f.write("you are speaking too fast")
		
	elif(space_split< (2*timer_HCR)):	
		print("you are speaking too slow")
		f.write("you are speaking too slow")
		
	else:
		print("your speed is fine")
		f.write("your speed is fine")
	
	
	f.close()
	
	
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    number=-1
    rec="NULL"
    space_split=0
    #print("confice level is:" + str(number) +" for " + str(rec)+" " +" str(space_split) )

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



# recognize speech using Microsoft Bing Voice Recognition
#BING_KEY = "28cfcf7a63c441b0815c4295157b9c7f" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
#try:
	#pprint(r.recognize_bing(audio, key=BING_KEY,show_all=True))  confidence level for Microsoft
#    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
#except sr.UnknownValueError:
#    print("Microsoft Bing Voice Recognition could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))




# recognize speech using IBM Speech to Text
# IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
# IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE" # IBM Speech to Text passwords are mixed-case alphanumeric strings
# try:
    # print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
# except sr.UnknownValueError:
    # print("IBM Speech to Text could not understand audio")
# except sr.RequestError as e:
    # print("Could not request results from IBM Speech to Text service; {0}".format(e))