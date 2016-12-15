# Prezence

## Dates!
**Thursday 1st**: First test on NAO

**Monday 12th/Tuesday 13th**: Test on people

**Wednesday 14th**: Last minute changes

**Thursday 15th**: Demo

**Thursday 22nd**: Final research paper

## Run
So that the robot can be run with one command from one laptop, I've created a start script that can take some inputs as necessary. Currently, to run it, start in the `Prezence` directory and type `bash begin.sh`. The first command specifies where all the programs are, while the second specifies the control script to use. This may be changed in the future if you guys like the proposed structure.

## Outputs

#### Speech speed
Writes to [output](output)/speed.txt at regular intervals with speed in words per minute as an integer.

#### Speech accuracy
Writes to [output](output)/clarity.txt at regular intervals with a confidence level between 0 and 1.

#### Speech volume
Writes to [output](output)/volume.txt at regular intervals with an absolute value between 0 and 10000.

#### TIME TAKEN
NOTE: speech module now records the time at the end of execution into the last line in 'time.txt', happens every presentation independently of any other factors 

#### Gestures
Writes to [output](output)/gestures.txt. Gestures being monitored: facing away, folded arms, gesticulating, moving, covering mouth, hands in pockets, shifting weight?. Written whenever there is a change or every 30 seconds. 

#### Head gaze
Writes to [output](output)/head_gaze.txt. Output `x y` angle (0 - 180) as an integer. Output at regular intervals. This is for determining whether enough contact is being made with the audience.

#### Central processor
Writes to [output](output)/kinetic_feedback.txt with values from 1 to 9 when needed.

#### Synchronisation
Speech script writes to [output](output)/sync.txt with start or stop on a new line. Everyone else monitors this file to know when to start and stop recording.

#### Note about [computer_vision](computer_vision)
The file contained in this folder is a copy of what Max is changing to run his module. There are many dependencies outside of this that are contained on the shared laptop, no point in committing because it requires set up.

## Proposed structure
The script [script/start.sh](script/start.sh) will start all of the programs in parallel. Please add your start command, with the correct path relative to the main Prezence folder, to this line. 
All the modules will need to monitor [output](output)/sync.txt to know when to start and stop. 
Have a folder for each module ([speech](speech), [computer_vision](computer_vision), [kinetic_feedback](kinetic_feedback) and [central_processor](central_processor)) in which any files you need will be stored.

## Branching conventions
The convention that my workplace used over the summer (granted they used fossil and not git, fossil so much easier to use but a lot less popular) is that the master branch should always be ready to run - so it is tested and happy to go. So any development goes on in branches, and when you're happy the full feature works you merge the master branch into your branch, then merge your branch into master. This seemed to be a pretty good way of doing things. If you were making a small change then you didn't have to do that, so you don't have the hassle of branching and immediately merging.

## Adding to the README
If you want to add to the readme file using nice formatting, check out the helpful cheatsheet [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

##Possible errors and future improvement
* Screen is too small, participants find it difficult to look at screen.
* Avatar has no verbal feedback since choreographe has no audio output. We did not have enough time to make a bespoke animation independent of choreographe that is 