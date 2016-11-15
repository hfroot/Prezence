#!/bin/bash

# run by: ./scripts/start.sh dummy_programs NAME_OF_CONTROL
# run programs in parallel
python central_proc/$2.py & python $1/speech_speed.py & python $1/speech_accuracy.py & python $1/cv_gesture.py & wait