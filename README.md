![Header](https://github.com/hfroot/Prezence/blob/master/prezence.pdf)

## Project outline
Public speaking is a skill many people struggle with, due to lack of experience and/or confidence. Human coaches can be too expensive to use regularly or for more informal occasions. This is why we developed Prezence, a robotic presentation delivery coach that won't get bored hearing you practice the same speech over and over again!

Prezence is a system that combines a NAO robot, a microphone and a Kinect to watch you give a speech and give you real-time and post-fact feedback. Prezence at the moment tracks speech accuracy, volume and speed, as well as head gaze and gesticulation. If you deviate from the configurable ideal model of delivery, NAO will gesture to you to indicate the change you need to make. At the end of your presentation, NAO will give you statistics about your presentation so that you know what to improve on.

## Run
To run this software, you will need a NAO, a Kinect and a microphone. Starting in the `Prezence` directory, type `bash begin.sh` to start the program.

#### Note about [computer_vision](computer_vision)
The file contained in this folder is a copy of what we have created for this system. There are many dependencies outside of this that require setting up on the laptop in use in order to be able to run this module.

## Ideal delivery model
We created an ideal delivery model following research and testing. If you would like to change it, however, this is easily done in [config](central_proc/config.txt).

The config data is specified as such:

``speechAspectName min minValue max maxValue allowance allowanceValue priority priorityValue``

`speechAspectName` is the name of the aspect that is being analysed, e.g. `accuracy` or `head_gaze`, required.

`minValue` is the minimum value the aspect can take before being considered wrong.

`maxValue` is the maximum value the aspect can take before being considered wrong. One or both of min and max can be specified.

`allowanceValue` is the number of consecutive measurements of an non ideal value are allowed before feedback should occur, optional.

`priorityValue` acts as a tiebreaker for deciding which aspect to provide feedback for. A lower value means a higher priority. Required and must be a unique number.

## Outputs

#### Speech speed
Writes to [output](output)/speed.txt at regular intervals with speed in words per minute as an integer.

#### Speech accuracy
Writes to [output](output)/clarity.txt at regular intervals with a confidence level between 0 and 1.

#### Speech volume
Writes to [output](output)/volume.txt at regular intervals with an absolute value between 0 and 10000.

#### Time taken
Speech module records the time at the end of execution into the last line in 'time.txt', happens every presentation independently of any other factors.

#### Gestures
Writes to [output](output)/gestures.txt. Gestures being monitored: facing away, folded arms, gesticulating, moving, covering mouth, hands in pockets. Written whenever there is a change or every 30 seconds. 

#### Head gaze
Writes to [output](output)/head_gaze.txt. Output `x y` angle (0 - 180) as an integer. Output at regular intervals. This is for determining whether enough contact is being made with the audience.

#### Central processor
Writes to [output](output)/kinetic_feedback.txt with values from 1 to 9 when needed.

#### Synchronisation
Speech script writes to [output](output)/sync.txt with start or stop on a new line. Everyone else monitors this file to know when to start and stop recording.

## Notes for additional modules
The script [script/start.sh](script/start.sh) will start all of the programs in parallel. Please add your start command, with the correct path relative to the main Prezence folder, to this line. 
All the modules will need to monitor [output](output)/sync.txt to know when to start and stop. 

## Future development
* Although we generally want to avoid aural interruptions by the robot so as not to put the speaker off, audio output for when the speaker is looking down would be helpful
* Prompt feature to help the speaker if they forget their next point, will provide an interesting natural language processing challenge
