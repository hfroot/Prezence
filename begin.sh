#!/bin/sh
xterm -title "Central Proc" -hold -e python central_proc/tailored_cp.py  &
xterm -title "Speech Module" -hold -e python speech/speech.py  &
xterm -title "Computer Vision" -hold -e roslaunch skeleton_markers skeleton_launch | rosrun skeletom_monitor skeleton_monitor  &
xterm -title "Gesture" -hold -e python kinetic_feedback/kinetic_feedback.py