#!/bin/sh
rm output/sync.txt
touch output/sync.txt 
export PYTHONPATH=$PYTHONPATH:/home/human/Prezence/kinetic_feedback/pynaoqi-python2.7-2.1.2.17-linux64
#xterm -title "Computer Vision" -hold -e roslaunch skeleton_markers skeleton.launch &
xterm -title "Central Proc" -hold -e python central_proc/tailored_cp.py  &
xterm -title "Speech Module" -hold -e sudo python speech/speech.py &
xterm -title "Computer Vision" -hold -e rosrun skeleton_monitor skeleton_monitor  &
xterm -title "Gesture" -hold -e  python kinetic_feedback/kinetic_feedback_nofeedback.py
