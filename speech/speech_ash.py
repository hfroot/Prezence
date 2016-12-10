

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os
import sys
from pprint import pprint
import audioop



try:
	os.remove("C:\Python27\output\speed.txt")
	os.remove("C:\Python27\output\clarity.txt")
except:
	print("file does not exist")
	

try:
	f_speed = open("C:\Python27\output\speed.txt" , "a")
	f = open("C:\Python27\output\clarity.txt" , "a")
		
except IOError:
	print "Could not open file"
	sys.exit(1)


while(True):

	# obtain audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something!")
		timer_HCR = os.getenv('timer' , 3) #time to listen for in seconds
		timer_HCR=int(timer_HCR)
		audio = r.record(source,duration=timer_HCR)
		

		
	##########################Trying Loudness stuff####################################################################
	 #   audioasstring = audio.get_raw_data()
	 #  loudness = audioop.rms(audioasstring, 2) #2 means 2 bytes per sample i.e 16-bit audio
	 #   noisefloor = audioop.minmax(audioasstring, 2)
	 #   print ("how loud: " + str(loudness) + " " + str(noisefloor))
	##################################################################################################################



	# recognize speech using Google Speech Recognition
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		print("Google \n")
		print("Google Speech Recognition thinks you said " + r.recognize_google(audio) + "\n") 
		

		
		
		
		
		
		##clarity of speech
		msg_json=r.recognize_google(audio,show_all=True)
		try:
			number=(msg_json['alternative'][0]['confidence'])
			rec=str(msg_json['alternative'][0]['transcript'])
		except:
			rec=(msg_json['alternative'][0]['transcript'])
			number="0"

			
		print("confice level is:" + str(number) +" for " + rec )
		
		f.write(str(number)+ "\n")
		
		
		
		
		##fast/slow speaking
		space_split=len(rec.split(" "))
		print("number of words spoken is:" +" " + str(space_split))
		f_speed.write(str(space_split)+ "\n")
		
		#>150 wpm
		if(space_split> (2.4*timer_HCR) ):
			print("you are speaking too fast")
			#f.write("you are speaking too fast")
			
			#110 to 150 words per minute
		elif(  (1.83*timer_HCR)  <space_split <= (2.4*timer_HCR)):	
			print("you are speaking normal")
			#f.write("you are speaking normal")
			
			
			#100 to 110 wpm
		elif(  (1.66*timer_HCR)  <space_split<= (1.83*timer_HCR)):	
			print("you are speaking slow")
			#f.write("you are speaking slow")
			
			
			#less than 100
		elif( space_split <= (1.66*timer_HCR)):	
			print("you are speaking too slow")
			#f.write("you are speaking too slow")
		
		
		
		
		
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		number=0
		rec="NULL"
		space_split=-1
		print("confice level is:" + str(number) +" for " + str(rec)+" ," +"number of spaces is: " + str(space_split) )
		f_speed.write(str(space_split)+ "\n")
		f.write(str(number)+ "\n")

	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

f_speed.close()
f.close()

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