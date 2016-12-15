#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os
import sys
from pprint import pprint
import audioop
import re #to do regex
import time #to do timer

#m = sr.Microphone(device_index=4)
miclist = sr.Microphone.list_microphone_names()
pprint(miclist)
