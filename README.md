# Prezence

## Run
So that the robot can be run with one command from one laptop, I've created a start script that can take some inputs as necessary. Currently, to run it, start in the `Prezence` directory and type `./scripts/start.sh dummy_programs serial`. The first command specifies where all the programs are, while the second specifies the control script to use. This may be changed in the future if you guys like the proposed structure. 

## Proposed structure
I've written some dummy files so that I can start making the central processing hub. These can be found in [dummy_programs](dummy_programs). However, maybe a neater way than sticking all the programs in one folder is to create separate folders depending on module, and in those there may or may not be more than one file. I've followed this convention for [the central processing hub](central_proc) in which I've put a config file to tell me the output filenames that will be written to by the other programs, and the script which will read those files.

## Branching conventions
The convention that my workplace used over the summer (granted they used fossil and not git, fossil so much easier to use but a lot less popular) is that the master branch should always be ready to run - so it is tested and happy to go. So any development goes on in branches, and when you're happy the full feature works you merge the master branch into your branch, then merge your branch into master. This seemed to be a pretty good way of doing things. If you were making a small change then you didn't have to do that, so you don't have the hassle of branching and immediately merging.

## Adding to the README
If you want to add to the readme file using nice formatting, check out the helpful cheatsheet [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).