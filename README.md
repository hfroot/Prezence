# Prezence

## Run
So that the robot can be run with one command from one laptop, I've created a start script that can take some inputs as necessary. Currently, to run it, start in the `Prezence` directory and type `./scripts/start.sh dummy_programs serial`. The first command specifies where all the programs are, while the second specifies the control script to use. This may be changed in the future if you guys like the proposed structure. 

## Proposed structure
I've written some dummy files so that I can start making the central processing hub. These can be found in [dummy_programs](dummy_programs). However, maybe a neater way than sticking all the programs in one folder is to create separate folders depending on module, and in those there may or may not be more than one file. I've followed this convention for [the central processing hub](central_proc) in which I've put a config file to tell me the output filenames that will be written to by the other programs, and the script which will read those files.

## Adding to the README
If you want to add to the readme file using nice formatting, check out the helpful cheatsheet [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).