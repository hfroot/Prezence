

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os
import sys
from pprint import pprint
import audioop
import re #to do regex
import time #to do timer
import fileinput

def countlines(startstopfile):
	with open(startstopfile) as f:
		lines = 0
		for i, l in enumerate(f):
			lines = lines + 1
	return lines

#REMEMBER TO RUN IN SPEECH FOLDER BECAUSE OF THE WAY FILES ARE ADDRESSED AND CREATED

# try:
# 	os.remove("output/speed.txt")
# 	os.remove("output/clarity.txt")
# 	os.remove("output/content_sp.txt")
# except:
# 	print("file does not exist")

try:
	f_speed = open("output/speed.txt" , "w")
	f_clarity = open("output/clarity.txt" , "w")
	f_content = open("output/content_sp.txt" , "w")	
	f_loud = open("output/volume.txt", "w")
	f_content.close()
	f_clarity.close()
	f_speed.close()
	f_loud.close()
except IOError:
	print "Could not open file"
	sys.exit(1)


# try:
# 	f_speed = open("C:\Python27\output\speed.txt" , "a")
# 	f_clarity = open("C:\Python27\output\clarity.txt" , "a")
# 	f_content = open("C:\Python27\output\content_sp.txt" , "a")	
# except IOError:
# 	print "Could not open file"
# 	sys.exit(1)

# obtain audio from the microphone
r = sr.Recognizer()

m = 0
for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
	if microphone_name == "USB audio CODEC: Audio (hw:1,0)":
		m = i
		break

with sr.Microphone(device_index=m, sample_rate = 16000, chunk_size = 1024) as source:
	print("KEEP QUIET! MIC CALIBRATION")
	timer_HCR = int(os.getenv('timer' , 5)) #time to listen for in seconds
	#timer_HCR=int(timer_HCR)
	audio = r.record(source,duration=timer_HCR)

audioasstring = audio.get_raw_data()
background_noise = audioop.rms(audioasstring, 2) #2 means 2 bytes per sample i.e 16-bit audio
#noisefloor = audioop.minmax(audioasstring, 2)
		

presentation_start = False
print("Waiting for start signal \n")

######################END OF INIT###################################################

#########################CHECK FOR START AND STOP#############################################################################
while(presentation_start == False):
	# with sr.Microphone(device_index=m) as source:
	# 	print("Waiting to start!")
	# 	timer_HCR = os.getenv('timer' , 4) #time to listen for in seconds
	# 	timer_HCR=int(timer_HCR)
	# 	audio = r.record(source,duration=timer_HCR)

	# msg_json=r.recognize_google(audio,show_all=True) #extract message
	# try:
	# 	rec=str(msg_json['alternative'][0]['transcript'])
	# except:
	# 	rec="Nothing said"

	# print("Google Speech Recognition thinks you said " + rec + "\n") 

		
	# #Check if user has said "Prezence start" (google thinks Prezence is Presents)
	# #starting = re.search('presents? go|presence go', rec, flags=re.I) #flag to ignore any upper or lower-casing the speech recogniser
	# starting = re.search('go', rec, flags=re.I) #flag to ignore any upper or lower-casing the speech recogniser

	# if(starting != None):
	# 	try:
	# 		startfile = open('output/sync.txt', 'w')
	# 		timefile = open('output/time.txt', 'w')
	# 		startfile.write("start")
	# 		timefile.write(str(long(float(time.time()))))
	# 		print 'startfile created'
	# 		startfile.close()
	# 		timefile.close()
	# 		presentation_start = True
	# 	except IOError:
	# 		print "creating startfile went wrong"
	# 		sys.exit(1)
	print("Still waiting")
	numlines = countlines("output/sync.txt")
	if(numlines >= 1):
		presentation_start = True
		print(numlines)
	else:
		time.sleep(1)
		print(numlines)
################END OF START STOP#############################################################################

#############MAIN LOOP########################################################################################
while(presentation_start is True):

	


	# recognize speech using Google Speech Recognition
	try:
		try:
			f_speed = open("output/speed.txt" , "a")
			f_clarity = open("output/clarity.txt" , "a")
			f_content = open("output/content_sp.txt" , "a")	
			f_loud = open("output/volume.txt", "a")
		except IOError:
			print "Could not open file"
			sys.exit(1)
		# obtain audio from the microphone
		#r = sr.Recognizer()
		with sr.Microphone(device_index=m) as source:
			print("Say something!")
			timer_HCR = os.getenv('timer' , 5) #time to listen for in seconds
			timer_HCR=int(timer_HCR)
			audio = r.record(source,duration=timer_HCR)
				##clarity of speech
			msg_json=r.recognize_google(audio,show_all=True)

		try:
			number=(msg_json['alternative'][0]['confidence'])
			rec=str(msg_json['alternative'][0]['transcript'])
		except:
			print("Prezence could not understand audio")
			number=0
			rec="NULL"
			space_split=-1
			print("confice level is:" + str(number) +" for " + str(rec)+" ," +"number of spaces is: " + str(space_split) )
			f_speed.write(str(time.time()) + " " +str(space_split)+ "\n")
			f_clarity.write(str(time.time()) + " " +str(number)+ "\n")
			f_content.write("prezence does not understand your speech \n" )
			f_loud.write(str(time.time()) + " 0\n")
			continue



		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		#print("Google \n")



		print("Google Speech Recognition thinks you said " + rec + "\n") 
			
		print("confice level is:" + str(number) +" for " + rec )
		
		f_clarity.write(str(time.time()) + " " + str(number)+ "\n")
		f_content.write(rec+ "\n")
			
		
	##########################Trying Loudness stuff####################################################################
		audioasstring = audio.get_raw_data()
		loudness = audioop.rms(audioasstring, 2) #2 means 2 bytes per sample i.e 16-bit audio
		voice_vol = loudness - background_noise
		if(voice_vol < 0):
			voice_vol = 0
		#noisefloor = audioop.minmax(audioasstring, 2)
		f_loud.write(str(time.time()) + " " + str(voice_vol) + "\n")
		print("Volume: " + str(voice_vol))
	##################################################################################################################

		
		##fast/slow speaking
		space_split=len(rec.split(" "))
		print("number of words spoken is:" +" " + str(space_split))
		f_speed.write(str(time.time()) + " " + str(20*int(space_split))+ "\n")
		
		#>150 wpm
		# if(space_split> (2.4*timer_HCR) ):
		# 	print("you are speaking too fast")
		# 	#f.write("you are speaking too fast")
			
		# 	#110 to 150 words per minute
		# elif(  (1.83*timer_HCR)  <space_split <= (2.4*timer_HCR)):	
		# 	print("you are speaking normal")
		# 	#f.write("you are speaking normal")
			
			
		# 	#100 to 110 wpm
		# elif(  (1.66*timer_HCR)  <space_split<= (1.83*timer_HCR)):	
		# 	print("you are speaking slow")
		# 	#f.write("you are speaking slow")
			
			
		# 	#less than 100
		# elif( space_split <= (1.66*timer_HCR)):	
		# 	print("you are speaking too slow")
		# 	#f.write("you are speaking too slow")

		#########################CHECK FOR STOP#############################################################################		
		#Check if user said "Prezence stop"
		#ending = re.search('presents? end|presence end|presents? and|presence and', rec, flags=re.I)
		# ending = re.search('end$|stop$', rec, flags=re.I)
		# if(ending != None):
		# 	try:
		# 		startfile = open("output/sync.txt", "a")
		# 		timefile = open("output/time.txt", "a+")
		# 		startfile.write("\nstop")
		# 		endtime = long(float(time.time())) #IF stopped, we want to compute how long presentation took
		# 		print(endtime)
		# 		starttime = long(timefile.readline()) #get start time that we saved earlier
		# 		print(starttime)
		# 		timediff = endtime - starttime
		# 		print(timediff)
		# 		timediff_min = long(timediff / 60)
		# 		print(timediff_min)
		# 		timediff_sec = timediff % 60
		# 		print(timediff_sec)
		# 		timefile.write('\n'+ str(timediff_min) + 'min' + str(timediff_sec) + 'sec')
		# 		print 'It took ' + str(timediff_min) + 'min' + str(timediff_sec) + 'sec'
		# 		print 'endfile created'
		# 		startfile.close()
		# 		timefile.close()

		# 		presentation_start = False #Exit main loop
		# 	except IOError:
		# 		print "creating endfile went wrong"
		# 		sys.exit(1)

		#get number of lines
		numlines = countlines("output/sync.txt")
		print("number of lines: " + str(numlines))
		if (numlines >= 2):
			presentation_start = False
	################END OF START STOP#############################################################################
		
		
		
		
		
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		number=0
		rec="NULL"
		space_split=-1
		print("confice level is:" + str(number) +" for " + str(rec)+" ," +"number of spaces is: " + str(space_split) )
		f_speed.write(str(space_split)+ "\n")
		f_clarity.write(str(number)+ "\n")
		f_content.write("prezence does not understand your speech \n" )
		f_loud.write('0\n')

	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

	f_speed.close()
	f_clarity.close()
	f_content.close()
	f_loud.close()

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
	
	
	
	
	####################################################################################################
# recognize speech using Sphinx
# try:
    # print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
    # print("Sphinx could not understand audio")
# except sr.RequestError as e:
    # print("Sphinx error; {0}".format(e))
######################################################################################################