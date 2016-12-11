# -*- encoding: UTF-8 -*- 

import math
# import almath as m # python's wrapping of almath
import sys
from naoqi import ALProxy


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


def gesture_1_handwave(robotIP) :

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.6])
    keys.append([0.0459781])

    names.append("HeadYaw")
    times.append([0.6])
    keys.append([-0.0322559])

    names.append("LAnklePitch")
    times.append([0.6])
    keys.append([-0.352862])

    names.append("LAnkleRoll")
    times.append([0.6])
    keys.append([-0.00149202])

    names.append("LElbowRoll")
    times.append([0.6])
    keys.append([-0.492372])

    names.append("LElbowYaw")
    times.append([0.6])
    keys.append([-0.09515])

    names.append("LHand")
    times.append([0.6])
    keys.append([0.2372])

    names.append("LHipPitch")
    times.append([0.6])
    keys.append([-0.443284])

    names.append("LHipRoll")
    times.append([0.6])
    keys.append([-0.00609398])

    names.append("LHipYawPitch")
    times.append([0.6])
    keys.append([0.00310993])

    names.append("LKneePitch")
    times.append([0.6])
    keys.append([0.699462])

    names.append("LShoulderPitch")
    times.append([0.6])
    keys.append([-0.921976])

    names.append("LShoulderRoll")
    times.append([0.6])
    keys.append([0.25])

    names.append("LWristYaw")
    times.append([0.6])
    keys.append([0.11194])

    names.append("RAnklePitch")
    times.append([0.6])
    keys.append([-0.348176])

    names.append("RAnkleRoll")
    times.append([0.6])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([0.6])
    keys.append([0.925044])

    names.append("RElbowYaw")
    times.append([0.6])
    keys.append([1.39897])

    names.append("RHand")
    times.append([0.6])
    keys.append([0.2448])

    names.append("RHipPitch")
    times.append([0.6])
    keys.append([-0.451038])

    names.append("RHipRoll")
    times.append([0.6])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([0.6])
    keys.append([0.00310993])

    names.append("RKneePitch")
    times.append([0.6])
    keys.append([0.696478])

    names.append("RShoulderPitch")
    times.append([0.6])
    keys.append([1.40212])

    names.append("RShoulderRoll")
    times.append([0.6])
    keys.append([-0.069072])

    names.append("RWristYaw")
    times.append([0.6])
    keys.append([0.0597839])

    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


def gesture_2_attention(robotIP):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.44, 4.28])
    keys.append([0.0137641, 0.0106959])

    names.append("HeadYaw")
    times.append([0.44, 4.28])
    keys.append([-0.00464392, 0.0183661])

    names.append("LAnklePitch")
    times.append([0.44, 4.28])
    keys.append([-0.354312, -0.354396])

    names.append("LAnkleRoll")
    times.append([0.44, 4.28])
    keys.append([-4.19617e-05, 0.00157595])

    names.append("LElbowRoll")
    times.append([0.44, 4.28])
    keys.append([-0.975582, -0.0349066])

    names.append("LElbowYaw")
    times.append([0.44, 4.28])
    keys.append([-1.39138, -1.3653])

    names.append("LHand")
    times.append([0.44, 4.28])
    keys.append([0.244, 0.2432])

    names.append("LHipPitch")
    times.append([0.44, 4.28])
    keys.append([-0.449504, -0.447886])

    names.append("LHipRoll")
    times.append([0.44, 4.28])
    keys.append([-0.0061779, -0.00609398])

    names.append("LHipYawPitch")
    times.append([0.44, 4.28])
    keys.append([4.19617e-05, 0.00157595])

    names.append("LKneePitch")
    times.append([0.44, 4.28])
    keys.append([0.70108, 0.704064])

    names.append("LShoulderPitch")
    times.append([0.44, 4.28])
    keys.append([1.48947, 1.51402])

    names.append("LShoulderRoll")
    times.append([0.44, 4.28])
    keys.append([0.239262, 0.107338])

    names.append("LWristYaw")
    times.append([0.44, 4.28])
    keys.append([-0.0521979, 0.0168321])

    names.append("RAnklePitch")
    times.append([0.44, 4.28])
    keys.append([-0.354312, -0.351244])

    names.append("RAnkleRoll")
    times.append([0.44, 4.28])
    keys.append([4.19617e-05, -0.00916195])

    names.append("RElbowRoll")
    times.append([0.44, 4.28])
    keys.append([0.975582, 1.31315])

    names.append("RElbowYaw")
    times.append([0.44, 4.28])
    keys.append([1.39138, 1.03081])

    names.append("RHand")
    times.append([0.44, 4.28])
    keys.append([0.244, 0.3844])

    names.append("RHipPitch")
    times.append([0.44, 4.28])
    keys.append([-0.449504, -0.452572])

    names.append("RHipRoll")
    times.append([0.44, 4.28])
    keys.append([0.0061779, 0.00464392])

    names.append("RHipYawPitch")
    times.append([0.44, 4.28])
    keys.append([4.19617e-05, 0.00157595])

    names.append("RKneePitch")
    times.append([0.44, 4.28])
    keys.append([0.70108, 0.704148])

    names.append("RShoulderPitch")
    times.append([0.44, 4.28])
    keys.append([1.48947, -0.0705221])

    names.append("RShoulderRoll")
    times.append([0.44, 4.28])
    keys.append([-0.239262, 0.0352399])

    names.append("RWristYaw")
    times.append([0.44, 4.28])
    keys.append([0.0521979, -0.0322559])

    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


def gesture_3_leaning(robotIP):

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
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


def gesture_4_shrugging(robotIP):

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
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


def gesture_5_arms(robotIP):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([0.00762796, 0.00762796, 0.00762796, 0.00762796, 0.00762796])

    names.append("HeadYaw")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.023052, -0.023052, -0.023052, -0.023052, -0.023052])

    names.append("LAnklePitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.35593, -0.35593, -0.35593, -0.35593, -0.35593])

    names.append("LAnkleRoll")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.00149202, -0.00149202, -0.00149202, -0.00149202, -0.00149202])

    names.append("LElbowRoll")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.0429101, -0.0367742, -0.0429101, -0.0367741, -0.0429101])

    names.append("LElbowYaw")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.352862, -0.492456, -0.352862, -0.492455, -0.352862])

    names.append("LHand")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([0.2424, 0.2424, 0.2424, 0.2424, 0.2424])

    names.append("LHipPitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.444818, -0.444818, -0.444818, -0.444818, -0.444818])

    names.append("LHipRoll")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.00149202, -0.00149202, -0.00149202, -0.00149202, -0.00149202])

    names.append("LHipYawPitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999])

    names.append("LKneePitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([0.700996, 0.700996, 0.700996, 0.700996, 0.700996])

    names.append("LShoulderPitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([1.11518, 0.08126, 1.11518, 0.0812599, 1.11518])

    names.append("LShoulderRoll")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.245482, -0.277696, -0.245482, -0.277696, -0.245482])

    names.append("LWristYaw")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([0.854396, 0.743948, 0.854396, 0.743948, 0.854396])

    names.append("RAnklePitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.352778, -0.352778, -0.352778, -0.352778, -0.352778])

    names.append("RAnkleRoll")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.00149202, -0.00149202, -0.00149202, -0.00149202, -0.00149202])

    names.append("RElbowRoll")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([0.0782759, 0.11049, 0.0782759, 0.11049, 0.0782759])

    names.append("RElbowYaw")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.184122, -0.162646, -0.184122, -0.162646, -0.184122])

    names.append("RHand")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([0.2464, 0.2464, 0.2464, 0.2464, 0.2464])

    names.append("RHipPitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.449504, -0.458708, -0.449504, -0.458707, -0.449504])

    names.append("RHipRoll")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([0.0061779, 0.0061779, 0.00617791, 0.00617791, 0.00617791])

    names.append("RHipYawPitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999])

    names.append("RKneePitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([0.699546, 0.699546, 0.699545, 0.699545, 0.699545])

    names.append("RShoulderPitch")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([0.98487, -0.07359, 0.98487, -0.0735901, 0.98487])

    names.append("RShoulderRoll")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([0.27301, 0.246932, 0.27301, 0.246933, 0.27301])

    names.append("RWristYaw")
    times.append([0.68, 2.12, 3.68, 6.12, 9.56])
    keys.append([-0.45564, -0.070606, -0.455641, -0.0706061, -0.455641])


    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


def gesture_6_bored(robotIP):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.6])
    keys.append([-0.24855])

    names.append("HeadYaw")
    times.append([0.6])
    keys.append([0.029104])

    names.append("LAnklePitch")
    times.append([0.6])
    keys.append([-1.18276])

    names.append("LAnkleRoll")
    times.append([0.6])
    keys.append([0.0752079])

    names.append("LElbowRoll")
    times.append([0.6])
    keys.append([-1.54462])

    names.append("LElbowYaw")
    times.append([0.6])
    keys.append([-0.77011])

    names.append("LHand")
    times.append([0.6])
    keys.append([0.0412])

    names.append("LHipPitch")
    times.append([0.6])
    keys.append([-1.0891])

    names.append("LHipRoll")
    times.append([0.6])
    keys.append([-0.145688])

    names.append("LHipYawPitch")
    times.append([0.6])
    keys.append([-0.262272])

    names.append("LKneePitch")
    times.append([0.6])
    keys.append([2.10307])

    names.append("LShoulderPitch")
    times.append([0.6])
    keys.append([0.536858])

    names.append("LShoulderRoll")
    times.append([0.6])
    keys.append([-0.305308])

    names.append("LWristYaw")
    times.append([0.6])
    keys.append([-0.767042])

    names.append("RAnklePitch")
    times.append([0.6])
    keys.append([-1.1863])

    names.append("RAnkleRoll")
    times.append([0.6])
    keys.append([-0.07359])

    names.append("RElbowRoll")
    times.append([0.6])
    keys.append([0.0567999])

    names.append("RElbowYaw")
    times.append([0.6])
    keys.append([0.630432])

    names.append("RHand")
    times.append([0.6])
    keys.append([0.0427999])

    names.append("RHipPitch")
    times.append([0.6])
    keys.append([-1.06464])

    names.append("RHipRoll")
    times.append([0.6])
    keys.append([0.12583])

    names.append("RHipYawPitch")
    times.append([0.6])
    keys.append([-0.262272])

    names.append("RKneePitch")
    times.append([0.6])
    keys.append([2.11236])

    names.append("RShoulderPitch")
    times.append([0.6])
    keys.append([1.08918])

    names.append("RShoulderRoll")
    times.append([0.6])
    keys.append([-0.0629361])

    names.append("RWristYaw")
    times.append([0.6])
    keys.append([0.262272])


    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


def gesture_7_coverears(robotIP):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.6])
    keys.append([-0.24855])

    names.append("HeadYaw")
    times.append([0.6])
    keys.append([0.029104])

    names.append("LAnklePitch")
    times.append([0.6])
    keys.append([-1.18276])

    names.append("LAnkleRoll")
    times.append([0.6])
    keys.append([0.0752079])

    names.append("LElbowRoll")
    times.append([0.6, 0.64])
    keys.append([-1.54462, -1.54163])

    names.append("LElbowYaw")
    times.append([0.6, 0.64])
    keys.append([-0.77011, -1.64296])

    names.append("LHand")
    times.append([0.6, 0.64])
    keys.append([0.0412, 0.0908])

    names.append("LHipPitch")
    times.append([0.6])
    keys.append([-1.0891])

    names.append("LHipRoll")
    times.append([0.6])
    keys.append([-0.145688])

    names.append("LHipYawPitch")
    times.append([0.6])
    keys.append([-0.262272])

    names.append("LKneePitch")
    times.append([0.6])
    keys.append([2.10307])

    names.append("LShoulderPitch")
    times.append([0.6, 0.64])
    keys.append([0.536858, -1.09839])

    names.append("LShoulderRoll")
    times.append([0.6, 0.64])
    keys.append([-0.305308, -0.136568])

    names.append("LWristYaw")
    times.append([0.6, 0.64])
    keys.append([-0.767042, -0.771644])

    names.append("RAnklePitch")
    times.append([0.6])
    keys.append([-1.1863])

    names.append("RAnkleRoll")
    times.append([0.6])
    keys.append([-0.07359])

    names.append("RElbowRoll")
    times.append([0.6, 0.64])
    keys.append([0.0567999, 1.54462])

    names.append("RElbowYaw")
    times.append([0.6, 0.64])
    keys.append([0.630432, 1.63827])

    names.append("RHand")
    times.append([0.6, 0.64])
    keys.append([0.0427999, 0.0427999])

    names.append("RHipPitch")
    times.append([0.6])
    keys.append([-1.06464])

    names.append("RHipRoll")
    times.append([0.6])
    keys.append([0.12583])

    names.append("RHipYawPitch")
    times.append([0.6])
    keys.append([-0.262272])

    names.append("RKneePitch")
    times.append([0.6])
    keys.append([2.11236])

    names.append("RShoulderPitch")
    times.append([0.6, 0.64])
    keys.append([1.08918, -0.852862])

    names.append("RShoulderRoll")
    times.append([0.6, 0.64])
    keys.append([-0.0629361, 0.197844])

    names.append("RWristYaw")
    times.append([0.6, 0.64])
    keys.append([0.262272, 0.964844])


    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


def gesture_8_tilt_head(robotIP):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-0.24855, -0.016916, 0.02757, 0.128814])

    names.append("HeadYaw")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([0.029104, 0.0137641, -0.0153821, 0.708666])

    names.append("LAnklePitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-1.18276, -0.343658, -0.349794, -0.351328])

    names.append("LAnkleRoll")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([0.0752079, 0.00464392, 0.00310993, 0.00310993])

    names.append("LElbowRoll")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-1.54462, -0.513848, -1.00166, -1.00166])

    names.append("LElbowYaw")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-0.77011, -1.53558, -1.35917, -1.3699])

    names.append("LHand")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([0.0412, 0.2364, 0.2412, 0.2412])

    names.append("LHipPitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-1.0891, -0.446352, -0.452488, -0.452488])

    names.append("LHipRoll")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-0.145688, -0.00302601, 0.00157595, 0.00157595])

    names.append("LHipYawPitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-0.262272, 0.00310993, -0.00455999, -0.00302601])

    names.append("LKneePitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([2.10307, 0.704064, 0.699462, 0.69486])

    names.append("LShoulderPitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([0.536858, 1.35908, 1.42811, 1.42811])

    names.append("LShoulderRoll")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-0.305308, -0.0276539, 0.251534, 0.262272])

    names.append("LWristYaw")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-0.767042, 0.12728, 0.026036, 0.0152981])

    names.append("RAnklePitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-1.1863, -0.354312, -0.35738, -0.34971])

    names.append("RAnkleRoll")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-0.07359, -0.00302601, -0.00302601, -0.00302601])

    names.append("RElbowRoll")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([0.0567999, 1.54462, 0.997142, 1.54462])

    names.append("RElbowYaw")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([0.630432, 1.53242, 1.38363, 1.13052])

    names.append("RHand")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([0.0427999, 0.3012, 0.2444, 0.5212])

    names.append("RHipPitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-1.06464, -0.452572, -0.449504, -0.449504])

    names.append("RHipRoll")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([0.12583, -0.00302601, -0.00302601, 0.00771189])

    names.append("RHipYawPitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-0.262272, 0.00310993, -0.00455999, -0.00302601])

    names.append("RKneePitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([2.11236, 0.698012, 0.705682, 0.705682])

    names.append("RShoulderPitch")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([1.08918, 0.16418, 1.40672, 0.11816])

    names.append("RShoulderRoll")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([-0.0629361, -0.0123138, -0.276162, 0.208582])

    names.append("RWristYaw")
    times.append([0.6, 0.64, 0.68, 0.8])
    keys.append([0.262272, 0.076658, -0.0322559, 0.0475121])


    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


def gesture_9_nod(robotIP):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.6])
    keys.append([0.0459781])

    names.append("HeadYaw")
    times.append([0.6])
    keys.append([-0.0322559])

    names.append("LAnklePitch")
    times.append([0.6])
    keys.append([-0.348176])

    names.append("LAnkleRoll")
    times.append([0.6])
    keys.append([-0.00157595])

    names.append("LElbowRoll")
    times.append([0.6])
    keys.append([-0.925044])

    names.append("LElbowYaw")
    times.append([0.6])
    keys.append([-1.39897])

    names.append("LHand")
    times.append([0.6])
    keys.append([0.2448])

    names.append("LHipPitch")
    times.append([0.6])
    keys.append([-0.451038])

    names.append("LHipRoll")
    times.append([0.6])
    keys.append([0.00302601])

    names.append("LHipYawPitch")
    times.append([0.6])
    keys.append([0.00310993])

    names.append("LKneePitch")
    times.append([0.6])
    keys.append([0.696478])

    names.append("LShoulderPitch")
    times.append([0.6])
    keys.append([1.40212])

    names.append("LShoulderRoll")
    times.append([0.6])
    keys.append([0.069072])

    names.append("LWristYaw")
    times.append([0.6])
    keys.append([-0.0597839])

    names.append("RAnklePitch")
    times.append([0.6])
    keys.append([-0.348176])

    names.append("RAnkleRoll")
    times.append([0.6])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([0.6])
    keys.append([0.925044])

    names.append("RElbowYaw")
    times.append([0.6])
    keys.append([1.39897])

    names.append("RHand")
    times.append([0.6])
    keys.append([0.2448])

    names.append("RHipPitch")
    times.append([0.6])
    keys.append([-0.451038])

    names.append("RHipRoll")
    times.append([0.6])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([0.6])
    keys.append([0.00310993])

    names.append("RKneePitch")
    times.append([0.6])
    keys.append([0.696478])

    names.append("RShoulderPitch")
    times.append([0.6])
    keys.append([1.40212])

    names.append("RShoulderRoll")
    times.append([0.6])
    keys.append([-0.069072])

    names.append("RWristYaw")
    times.append([0.6])
    keys.append([0.0597839])


    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_confused(robotIP):

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
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


def squat(robotIP):

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
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      motion = ALProxy("ALMotion", robotIP, 9559)
        #motion = ALProxy("ALMotion")
      motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


def init():

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

    # Turn on the Motors
    # StiffnessOn(motionProxy)
    motionProxy.wakeUp()

    # say the text with the local configuration
    # animatedSpeechProxy.say("Don't be angry, please", gesture_confused)

    #StandUp
    StandUp(postureProxy)  


def main(robotIP,robotPort):

    #initialise 
    init()




 

    # #Walk 1 Meter
    # Walk(motionProxy,1,0,0)


    # gesture_1_handwave(robotIP)
    # StandUp(postureProxy)
    

    # gesture_2(robotIP)
    # StandUp(postureProxy)

    # gesture_3(robotIP)
    # StandUp(postureProxy)

    # gesture_4(robotIP)
    # StandUp(postureProxy)

    # gesture_5(robotIP)
    # StandUp(postureProxy)

    # gesture_6(robotIP)
    # StandUp(postureProxy)

    # gesture_7(robotIP)
    # StandUp(postureProxy)

    # gesture_8(robotIP)
    # StandUp(postureProxy)

    gesture_confused(robotIP)
    StandUp(postureProxy)



    # ttsProxy.say("Shut up weicong")

    # #StandUp
    # StandUp(postureProxy)

    # # #Sit Down
    # squat(robotIP)


    # SitDown(postureProxy)

    # # # Turn off the Motors
    # StiffnessOff(motionProxy)

    motionProxy.rest()


if __name__ == "__main__":
    robotIp = "169.254.121.24" #Set a default IP here
    robotPort = 9559 #Set default POort here


    # if len(sys.argv) < 2:
    #     print "Usage python robotIP please"
    # else:
    #     robotIp = sys.argv[1]

    # if len(sys.argv) > 2:
    #     print "Usage python robotPort please"
    # else:
    #     robotPort = int(sys.argv[2])

    main(robotIp, robotPort)