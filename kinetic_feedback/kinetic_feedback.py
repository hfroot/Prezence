# -*- encoding: UTF-8 -*- 

import math
# import almath as m # python's wrapping of almath
import sys
from naoqi import ALProxy
import time
import threading
from threading import Thread


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def StiffnessOff(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 0.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def StandUp(proxy):
    proxy.goToPosture("StandInit", 1.0)

def SitDown(proxy):
    proxy.goToPosture("Sit", 1.0)

def Walk(proxy,x,y,theta):
    proxy.moveTo(x, y, theta)
    # self.onStopped()

def gesture_1_handwave(motionProxy) :

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.68, 4.92])
    keys.append([0.00916195, 0.00916195])

    names.append("HeadYaw")
    times.append([0.68, 4.92])
    keys.append([-0.021518, -0.021518])

    names.append("LAnklePitch")
    times.append([0.68, 4.92])
    keys.append([-0.352862, -0.352862])

    names.append("LAnkleRoll")
    times.append([0.68, 4.92])
    keys.append([4.19617e-05, 4.19617e-05])

    names.append("LElbowRoll")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([-0.995524, -1.04921, -0.858998, -0.843658, -0.995524])

    names.append("LElbowYaw")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([-1.39905, -0.237812, -0.403484, -0.40962, -1.39905])

    names.append("LHand")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([0.2336, 0.6336, 0.6336, 0.6336, 0.2336])

    names.append("LHipPitch")
    times.append([0.68, 4.92])
    keys.append([-0.447886, -0.447886])

    names.append("LHipRoll")
    times.append([0.68, 4.92])
    keys.append([0.00310993, 0.00310993])

    names.append("LHipYawPitch")
    times.append([0.68, 4.92])
    keys.append([-0.00609398, -0.00609397])

    names.append("LKneePitch")
    times.append([0.68, 4.92])
    keys.append([0.699462, 0.699462])

    names.append("LShoulderPitch")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([1.41737, -0.935782, -1.00174, -0.891296, 1.41737])

    names.append("LShoulderRoll")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([0.28068, 0.354312, 1.04308, 0.36505, 0.28068])

    names.append("LWristYaw")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([-0.0614018, 0.31903, 0.31903, 0.31903, -0.0614019])

    names.append("RAnklePitch")
    times.append([0.68, 4.92])
    keys.append([-0.352778, -0.352778])

    names.append("RAnkleRoll")
    times.append([0.68, 4.92])
    keys.append([0.00157595, 0.00157595])

    names.append("RElbowRoll")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([0.997142, 1.0493, 1.0493, 1.0493, 0.997141])

    names.append("RElbowYaw")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([1.36215, 0.816046, 0.816046, 0.816046, 1.36215])

    names.append("RHand")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([0.246, 0.0408, 0.0408, 0.0408, 0.246])

    names.append("RHipPitch")
    times.append([0.68, 4.92])
    keys.append([-0.44797, -0.44797])

    names.append("RHipRoll")
    times.append([0.68, 4.92])
    keys.append([-0.00302601, -0.00302602])

    names.append("RHipYawPitch")
    times.append([0.68, 4.92])
    keys.append([-0.00609398, -0.00609397])

    names.append("RKneePitch")
    times.append([0.68, 4.92])
    keys.append([0.702614, 0.702614])

    names.append("RShoulderPitch")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([1.42666, 1.44047, 1.44047, 1.44047, 1.42666])

    names.append("RShoulderRoll")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([-0.265424, -0.154976, -0.154976, -0.154976, -0.265424])

    names.append("RWristYaw")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([-0.016916, -0.11816, -0.11816, -0.11816, -0.016916])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_2_puthandsdown(animatedSpeechProxy):

    # say the text with the local configuration
    animatedSpeechProxy.say("Put yo fat hands down yo!!", gesture_confused)

def gesture_3_leaning(motionProxy):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1])
    keys.append([0.0843279])

    names.append("HeadYaw")
    times.append([1])
    keys.append([0.0106959])

    names.append("LAnklePitch")
    times.append([1])
    keys.append([-0.527738])

    names.append("LAnkleRoll")
    times.append([1])
    keys.append([-0.300622])

    names.append("LElbowRoll")
    times.append([1])
    keys.append([-0.469362])

    names.append("LElbowYaw")
    times.append([1])
    keys.append([-0.926578])

    names.append("LHand")
    times.append([1])
    keys.append([0.0256])

    names.append("LHipPitch")
    times.append([1])
    keys.append([-0.207048])

    names.append("LHipRoll")
    times.append([1])
    keys.append([0.527738])

    names.append("LHipYawPitch")
    times.append([1])
    keys.append([-0.374254])

    names.append("LKneePitch")
    times.append([1])
    keys.append([0.918824])

    names.append("LShoulderPitch")
    times.append([1])
    keys.append([1.36215])

    names.append("LShoulderRoll")
    times.append([1])
    keys.append([-0.196394])

    names.append("LWristYaw")
    times.append([1])
    keys.append([0.470896])

    names.append("RAnklePitch")
    times.append([1])
    keys.append([-0.220854])

    names.append("RAnkleRoll")
    times.append([1])
    keys.append([0.191792])

    names.append("RElbowRoll")
    times.append([1])
    keys.append([0.1335])

    names.append("RElbowYaw")
    times.append([1])
    keys.append([0.793036])

    names.append("RHand")
    times.append([1])
    keys.append([0.348])

    names.append("RHipPitch")
    times.append([1])
    keys.append([0.11961])

    names.append("RHipRoll")
    times.append([1])
    keys.append([0.0782759])

    names.append("RHipYawPitch")
    times.append([1])
    keys.append([-0.374254])

    names.append("RKneePitch")
    times.append([1])
    keys.append([0.397348])

    names.append("RShoulderPitch")
    times.append([1])
    keys.append([1.24565])

    names.append("RShoulderRoll")
    times.append([1])
    keys.append([0.314159])

    names.append("RWristYaw")
    times.append([1])
    keys.append([0.639636])


    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_4_shrugging(motionProxy,postureProxy):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.12])
    keys.append([-0.01845])

    names.append("HeadYaw")
    times.append([1.12])
    keys.append([-0.0337899])

    names.append("LAnklePitch")
    times.append([1.12])
    keys.append([-0.352862])

    names.append("LAnkleRoll")
    times.append([1.12])
    keys.append([-0.00149202])

    names.append("LElbowRoll")
    times.append([1.12])
    keys.append([-1.49101])

    names.append("LElbowYaw")
    times.append([1.12])
    keys.append([-2.08567])

    names.append("LHand")
    times.append([1.12])
    keys.append([0.2536])

    names.append("LHipPitch")
    times.append([1.12])
    keys.append([-0.444818])

    names.append("LHipRoll")
    times.append([1.12])
    keys.append([-0.00149202])

    names.append("LHipYawPitch")
    times.append([1.12])
    keys.append([0.00157595])

    names.append("LKneePitch")
    times.append([1.12])
    keys.append([0.693326])

    names.append("LShoulderPitch")
    times.append([1.12])
    keys.append([0.0597839])

    names.append("LShoulderRoll")
    times.append([1.12])
    keys.append([0.240796])

    names.append("LWristYaw")
    times.append([1.12])
    keys.append([-0.216336])

    names.append("RAnklePitch")
    times.append([1.12])
    keys.append([-0.34971])

    names.append("RAnkleRoll")
    times.append([1.12])
    keys.append([-0.00149202])

    names.append("RElbowRoll")
    times.append([1.12])
    keys.append([1.51103])

    names.append("RElbowYaw")
    times.append([1.12])
    keys.append([2.08567])

    names.append("RHand")
    times.append([1.12])
    keys.append([0.158])

    names.append("RHipPitch")
    times.append([1.12])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([1.12])
    keys.append([0.0061779])

    names.append("RHipYawPitch")
    times.append([1.12])
    keys.append([0.00157595])

    names.append("RKneePitch")
    times.append([1.12])
    keys.append([0.696478])

    names.append("RShoulderPitch")
    times.append([1.12])
    keys.append([0.0337899])

    names.append("RShoulderRoll")
    times.append([1.12])
    keys.append([-0.016916])

    names.append("RWristYaw")
    times.append([1.12])
    keys.append([-0.096684])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

    postureProxy.goToPosture("StandInit", 1.0)

def gesture_5_arms(motionProxy):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.6, 7.6])
    keys.append([0.00916195, 0.00916195])

    names.append("HeadYaw")
    times.append([1.6, 7.6])
    keys.append([-0.021518, -0.021518])

    names.append("LAnklePitch")
    times.append([1.6, 7.6])
    keys.append([-0.352778, -0.352778])

    names.append("LAnkleRoll")
    times.append([1.6, 7.6])
    keys.append([-0.00157595, -0.00157595])

    names.append("LElbowRoll")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([-0.995524, -0.662646, -0.421808, -0.662646, -0.421808, -0.995524])

    names.append("LElbowYaw")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([-1.39905, -1.08305, -1.08305, -1.08305, -1.08305, -1.39905])

    names.append("LHand")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([0.2336, 0.6844, 0.6844, 0.6844, 0.6844, 0.2336])

    names.append("LHipPitch")
    times.append([1.6, 7.6])
    keys.append([-0.44797, -0.44797])

    names.append("LHipRoll")
    times.append([1.6, 7.6])
    keys.append([0.00302601, 0.00302602])

    names.append("LHipYawPitch")
    times.append([1.6, 7.6])
    keys.append([-0.00609398, -0.00609397])

    names.append("LKneePitch")
    times.append([1.6, 7.6])
    keys.append([0.702614, 0.702614])

    names.append("LShoulderPitch")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([1.41737, 0.294486, 1.65668, 0.294486, 1.65668, 1.41737])

    names.append("LShoulderRoll")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([0.28068, 0.371186, 0.262272, 0.371186, 0.262272, 0.28068])

    names.append("LWristYaw")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([-0.0614018, 0.83292, 0.866668, 0.83292, 0.866668, -0.0614019])

    names.append("RAnklePitch")
    times.append([1.6, 7.6])
    keys.append([-0.352778, -0.352778])

    names.append("RAnkleRoll")
    times.append([1.6, 7.6])
    keys.append([0.00157595, 0.00157595])

    names.append("RElbowRoll")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([0.995524, 0.587564, 0.121228, 0.587563, 0.121228, 0.995524])

    names.append("RElbowYaw")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([1.39905, 1.05995, 1.05995, 1.05995, 1.05995, 1.39905])

    names.append("RHand")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([0.2336, 0.7204, 0.7204, 0.7204, 0.7204, 0.2336])

    names.append("RHipPitch")
    times.append([1.6, 7.6])
    keys.append([-0.44797, -0.44797])

    names.append("RHipRoll")
    times.append([1.6, 7.6])
    keys.append([-0.00302601, -0.00302602])

    names.append("RHipYawPitch")
    times.append([1.6, 7.6])
    keys.append([-0.00609398, -0.00609397])

    names.append("RKneePitch")
    times.append([1.6, 7.6])
    keys.append([0.702614, 0.702614])

    names.append("RShoulderPitch")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([1.41737, 0.184122, 1.29934, 0.184122, 1.29934, 1.41737])

    names.append("RShoulderRoll")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([-0.28068, -0.220938, -0.184122, -0.220938, -0.184122, -0.28068])

    names.append("RWristYaw")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([0.0614018, -1.02015, -1.05237, -1.02015, -1.05237, 0.0614019])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_6_bored(motionProxy):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.12, 3.36])
    keys.append([0.00916195, 0.25])

    names.append("HeadYaw")
    times.append([1.12, 3.36])
    keys.append([-0.021518, -0.092082])

    names.append("LAnklePitch")
    times.append([1.12, 3.36])
    keys.append([-0.352778, -1.16281])

    names.append("LAnkleRoll")
    times.append([1.12, 3.36])
    keys.append([-0.00157595, 0.0061779])

    names.append("LElbowRoll")
    times.append([1.12, 3.36])
    keys.append([-0.995524, -1.54163])

    names.append("LElbowYaw")
    times.append([1.12, 3.36])
    keys.append([-1.39905, -0.62438])

    names.append("LHand")
    times.append([1.12, 3.36])
    keys.append([0.2336, 0.4936])

    names.append("LHipPitch")
    times.append([1.12, 3.36])
    keys.append([-0.44797, -0.811444])

    names.append("LHipRoll")
    times.append([1.12, 3.36])
    keys.append([0.00302601, 0.314512])

    names.append("LHipYawPitch")
    times.append([1.12, 3.36])
    keys.append([-0.00609398, -0.18097])

    names.append("LKneePitch")
    times.append([1.12, 3.36])
    keys.append([0.702614, 2.10921])

    names.append("LShoulderPitch")
    times.append([1.12, 3.36])
    keys.append([1.41737, 0.674918])

    names.append("LShoulderRoll")
    times.append([1.12, 3.36])
    keys.append([0.28068, -0.291502])

    names.append("LWristYaw")
    times.append([1.12, 3.36])
    keys.append([-0.0614018, -1.11526])

    names.append("RAnklePitch")
    times.append([1.12, 3.36])
    keys.append([-0.352778, -1.15506])

    names.append("RAnkleRoll")
    times.append([1.12, 3.36])
    keys.append([0.00157595, 0.0123138])

    names.append("RElbowRoll")
    times.append([1.12, 3.36])
    keys.append([0.995524, 0.905102])

    names.append("RElbowYaw")
    times.append([1.12, 3.36])
    keys.append([1.39905, 0.766958])

    names.append("RHand")
    times.append([1.12, 3.36])
    keys.append([0.2336, 0.0516])

    names.append("RHipPitch")
    times.append([1.12, 3.36])
    keys.append([-0.44797, -0.282298])

    names.append("RHipRoll")
    times.append([1.12, 3.36])
    keys.append([-0.00302601, 0.342124])

    names.append("RHipYawPitch")
    times.append([1.12, 3.36])
    keys.append([-0.00609398, -0.18097])

    names.append("RKneePitch")
    times.append([1.12, 3.36])
    keys.append([0.702614, 1.62148])

    names.append("RShoulderPitch")
    times.append([1.12, 3.36])
    keys.append([1.41737, 1.50796])

    names.append("RShoulderRoll")
    times.append([1.12, 3.36])
    keys.append([-0.28068, 0.167164])

    names.append("RWristYaw")
    times.append([1.12, 3.36])
    keys.append([0.0614018, -0.139636])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_7_coverears(motionProxy):
    # Choregraphe simplified export in Python.

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.6, 3.76])
    keys.append([0.00916195, 0.508257])

    names.append("HeadYaw")
    times.append([1.6, 3.76])
    keys.append([-0.021518, -0.0644701])

    names.append("LAnklePitch")
    times.append([1.6])
    keys.append([-0.352778])

    names.append("LAnkleRoll")
    times.append([1.6])
    keys.append([-0.00157595])

    names.append("LElbowRoll")
    times.append([1.6, 3.76])
    keys.append([-0.995524, -1.53242])

    names.append("LElbowYaw")
    times.append([1.6, 3.76])
    keys.append([-1.39905, -1.37757])

    names.append("LHand")
    times.append([1.6, 3.76])
    keys.append([0.2336, 0.022])

    names.append("LHipPitch")
    times.append([1.6])
    keys.append([-0.44797])

    names.append("LHipRoll")
    times.append([1.6])
    keys.append([0.00302601])

    names.append("LHipYawPitch")
    times.append([1.6])
    keys.append([-0.00609398])

    names.append("LKneePitch")
    times.append([1.6])
    keys.append([0.702614])

    names.append("LShoulderPitch")
    times.append([1.6, 3.76])
    keys.append([1.41737, -0.733294])

    names.append("LShoulderRoll")
    times.append([1.6, 3.76])
    keys.append([0.28068, -0.173384])

    names.append("LWristYaw")
    times.append([1.6, 3.76])
    keys.append([-0.0614018, -0.00924587])

    names.append("RAnklePitch")
    times.append([1.6])
    keys.append([-0.352778])

    names.append("RAnkleRoll")
    times.append([1.6])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([1.6, 3.76])
    keys.append([0.995524, 1.53251])

    names.append("RElbowYaw")
    times.append([1.6, 3.76])
    keys.append([1.39905, 1.34221])

    names.append("RHand")
    times.append([1.6, 3.76])
    keys.append([0.2336, 0.0412])

    names.append("RHipPitch")
    times.append([1.6])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([1.6])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([1.6])
    keys.append([-0.00609398])

    names.append("RKneePitch")
    times.append([1.6])
    keys.append([0.702614])

    names.append("RShoulderPitch")
    times.append([1.6, 3.76])
    keys.append([1.41737, -0.728608])

    names.append("RShoulderRoll")
    times.append([1.6, 3.76])
    keys.append([-0.28068, 0.130348])

    names.append("RWristYaw")
    times.append([1.6, 3.76])
    keys.append([0.0614018, 0.51078])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_8_tilt_head(motionProxy):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.16, 2.24])
    keys.append([0.00916195, 0.325166])

    names.append("HeadYaw")
    times.append([1.16, 2.24])
    keys.append([-0.021518, -0.895898])

    names.append("LAnklePitch")
    times.append([1.16])
    keys.append([-0.352778])

    names.append("LAnkleRoll")
    times.append([1.16])
    keys.append([-0.00157595])

    names.append("LElbowRoll")
    times.append([1.16, 2.24])
    keys.append([-0.995524, -1.54462])

    names.append("LElbowYaw")
    times.append([1.16, 2.24])
    keys.append([-1.39905, -1.13213])

    names.append("LHand")
    times.append([1.16, 2.24])
    keys.append([0.2336, 0.6428])

    names.append("LHipPitch")
    times.append([1.16])
    keys.append([-0.44797])

    names.append("LHipRoll")
    times.append([1.16])
    keys.append([0.00302601])

    names.append("LHipYawPitch")
    times.append([1.16])
    keys.append([-0.00609398])

    names.append("LKneePitch")
    times.append([1.16])
    keys.append([0.702614])

    names.append("LShoulderPitch")
    times.append([1.16, 2.24])
    keys.append([1.41737, 0.217786])

    names.append("LShoulderRoll")
    times.append([1.16, 2.24])
    keys.append([0.28068, -0.18719])

    names.append("LWristYaw")
    times.append([1.16, 2.24])
    keys.append([-0.0614018, -0.216336])

    names.append("RAnklePitch")
    times.append([1.16])
    keys.append([-0.352778])

    names.append("RAnkleRoll")
    times.append([1.16])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([1.16, 2.24])
    keys.append([0.995524, 0.998676])

    names.append("RElbowYaw")
    times.append([1.16, 2.24])
    keys.append([1.39905, 0.808376])

    names.append("RHand")
    times.append([1.16, 2.24])
    keys.append([0.2336, 0.0436])

    names.append("RHipPitch")
    times.append([1.16])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([1.16])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([1.16])
    keys.append([-0.00609398])

    names.append("RKneePitch")
    times.append([1.16])
    keys.append([0.702614])

    names.append("RShoulderPitch")
    times.append([1.16, 2.24])
    keys.append([1.41737, 1.43126])

    names.append("RShoulderRoll")
    times.append([1.16, 2.24])
    keys.append([-0.28068, -0.159578])

    names.append("RWristYaw")
    times.append([1.16, 2.24])
    keys.append([0.0614018, -0.108956])


    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


    time.sleep(2)


    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.08, 2.28])
    keys.append([0.325166, 0.00916195])

    names.append("HeadYaw")
    times.append([1.08, 2.28])
    keys.append([-0.895898, -0.021518])

    names.append("LAnklePitch")
    times.append([2.28])
    keys.append([-0.352778])

    names.append("LAnkleRoll")
    times.append([2.28])
    keys.append([-0.00157595])

    names.append("LElbowRoll")
    times.append([1.08, 2.28])
    keys.append([-1.54462, -0.995524])

    names.append("LElbowYaw")
    times.append([1.08, 2.28])
    keys.append([-1.13213, -1.39905])

    names.append("LHand")
    times.append([1.08, 2.28])
    keys.append([0.6428, 0.2336])

    names.append("LHipPitch")
    times.append([2.28])
    keys.append([-0.44797])

    names.append("LHipRoll")
    times.append([2.28])
    keys.append([0.00302601])

    names.append("LHipYawPitch")
    times.append([2.28])
    keys.append([-0.00609398])

    names.append("LKneePitch")
    times.append([2.28])
    keys.append([0.702614])

    names.append("LShoulderPitch")
    times.append([1.08, 2.28])
    keys.append([0.217786, 1.41737])

    names.append("LShoulderRoll")
    times.append([1.08, 2.28])
    keys.append([-0.18719, 0.28068])

    names.append("LWristYaw")
    times.append([1.08, 2.28])
    keys.append([-0.216336, -0.0614018])

    names.append("RAnklePitch")
    times.append([2.28])
    keys.append([-0.352778])

    names.append("RAnkleRoll")
    times.append([2.28])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([1.08, 2.28])
    keys.append([0.998676, 0.995524])

    names.append("RElbowYaw")
    times.append([1.08, 2.28])
    keys.append([0.808376, 1.39905])

    names.append("RHand")
    times.append([1.08, 2.28])
    keys.append([0.0436, 0.2336])

    names.append("RHipPitch")
    times.append([2.28])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([2.28])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([2.28])
    keys.append([-0.00609398])

    names.append("RKneePitch")
    times.append([2.28])
    keys.append([0.702614])

    names.append("RShoulderPitch")
    times.append([1.08, 2.28])
    keys.append([1.43126, 1.41737])

    names.append("RShoulderRoll")
    times.append([1.08, 2.28])
    keys.append([-0.159578, -0.28068])

    names.append("RWristYaw")
    times.append([1.08, 2.28])
    keys.append([-0.108956, 0.0614018])


    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_9_nod(motionProxy):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()
    names.append("HeadPitch")
    times.append([1.16, 2.52, 3.84, 5.12, 6.44])
    keys.append([0.024502, 0.511469, 0.024502, 0.511469, 0.024502])

    names.append("HeadYaw")
    times.append([1.16, 2.52, 3.84, 5.12, 6.44])
    keys.append([-0.024586, -0.024586, -0.0245859, -0.0245859, -0.0245859])

    names.append("LAnklePitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.352862, -0.352862, -0.352862])

    names.append("LAnkleRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.00609398, -0.00609397, -0.00609397])

    names.append("LElbowRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.998592, -0.998592, -0.998592])

    names.append("LElbowYaw")
    times.append([1.16, 3.84, 6.44])
    keys.append([-1.35763, -1.35763, -1.35763])

    names.append("LHand")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.2612, 0.2612, 0.2612])

    names.append("LHipPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.450954, -0.450955, -0.450955])

    names.append("LHipRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.00157595, 0.00157595, 0.00157595])

    names.append("LHipYawPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([4.19617e-05, 4.19617e-05, 4.19617e-05])

    names.append("LKneePitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.707132, 0.707132, 0.707132])

    names.append("LShoulderPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([1.40357, 1.40357, 1.40357])

    names.append("LShoulderRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.262272, 0.262272, 0.262272])

    names.append("LWristYaw")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.023052, -0.023052, -0.023052])

    names.append("RAnklePitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.346642, -0.346642, -0.346642])

    names.append("RAnkleRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([4.19617e-05, 4.19617e-05, 4.19617e-05])

    names.append("RElbowRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.975666, 0.975665, 0.975665])

    names.append("RElbowYaw")
    times.append([1.16, 3.84, 6.44])
    keys.append([1.36675, 1.36675, 1.36675])

    names.append("RHand")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.244, 0.244, 0.244])

    names.append("RHipPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.454106, -0.454105, -0.454105])

    names.append("RHipRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.0061779, 0.00617791, 0.00617791])

    names.append("RHipYawPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([4.19617e-05, 4.19617e-05, 4.19617e-05])

    names.append("RKneePitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.699546, 0.699545, 0.699545])

    names.append("RShoulderPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([1.4328, 1.4328, 1.4328])

    names.append("RShoulderRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.270026, -0.270025, -0.270025])

    names.append("RWristYaw")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.0123138, -0.0123138, -0.0123138])


    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_confused(motionProxy):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.429478, 0.420274, 0.479767, 0.332836])

    names.append("HeadYaw")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.354396, -0.47865, -0.193326, 0.50311])

    names.append("LAnklePitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.34826, -0.34826, -0.352862, -0.349794])

    names.append("LAnkleRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.00771189, 0.00771189, 0.00771189, 0.00771189])

    names.append("LElbowRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-1.00166, -0.990922, -0.990922, -0.990922])

    names.append("LElbowYaw")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-1.35456, -1.38678, -1.38678, -1.38678])

    names.append("LHand")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.4112, 0.4112, 0.4112, 0.4112])

    names.append("LHipPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.44942, -0.44942, -0.44942, -0.450954])

    names.append("LHipRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.00302601, -0.00302601, -0.00302601, -0.00302601])

    names.append("LHipYawPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.00157595, -0.00762796, 0.00310993, 0.00310993])

    names.append("LKneePitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.69486, 0.704064, 0.696394, 0.704064])

    names.append("LShoulderPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([1.54163, 1.52782, 1.52782, 1.52782])

    names.append("LShoulderRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.0858622, 0.098134, 0.098134, 0.0873961])

    names.append("LWristYaw")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.0168321, -0.01845, -0.01845, -0.01845])

    names.append("RAnklePitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.360448, -0.360448, -0.360448, -0.34971])

    names.append("RAnkleRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.00609398, -0.00609398, -0.00609398, -0.00609398])

    names.append("RElbowRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([1.12907, 1.16895, 1.15821, 1.15208])

    names.append("RElbowYaw")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.952572, 0.820648, 0.95564, 0.943368])

    names.append("RHand")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.0391999, 0.0391999, 0.0391999, 0.0391999])

    names.append("RHipPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.44797, -0.472514, -0.451038, -0.444902])

    names.append("RHipRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.00157595, 0.00157595, 0.00157595, 0.00157595])

    names.append("RHipYawPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.00157595, -0.00762796, 0.00310993, 0.00310993])

    names.append("RKneePitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.704148, 0.702614, 0.698012, 0.690342])

    names.append("RShoulderPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.724006, -0.279146, -0.77923, -0.776162])

    names.append("RShoulderRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.328318, -0.277696, -0.323716, -0.319114])

    names.append("RWristYaw")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.314428, 0.30369, 0.30369, 0.297554])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_standattention(motionProxy):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.68])
    keys.append([0.00916195])

    names.append("HeadYaw")
    times.append([0.68])
    keys.append([-0.021518])

    names.append("LAnklePitch")
    times.append([0.68])
    keys.append([-0.352862])

    names.append("LAnkleRoll")
    times.append([0.68])
    keys.append([4.19617e-05])

    names.append("LElbowRoll")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([-0.995524, -0.0689881, -0.0349066, -1.08756])

    names.append("LElbowYaw")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([-1.39905, -0.326784, -0.971064, 0.53379])

    names.append("LHand")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([0.2336, 0.0148, 0.0184, 0.0184])

    names.append("LHipPitch")
    times.append([0.68])
    keys.append([-0.447886])

    names.append("LHipRoll")
    times.append([0.68])
    keys.append([0.00310993])

    names.append("LHipYawPitch")
    times.append([0.68])
    keys.append([-0.00609398])

    names.append("LKneePitch")
    times.append([0.68])
    keys.append([0.699462])

    names.append("LShoulderPitch")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([1.41737, 1.72571, 2.08567, 2.05245])

    names.append("LShoulderRoll")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([0.28068, 0.0137641, -0.239346, -0.131966])

    names.append("LWristYaw")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([-0.0614018, -1.56165, -0.771644, -1.55245])

    names.append("RAnklePitch")
    times.append([0.68])
    keys.append([-0.352778])

    names.append("RAnkleRoll")
    times.append([0.68])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([0.997142, 0.181054, 0.046062, 1.08305])

    names.append("RElbowYaw")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([1.36215, 0.70253, 0.854396, -0.921976])

    names.append("RHand")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([0.246, 0.0700001, 0.0492001, 0.0704])

    names.append("RHipPitch")
    times.append([0.68])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([0.68])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([0.68])
    keys.append([-0.00609398])

    names.append("RKneePitch")
    times.append([0.68])
    keys.append([0.702614])

    names.append("RShoulderPitch")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([1.42666, 1.68131, 2.06787, 1.93902])

    names.append("RShoulderRoll")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([-0.265424, -0.0798099, 0.176368, 0.0643861])

    names.append("RWristYaw")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([-0.016916, 0.92496, 0.515382, 0.834454])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err




    time.sleep(5)

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([5.04])
    keys.append([0.00916195])

    names.append("HeadYaw")
    times.append([5.04])
    keys.append([-0.021518])

    names.append("LAnklePitch")
    times.append([5.04])
    keys.append([-0.352778])

    names.append("LAnkleRoll")
    times.append([5.04])
    keys.append([-0.00157595])

    names.append("LElbowRoll")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([-1.08756, -0.0349066, -0.0689881, -0.995524])

    names.append("LElbowYaw")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([0.53379, -0.971064, -0.326784, -1.39905])

    names.append("LHand")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([0.0184, 0.0184, 0.0148, 0.2336])

    names.append("LHipPitch")
    times.append([5.04])
    keys.append([-0.44797])

    names.append("LHipRoll")
    times.append([5.04])
    keys.append([0.00302601])

    names.append("LHipYawPitch")
    times.append([5.04])
    keys.append([-0.00609398])

    names.append("LKneePitch")
    times.append([5.04])
    keys.append([0.702614])

    names.append("LShoulderPitch")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([2.05245, 2.08567, 1.72571, 1.41737])

    names.append("LShoulderRoll")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([-0.131966, -0.239346, 0.0137641, 0.28068])

    names.append("LWristYaw")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([-1.55245, -0.771644, -1.56165, -0.0614018])

    names.append("RAnklePitch")
    times.append([5.04])
    keys.append([-0.352778])

    names.append("RAnkleRoll")
    times.append([5.04])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([1.08756, 0.0349066, 0.0689881, 0.995524])

    names.append("RElbowYaw")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([-0.53379, 0.971064, 0.326784, 1.39905])

    names.append("RHand")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([0.0184, 0.0184, 0.0148, 0.2336])

    names.append("RHipPitch")
    times.append([5.04])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([5.04])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([5.04])
    keys.append([-0.00609398])

    names.append("RKneePitch")
    times.append([5.04])
    keys.append([0.702614])

    names.append("RShoulderPitch")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([2.05245, 2.08567, 1.72571, 1.41737])

    names.append("RShoulderRoll")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([0.131966, 0.239346, -0.0137641, -0.28068])

    names.append("RWristYaw")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([1.55245, 0.771644, 1.56165, 0.0614018])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


    time.sleep(3)

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.12, 3.4])
    keys.append([0.25, 0.00916195])

    names.append("HeadYaw")
    times.append([1.12, 3.4])
    keys.append([-0.092082, -0.021518])

    names.append("LAnklePitch")
    times.append([1.12, 3.4])
    keys.append([-1.16281, -0.352778])

    names.append("LAnkleRoll")
    times.append([1.12, 3.4])
    keys.append([0.0061779, -0.00157595])

    names.append("LElbowRoll")
    times.append([1.12, 3.4])
    keys.append([-1.54163, -0.995524])

    names.append("LElbowYaw")
    times.append([1.12, 3.4])
    keys.append([-0.62438, -1.39905])

    names.append("LHand")
    times.append([1.12, 3.4])
    keys.append([0.4936, 0.2336])

    names.append("LHipPitch")
    times.append([1.12, 3.4])
    keys.append([-0.811444, -0.44797])

    names.append("LHipRoll")
    times.append([1.12, 3.4])
    keys.append([0.314512, 0.00302601])

    names.append("LHipYawPitch")
    times.append([1.12, 3.4])
    keys.append([-0.18097, -0.00609398])

    names.append("LKneePitch")
    times.append([1.12, 3.4])
    keys.append([2.10921, 0.702614])

    names.append("LShoulderPitch")
    times.append([1.12, 3.4])
    keys.append([0.674918, 1.41737])

    names.append("LShoulderRoll")
    times.append([1.12, 3.4])
    keys.append([-0.291502, 0.28068])

    names.append("LWristYaw")
    times.append([1.12, 3.4])
    keys.append([-1.11526, -0.0614018])

    names.append("RAnklePitch")
    times.append([1.12, 3.4])
    keys.append([-1.15506, -0.352778])

    names.append("RAnkleRoll")
    times.append([1.12, 3.4])
    keys.append([0.0123138, 0.00157595])

    names.append("RElbowRoll")
    times.append([1.12, 3.4])
    keys.append([0.905102, 0.995524])

    names.append("RElbowYaw")
    times.append([1.12, 3.4])
    keys.append([0.766958, 1.39905])

    names.append("RHand")
    times.append([1.12, 3.4])
    keys.append([0.0516, 0.2336])

    names.append("RHipPitch")
    times.append([1.12, 3.4])
    keys.append([-0.282298, -0.44797])

    names.append("RHipRoll")
    times.append([1.12, 3.4])
    keys.append([0.342124, -0.00302601])

    names.append("RHipYawPitch")
    times.append([1.12, 3.4])
    keys.append([-0.18097, -0.00609398])

    names.append("RKneePitch")
    times.append([1.12, 3.4])
    keys.append([1.62148, 0.702614])

    names.append("RShoulderPitch")
    times.append([1.12, 3.4])
    keys.append([1.50796, 1.41737])

    names.append("RShoulderRoll")
    times.append([1.12, 3.4])
    keys.append([0.167164, -0.28068])

    names.append("RWristYaw")
    times.append([1.12, 3.4])
    keys.append([-0.139636, 0.0614018])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err

def gangnam_style(postureProxy,audioProxy,motionProxy):
    postureProxy.goToPosture("StandInit", 1.0)

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.96, 1.32, 1.76, 2, 2.24, 2.48, 2.72, 2.96, 3.2, 3.44, 3.68, 3.92, 4.16, 4.4, 4.64, 4.88, 5.12, 5.36, 5.6, 5.84, 6.08, 6.32, 6.56, 6.8, 7.04, 7.28, 7.52, 7.76, 8, 8.52, 8.76, 9, 9.24, 9.48, 9.72, 9.96, 10.2, 10.44, 10.68, 10.92, 11.16, 11.4, 11.64, 11.88, 12.12, 12.36, 12.72, 13.04, 13.28, 13.52, 13.76, 14, 14.24, 14.48, 14.72, 14.96, 15.2, 15.44, 15.68, 15.92, 16.24, 16.64])
    keys.append([-0.392746, -0.392746, -0.392746, -0.105767, -0.392746, -0.105767, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.0808051, -0.0139626, -0.392746, -0.0139626, -0.392746, -0.0139626, -0.392746, -0.0139626, -0.392746, -0.0139626, -0.392746, -0.0139626, -0.392746, -0.0139626, -0.375714, -0.434587])

    names.append("HeadYaw")
    times.append([0.96, 1.32, 1.76, 2, 2.24, 2.48, 2.72, 2.96, 3.2, 3.44, 3.68, 3.92, 4.16, 4.4, 4.64, 4.88, 5.12, 5.36, 5.6, 5.84, 6.08, 6.32, 6.56, 6.8, 7.04, 7.28, 7.52, 7.76, 8, 8.52, 9, 9.48, 9.96, 10.44, 10.92, 11.4, 11.88, 12.36, 13.28, 14.24, 14.72, 15.68, 16.24, 16.64])
    keys.append([0.00455999, 0.00455999, 0.00455999, -0.00157595, 0.00455999, -0.00157595, 0.00455999, -0.00157595, 0.00455999, -0.00157595, 0.00455999, -0.00157595, 0.00455999, -0.00157595, 0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, 0.638352, 0.638352, -0.639567, -0.639567, -0.0592826, -0.0153821])

    names.append("LAnklePitch")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([0.091998, 0.091998, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.144154, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, -0.14364, -0.119694])

    names.append("LAnkleRoll")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([-0.118076, -0.118076, -0.118076, -0.116542, -0.118076, -0.116542, -0.118076, -0.116542, -0.118076, -0.116542, -0.118076, -0.116542, -0.118076, -0.116542, -0.118076, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.112081, -0.116542])

    names.append("LElbowRoll")
    times.append([0.96, 1.32, 1.72, 1.96, 2.2, 2.44, 2.68, 2.92, 3.16, 3.4, 3.64, 3.88, 4.12, 4.36, 4.84, 5.08, 5.32, 5.56, 5.8, 6.04, 6.28, 6.52, 6.76, 7, 7.24, 7.48, 7.72, 7.96, 8.4, 8.64, 8.88, 9.12, 9.36, 9.6, 9.84, 10.08, 10.32, 10.56, 10.8, 11.04, 11.28, 11.52, 11.76, 12, 12.24, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([-1.52782, -1.52782, -1.52782, -1.52169, -1.52782, -1.52169, -1.52782, -1.52169, -1.52782, -1.52169, -1.52782, -1.52169, -1.52782, -1.52169, -0.550747, -0.349794, -0.550747, -0.349794, -0.550747, -0.349794, -0.550747, -0.349794, -0.550747, -0.349794, -0.550747, -0.349794, -0.550747, -0.349794, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -1.33657, -1.54462, -1.33657, -1.54462, -1.33657, -1.54462, -1.33657, -1.54462, -1.33657, -1.54462, -1.33657, -1.54462, -1.33657, -0.15575, -0.0349068])

    names.append("LElbowYaw")
    times.append([0.96, 1.32, 1.72, 1.96, 2.2, 2.44, 2.68, 2.92, 3.16, 3.4, 3.64, 3.88, 4.12, 4.36, 4.84, 5.08, 5.32, 5.56, 5.8, 6.04, 6.28, 6.52, 6.76, 7, 7.24, 7.48, 7.72, 7.96, 8.48, 8.72, 8.96, 9.2, 9.44, 9.68, 9.92, 10.16, 10.4, 10.64, 10.88, 11.12, 11.36, 11.6, 11.84, 12.08, 12.32, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([-0.236277, -0.236277, -0.236277, -0.145772, -0.236277, -0.145772, -0.236277, -0.145772, -0.236277, -0.145772, -0.236277, -0.145772, -0.236277, -0.145772, 0.380475, -1.06302, 0.380475, -1.06302, 0.380475, -1.06302, 0.380475, -1.06302, 0.380475, -1.06302, 0.380475, -1.06302, 0.380475, -1.06302, -0.644027, -0.0801321, -0.644027, -0.0801321, -0.644027, -0.0801321, -0.644027, -0.0801321, -0.644027, -0.0801319, -0.644027, -0.0801321, -0.644027, -0.0801321, -0.644027, -0.0801321, -0.644027, 0.038455, 0.0383972, 0.038455, 0.0383972, 0.038455, 0.0383972, 0.038455, 0.0383972, 0.038455, 0.0383972, 0.038455, 0.0383972, 0.038455, -1.59015, -1.82551])

    names.append("LHand")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.4, 8.64, 8.88, 9.12, 9.36, 9.6, 9.84, 10.08, 10.32, 10.56, 10.8, 11.04, 11.28, 11.52, 11.76, 12, 12.24, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0, 0.00479996, 0, 0.00479996, 0, 0.00479996, 0, 0.00479996, 0, 0.00479996, 0, 0.00479996, 0.875715, 0.9996])

    names.append("LHipPitch")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([0.0123138, 0.0123138, 0.0123138, -0.358915, 0.0123138, -0.358915, 0.0123138, -0.358915, 0.0123138, -0.358915, 0.0123138, -0.358915, 0.0123138, -0.358915, 0.0521979, -0.318285, 0.0194225, -0.334564, 0.0106959, -0.334564, 0.0106959, -0.334564, 0.0106959, -0.334564, 0.0106959, -0.334564, 0.0106959, -0.334564, 0.0106959, -0.334564, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.28663, 0.129154, -0.31281, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.397396, 0.481718])

    names.append("LHipRoll")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([0.112024, 0.112024, 0.112024, 0.115092, 0.112024, 0.115092, 0.112024, 0.115092, 0.112024, 0.115092, 0.112024, 0.115092, 0.112024, 0.115092, 0.112024, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.113546, 0.11816])

    names.append("LHipYawPitch")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([-0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733])

    names.append("LKneePitch")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([-0.090548, -0.090548, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.000676226, -0.090548])

    names.append("LShoulderPitch")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.4, 8.64, 8.88, 9.12, 9.36, 9.6, 9.84, 10.08, 10.32, 10.56, 10.8, 11.04, 11.28, 11.52, 11.76, 12, 12.24, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([0.226991, 0.226991, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, -0.730907, -1.44345, -1.03006, -1.44345, -1.03006, -1.44345, -1.03006, -1.44345, -1.03006, -1.44345, -1.03006, -1.44345, -1.03006, -1.44345, -0.331613, 0.00878002, -0.331613, 0.00878005, -0.331613, 0.00878005, -0.331613, 0.00878005, -0.331613, 0.00878, -0.331613, 0.00878, -0.331613, 0.00878, -0.331613, 0.00878, -0.331613, 1.53865, 1.53938, 1.53865, 1.53938, 1.53865, 1.53938, 1.53865, 1.53938, 1.53865, 1.53938, 1.53865, 1.53938, 1.53865, 1.73828, 1.76713])

    names.append("LShoulderRoll")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.4, 8.64, 8.88, 9.12, 9.36, 9.6, 9.84, 10.08, 10.32, 10.56, 10.8, 11.04, 11.28, 11.52, 11.76, 12, 12.24, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([0.121144, 0.121144, 0.121144, 0.12728, 0.121144, 0.12728, 0.121144, 0.12728, 0.121144, 0.12728, 0.121144, 0.12728, 0.121144, 0.12728, 0.248551, 0.331386, 0.248551, 0.331386, 0.248551, 0.331386, 0.248551, 0.331386, 0.248551, 0.331386, 0.248551, 0.331386, 0.248551, 0.331386, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, 0.788697, 0.909316, 0.788697, 0.909316, 0.788697, 0.909316, 0.788697, 0.909316, 0.788697, 0.909316, 0.788697, 0.909316, 0.788697, 0.530231, 0.506179])

    names.append("LWristYaw")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.4, 8.64, 8.88, 9.12, 9.36, 9.6, 9.84, 10.08, 10.32, 10.56, 10.8, 11.04, 11.28, 11.52, 11.76, 12, 12.24, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([0.105804, 0.105804, 0.105804, 0.107338, 0.105804, 0.107338, 0.105804, 0.107338, 0.105804, 0.107338, 0.105804, 0.107338, 0.105804, 0.107338, -0.512313, -0.115008, -0.512313, -0.115008, -0.512313, -0.115008, -0.512313, -0.115008, -0.512313, -0.115008, -0.512313, -0.115008, -0.512313, -0.115008, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, -1.51511, -1.79636])

    names.append("RAnklePitch")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([0.101286, 0.101286, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.145772, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, -0.14204, -0.118076])

    names.append("RAnkleRoll")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([0.075208, 0.075208, 0.075208, 0.073674, 0.075208, 0.073674, 0.075208, 0.073674, 0.075208, 0.073674, 0.075208, 0.073674, 0.075208, 0.073674, 0.075208, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.0776441, 0.073674])

    names.append("RElbowRoll")
    times.append([0.96, 1.32, 1.72, 1.96, 2.2, 2.44, 2.68, 2.92, 3.16, 3.4, 3.64, 3.88, 4.12, 4.36, 4.84, 5.08, 5.32, 5.56, 5.8, 6.04, 6.28, 6.52, 6.76, 7, 7.24, 7.48, 7.72, 7.96, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([0.349794, 0.349794, 0.349794, 0.550747, 0.349794, 0.550747, 0.349794, 0.550747, 0.349794, 0.550747, 0.349794, 0.550747, 0.349794, 0.550747, 1.52169, 1.52782, 1.52169, 1.52782, 1.52169, 1.52782, 1.52169, 1.52782, 1.52169, 1.52782, 1.52169, 1.52782, 1.52169, 1.52782, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 1.33276, 1.54296, 1.33276, 1.54296, 1.33276, 1.54296, 1.33276, 1.54296, 1.33276, 1.54296, 1.33276, 1.54296, 1.33276, 0.170923, 0.0521979])

    names.append("RElbowYaw")
    times.append([0.96, 1.32, 1.72, 1.96, 2.2, 2.44, 2.68, 2.92, 3.16, 3.4, 3.64, 3.88, 4.12, 4.36, 4.84, 5.08, 5.32, 5.56, 5.8, 6.04, 6.28, 6.52, 6.76, 7, 7.24, 7.48, 7.72, 7.96, 8.44, 8.68, 8.92, 9.16, 9.4, 9.64, 9.88, 10.12, 10.36, 10.6, 10.84, 11.08, 11.32, 11.56, 11.8, 12.04, 12.28, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([1.06302, 1.06302, 1.06302, -0.380475, 1.06302, -0.380475, 1.06302, -0.380475, 1.06302, -0.380475, 1.06302, -0.380475, 1.06302, -0.380475, 0.145772, 0.236277, 0.145772, 0.236277, 0.145772, 0.236277, 0.145772, 0.236277, 0.145772, 0.236277, 0.145772, 0.236277, 0.145772, 0.236277, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, -0.0384695, -0.0377698, -0.0384695, -0.0377698, -0.0384695, -0.0377698, -0.0384695, -0.0377698, -0.0384695, -0.0377698, -0.0384695, -0.0377698, -0.0384695, 1.59007, 1.82542])

    names.append("RHand")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0, 0.00440001, 0, 0.00440001, 0, 0.00440001, 0, 0.00440001, 0, 0.00440001, 0, 0.00440001, 0.875526, 0.9996])

    names.append("RHipPitch")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([0.0106959, 0.0106959, 0.0106959, -0.358999, 0.0106959, -0.358999, 0.0106959, -0.358999, 0.0106959, -0.358999, 0.0106959, -0.358999, 0.0106959, -0.358999, 0.052114, -0.318201, 0.0210405, -0.33448, 0.0123138, -0.33448, 0.0123138, -0.33448, 0.0123138, -0.33448, 0.0123138, -0.33448, 0.0123138, -0.33448, 0.0123138, -0.33448, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.28663, 0.129154, -0.31281, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.397321, 0.481634])

    names.append("RHipRoll")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([-0.061318, -0.061318, -0.061318, -0.0643861, -0.061318, -0.0643861, -0.061318, -0.0643861, -0.061318, -0.0643861, -0.061318, -0.0643861, -0.061318, -0.0643861, -0.0628521, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.0710375, -0.06592])

    names.append("RHipYawPitch")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([-0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733])

    names.append("RKneePitch")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
    keys.append([-0.0923279, -0.0923279, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.091998, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.00243924, -0.0923279])

    names.append("RShoulderPitch")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([-1.44345, -1.44345, -1.44345, -1.03084, -1.44345, -1.03084, -1.44345, -1.03084, -1.44345, -1.03084, -1.44345, -1.03084, -1.44345, -0.733274, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 1.53849, 1.53857, 1.53849, 1.53857, 1.53849, 1.53857, 1.53849, 1.53857, 1.53849, 1.53857, 1.53849, 1.53857, 1.53849, 1.73967, 1.76875])

    names.append("RShoulderRoll")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([-0.331386, -0.331386, -0.331386, -0.248551, -0.331386, -0.248551, -0.331386, -0.248551, -0.331386, -0.248551, -0.331386, -0.248551, -0.331386, -0.248551, -0.12728, -0.121144, -0.12728, -0.121144, -0.12728, -0.121144, -0.12728, -0.121144, -0.12728, -0.121144, -0.12728, -0.121144, -0.12728, -0.121144, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, -0.795964, -0.912095, -0.795964, -0.912095, -0.795964, -0.912095, -0.795964, -0.912095, -0.795964, -0.912095, -0.795964, -0.912095, -0.795964, -0.50207, -0.474047])

    names.append("RWristYaw")
    times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
    keys.append([0.115008, 0.115008, 0.115008, 0.512313, 0.115008, 0.512313, 0.115008, 0.512313, 0.115008, 0.512313, 0.115008, 0.512313, 0.115008, 0.512313, -0.107338, -0.105804, -0.107338, -0.105804, -0.107338, -0.105804, -0.107338, -0.105804, -0.107338, -0.105804, -0.107338, -0.105804, -0.107338, -0.105804, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, 1.50029, 1.7794])

    
    audioProxy.post.playFile("/home/daryl/HCR/Prezence/kinetic_feedback/gangnamstyle.wav",0.5,0.5)
    motionProxy.angleInterpolation(names, keys, times, True)
    postureProxy.goToPosture("StandInit", 1.0)

def taichiquan(postureProxy,audioProxy,motionProxy):

    postureProxy.goToPosture("StandInit", 1.0)
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([0, 8.95233e-08, -4.76838e-07, 8.89455e-08, 1.04976e-07, 0.331613, 0.314159, 9.19019e-08, -0.331613, 0.139626, -0.0872665, 0.139626, 0.383972, 0.558505, 0.383972, -0.331613, 0.139626, -0.0872665, 0.139626, 0.383972, 0, -0.190258])

    names.append("HeadYaw")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([0, 8.42936e-08, 8.42938e-08, 8.42938e-08, -4.76838e-07, 0.314159, -0.296706, -1.18682, -0.279253, 0.20944, 1.5708, 0.20944, 0.139626, 0, -0.139626, 0.279253, -0.20944, -1.5708, -0.20944, -0.139626, 0, -0.00310993])

    names.append("LAnklePitch")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 43.4, 44.4, 46.2, 50])
    keys.append([1.00403e-07, 0, -0.303687, 0, 0, -0.647517, -0.610865, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -0.872665, -0.741765, 0, 1.00403e-07, 0.523599, 1.00403e-07, -0.555015, -0.654498, -1.0472, 0.033706])

    names.append("LAnkleRoll")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 33.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([0.0523599, 0.122173, 0.174533, -0.10472, -0.10472, 0.174533, -0.261799, 0.0628318, 0.174533, 0.0872665, 0.0872665, 0.0872665, 0.174533, 0, -0.240855, -0.55676, -0.424115, -0.349066, 0, -0.349066, -0.312414, 0, -0.05058])

    names.append("LElbowRoll")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 45.4, 46.2, 50])
    keys.append([0, -0.698132, -1.0472, 0, 0, -1.65806, -0.959931, -1.48353, -1.01229, -1.01229, 0, -1.01229, -1.01229, -0.890118, -0.855211, -1.11701, -0.855211, -1.25664, -0.855211, -0.855211, -0.994838, -1.4207, -0.38806])

    names.append("LElbowYaw")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 45.4, 46.2, 50])
    keys.append([-1.5708, -1.5708, -1.5708, -1.5708, -1.5708, -0.383972, 0, 0, 0, 0, 0, 0, 0, 0.20944, 0.191986, -0.418879, -0.418879, -0.0872665, -0.418879, 0.191986, -0.378736, -0.244346, -1.18276])

    names.append("LHand")
    times.append([3, 50])
    keys.append([0, 0.2984])

    names.append("LHipPitch")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([0, 0, -0.349066, 0, 0, -0.698132, -0.610865, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -0.872665, -0.741765, -0.122173, -0.872665, 0, -0.872665, -0.654498, -1.0472, 0.216335])

    names.append("LHipRoll")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 33.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([-0.0523599, -0.122173, -0.174533, 0.10472, 0.10472, -0.174533, 0.174533, 0.420624, 0.528835, 0.610865, 0.610865, 0.610865, 0.349066, 0, -0.261799, 0.251327, 0.261799, 0.139626, 0.698132, 0.139626, -0.261799, 0, 0.0414601])

    names.append("LHipYawPitch")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([-0.10821, -0.120428, -0.1309, -0.120428, -0.143117, -0.167552, -0.0994838, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.0680678, 0, -0.194775])

    names.append("LKneePitch")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([0, 0, 0.698132, -9.9341e-08, -9.9341e-08, 1.39626, 1.22173, 2.0944, 2.0944, 2.0944, 2.0944, 2.0944, 2.1101, 1.74533, 1.48353, 0.122173, 1.74533, 0, 1.74533, 1.309, 2.0944, -0.0890141])

    names.append("LShoulderPitch")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([1.5708, 1.91986, 2.0944, 1.5708, 0, 0.366519, 0.349066, 0.191986, -0.802851, -0.174533, -0.296706, -0.174533, 0.523599, 0.471239, 0.331613, -0.471239, 0.0698132, -0.0698132, 0.0698132, 0.331613, 1.69297, 1.52936])

    names.append("LShoulderRoll")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([0.174533, 0.349066, 0.174533, 0.174533, 0.174533, 0.698132, 0, 0.0872665, 0.174533, 0.401426, 1.15192, 0.401426, 0.401426, 0.174533, 0, 0.401426, 0, 0, 0, 0.20944, 0.942478, 0.107338])

    names.append("LWristYaw")
    times.append([3, 50])
    keys.append([-1.53589, 0.139552])

    names.append("RAnklePitch")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([1.00403e-07, 0, 0, 0, 0, -0.698132, -0.174533, 0, 0, 1.00403e-07, 0.523599, 1.00403e-07, -0.741765, -0.872665, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, 0.036858])

    names.append("RAnkleRoll")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([-0.0523599, 0.1309, 0.438078, 0.10472, 0.10472, 0.294961, 0.621337, 0.785398, 0.74351, 0.436332, 0, 0.349066, 0.261799, 0, -0.174533, -0.174533, -0.0872665, -0.0872665, -0.0628318, -0.0418879, 0, 0.0291878])

    names.append("RElbowRoll")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 45.4, 46.2, 50])
    keys.append([0, 0.698132, 1.0472, 2.57424e-07, 0, 1.23918, 1.64061, 0.0698132, 1.11701, 0.855211, 1.25664, 0.855211, 0.855211, 0.890118, 1.01229, 1.01229, 1.01229, 0.0349066, 1.01229, 1.01229, 1.13272, 1.36659, 0.395814])

    names.append("RElbowYaw")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 45.4, 46.2, 50])
    keys.append([1.5708, 1.5708, 1.5708, 1.5708, 1.5708, 0.191986, 0.349066, 1.5708, 0.418879, 0.418879, 0.0872665, 0.418879, -0.191986, -0.20944, 0, 0, 0, 0, 0, 0, 0.342085, 0.244346, 1.15966])

    names.append("RHand")
    times.append([3, 50])
    keys.append([0, 0.302])

    names.append("RHipPitch")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([0, 0, 0, 0, 0, -0.698132, -0.174533, -0.10472, -0.122173, -0.872665, 0, -0.872665, -0.741765, -0.872665, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, 0.214717])

    names.append("RHipRoll")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([0.0523599, -0.122173, -0.438078, -0.10472, -0.10472, -0.349066, -0.785398, -0.541052, -0.139626, -0.139626, -0.698132, -0.139626, 0.261799, 0, -0.349066, -0.539307, -0.610865, -0.610865, -0.610865, -0.532325, 0, -0.021434])

    names.append("RHipYawPitch")
    times.append([3, 5, 7, 9, 11, 13, 50])
    keys.append([-0.10821, -0.120428, -0.1309, -0.120428, -0.143117, -0.167552, -0.194775])

    names.append("RKneePitch")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([0, 0, 0, 0, 0, 1.39626, 0.349066, 0.122173, 0.122173, 1.74533, 0, 1.74533, 1.48353, 1.74533, 2.0944, 2.0944, 2.0944, 2.0944, 2.0944, 2.0944, 2.0944, -0.091998])

    names.append("RShoulderPitch")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([1.5708, 1.91986, 2.0944, 1.5708, 0, 0.174533, 0.610865, 1.0472, -0.471239, 0.0698132, -0.0698132, 0.0698132, 0.331613, 0.471239, 0.523599, -0.802851, -0.174533, -0.296706, -0.174533, 0.523599, 1.69297, 1.51563])

    names.append("RShoulderRoll")
    times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2, 28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
    keys.append([-0.174533, -0.174533, -0.349066, -0.174533, -0.174515, -0.0698132, -0.837758, -1.51844, -0.401426, 0, 0, 0, 0, -0.174533, -0.401426, -0.174533, -0.401426, -1.15192, -0.401426, -0.558505, -0.942478, -0.099752])

    names.append("RWristYaw")
    times.append([3, 50])
    keys.append([1.53589, 0.164096])

    
    audioProxy.post.playFile("/home/daryl/HCR/Prezence/kinetic_feedback/swiftswords_ext.mp3",0.5,0.5)
    motionProxy.angleInterpolation(names, keys, times, True)
    postureProxy.goToPosture("StandInit", 1.0)

def squat(motionProxy):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.6])
    keys.append([0.0674541])

    names.append("HeadYaw")
    times.append([0.6])
    keys.append([-0.0276539])

    names.append("LAnklePitch")
    times.append([0.6])
    keys.append([-1.18276])

    names.append("LAnkleRoll")
    times.append([0.6])
    keys.append([0.070606])

    names.append("LElbowRoll")
    times.append([0.6])
    keys.append([-1.03848])

    names.append("LElbowYaw")
    times.append([0.6])
    keys.append([-0.794654])

    names.append("LHand")
    times.append([0.6])
    keys.append([0.0192])

    names.append("LHipPitch")
    times.append([0.6])
    keys.append([-0.700996])

    names.append("LHipRoll")
    times.append([0.6])
    keys.append([-0.076658])

    names.append("LHipYawPitch")
    times.append([0.6])
    keys.append([-0.237728])

    names.append("LKneePitch")
    times.append([0.6])
    keys.append([2.10767])

    names.append("LShoulderPitch")
    times.append([0.6])
    keys.append([1.44959])

    names.append("LShoulderRoll")
    times.append([0.6])
    keys.append([0.0873961])

    names.append("LWristYaw")
    times.append([0.6])
    keys.append([0.0843279])

    names.append("RAnklePitch")
    times.append([0.6])
    keys.append([-1.1863])

    names.append("RAnkleRoll")
    times.append([0.6])
    keys.append([-0.078192])

    names.append("RElbowRoll")
    times.append([0.6])
    keys.append([1.02782])

    names.append("RElbowYaw")
    times.append([0.6])
    keys.append([0.823716])

    names.append("RHand")
    times.append([0.6])
    keys.append([0.0172])

    names.append("RHipPitch")
    times.append([0.6])
    keys.append([-0.698012])

    names.append("RHipRoll")
    times.append([0.6])
    keys.append([0.07214])

    names.append("RHipYawPitch")
    times.append([0.6])
    keys.append([-0.237728])

    names.append("RKneePitch")
    times.append([0.6])
    keys.append([2.10622])

    names.append("RShoulderPitch")
    times.append([0.6])
    keys.append([1.44967])

    names.append("RShoulderRoll")
    times.append([0.6])
    keys.append([-0.0844119])

    names.append("RWristYaw")
    times.append([0.6])
    keys.append([-0.0583339])


    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def begin_presentation():
    start = False
    syncFile = open('output/sync.txt', 'r')
    while not start:
        # read sync
        where = syncFile.tell()
        line = syncFile.readline()
        if not line or line in ['\n', '\r\n']:
            time.sleep(1)
            syncFile.seek(where)
        else:
            if line.rstrip('\n') == "start":
                start = True
    print "Sync File has announced start"

def end_presentation():
    start = False
    syncFile = open('output/sync.txt', 'r')
    while not start:
        # read sync
        where = syncFile.tell()
        line = syncFile.readline()
        if not line or line in ['\n', '\r\n']:
            time.sleep(1)
            syncFile.seek(where)
        else:
            if line.rstrip('\n') == "end":
                start = True
    print "Sync File has announced end"

def decode_input(char,motionProxy):
    if char == 1:
        gesture_1_handwave(motionProxy)

    elif char == 2:
        gesture_2_attention(motionProxy)

    elif char == 3:
        gesture_3_leaning(motionProxy)

    elif char == 4:
        gesture_4_shrugging(motionProxy)

    elif char ==5:
        gesture_5_arms(motionProxy)

    elif char ==6:
        gesture_6_bored(motionProxy)

    elif char ==7:
        gesture_7_coverears(motionProxy)

    elif char ==8:
        gesture_8_tilt_head(motionProxy)

    else:
        gesture_9_nod(motionProxy)
 
def main(robotIP,robotPort):

    # kinetic_feedbackfile = open('output/kinetic_feedback.txt', 'w')
    # kinetic_feedbackfile.close()


    #==================initialise the NAO===========================
    print "Initialising NAO"
    #Setting the Proxies
    try:
        motionProxy = ALProxy("ALMotion", robotIP, robotPort)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        ttsProxy = ALProxy("ALTextToSpeech", robotIP, robotPort)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, robotPort)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    try:
        animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, robotPort)    
    except Exception, e:
        print "Could not create proxy to ALAnimatedSpeech"
        print "Error was: ", e

    try:
        audioProxy = ALProxy("ALAudioPlayer", robotIP, robotPort)
    except Exception,e:
        print "Could not create proxy to ALAudioPlayer"
        print "Error was: ",e


    try:
        ledsProxy = ALProxy("ALLeds", robotIP, robotPort)
    except Exception,e:
        print "Could not create proxy to ALLeds"
        print "Error was: ",e



    # Turn on the Motors
    motionProxy.wakeUp()


    # ledsProxy.bIsRunning = True;
    # ledsProxy.bMustStop = False;

    # rDuration = 1.0;
    # ledsProxy.post.fadeRGB( "FaceLedsTop", 0x0000ff, rDuration );
    # ledsProxy.post.fadeRGB( "FaceLedsInternal", 0x00ff00, rDuration );
    # ledsProxy.post.fadeRGB( "FaceLedsBottom", 0x0000ff, rDuration );
    # ledsProxy.fadeRGB( "FaceLedsExternal", 0x0000ff, rDuration );

    # while( not ledsProxy.bMustStop ):
    #   ledsProxy=1.0
    #   ledsProxy.fadeRGB( "FaceLedsInternal", 0x000000, rTime );
    #   if( ledsProxy.bMustStop ):
    #     break;
    #   ledsProxy.fadeRGB( "FaceLedsInternal", 0x00ff00, rDuration );


    # gangnam_style(postureProxy,audioProxy,motionProxy)
    # taichiquan(postureProxy,audioProxy,motionProxy)


    # say the text with the local configuration
    animatedSpeechProxy.say("Please wait while I get ready, you can chill out now", gesture_confused)

    #StandUp
    StandUp(postureProxy)
    # motionProxy.rest()

    #==================Check for Presentation to Begin===========================
    time.sleep(8)

    animatedSpeechProxy.say("Please say go when you are ready and raise your arms in a right angled manner", gesture_confused)

    start = False
    syncFile = open('output/sync.txt', 'r')
    while not start:
        # read sync
        where = syncFile.tell()
        line = syncFile.readline()
        if not line or line in ['\n', '\r\n']:
            time.sleep(1)
            syncFile.seek(where)
        else:
            if line.rstrip('\n') == "start":
                start = True
    print "Sync File has announced start"
    print "Begin Presentation"

    animatedSpeechProxy.say("Begin Presentation", gesture_confused)

    #================== Detecting inputs ===========================

    #Reads kineticFeedback File
    stop = False
    kinetic_feedbackfile = open('output/kinetic_feedback.txt', 'r')
    timeSinceLastNod = 0
    while not stop:
        where = kinetic_feedbackfile.tell()
        line = kinetic_feedbackfile.readline()
        syncwhere = syncFile.tell()
        syncline = syncFile.readline()
        #Checks for new inputs into kinect file
        if not line or line in ['\n','\n']:
            print "No new line detected in Kinetic Feedback"
            time.sleep(1)
            kinetic_feedbackfile.seek(where)
            if time.time() - timeSinceLastNod > 15:
                gesture_9_nod(motionProxy) #Goes to listening state
                timeSinceLastNod = time.time()
        else:
            #if kinetic feedback output file changes
            print "perform function"
            if line.rstrip('\n') != 0:
                #do output            
                char  = int(line.rstrip('\n'))
                if char == 1:
                    gesture_1_handwave(motionProxy)
                    print "handwave gesture, head_gaze_low"

                elif char == 2:
                    gesture_2_attention(motionProxy)
                    print "attention, gestures_high"

                elif char == 3:
                    gesture_3_leaning(motionProxy)
                    print "leaning,posture_low"

                elif char == 4:
                    gesture_4_shrugging(motionProxy,postureProxy)
                    print "shrugging,clarity_low"

                elif char ==5:
                    gesture_5_arms(motionProxy)
                    print "raise up and down, speed_high"

                elif char ==6:
                    gesture_6_bored(motionProxy)
                    print "Bored, Speed Too Slow"                    

                elif char ==7:
                    gesture_7_coverears(motionProxy)
                    print "Cover ears, volume_high"                    

                elif char ==8:
                    gesture_8_tilt_head(motionProxy)
                    print "tilt head, volume_low"                    

                else:
                    gesture_9_nod(motionProxy)
                    print "Nodding Head and standing chill" 

        # if not syncline or syncline in ['\n','\n']:
        #     print "No new line detected in Sync File"
        #     time.sleep(1)
        #     syncFile.seek(syncwhere)
        # else:
        #     if syncline.rstrip('\n') == "stop":
        #         print "New line detected in sync file"
        #         stop = True

        # check if sync has said to stop
        syncFileStop = open("output/sync.txt", 'r')
        for sline in syncFileStop:
            if sline.rstrip('\n') == "stop":
                stop = True
                print "User called for stop"
        syncFileStop.close()
            

    animatedSpeechProxy.say("Well Done!", gesture_confused)
    print "End Presentation"

    # animatedSpeechProxy.say("Begin Post Speech Feedback", gesture_confused)
    print "Begin Post-Speech Feedback"

    postspeech_feedbackfile = open('output/postspeech_feedback.txt', 'r')    
    
    data=postspeech_feedbackfile.read()

    animatedSpeechProxy.say(data, gesture_confused)

    # animatedSpeechProxy.say("End Post Speech Feedback", gesture_confused)
    print "End Post-Speech Feedback, Terminating Robot"


    # gesture_confused(robotIP)
    # StandUp(postureProxy)

    # ttsProxy.say("Shut up weicong")

    # StandUp(postureProxy)

    # squat(robotIP)

    # SitDown(postureProxy)

    # StiffnessOff(motionProxy)

    motionProxy.rest()
    
if __name__ == "__main__":
    # robotIp = "169.254.44.123" #Set a default IP here
    robotIp = "127.0.0.1" #Set a default IP here
    # robotPort = 9559 #Set default POort here
    robotPort = 45555 #Set default POort here

    # if len(sys.argv) < 2:
    #     print "Usage python robotIP please"
    # else:
    #     robotIp = sys.argv[1]

    # if len(sys.argv) > 2:
    #     print "Usage python robotPort please"
    # else:
    #     robotPort = int(sys.argv[2])

    main(robotIp, robotPort)