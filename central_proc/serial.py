import os
import time

outputsTxt = open(os.path.dirname(os.path.realpath(__file__))+'/output_filenames.txt', 'r')

outputFiles = {}
outputDir = 'dummy_programs/output/'
for outputFileName in outputsTxt:
    name = outputFileName.rstrip('\n')
    outputFiles[name] = open(outputDir+name+'.txt', 'r')

i = 0
while i < 10: # safety to stop loop
    for name, f in outputFiles.iteritems():
        # the following inspired by the soln: http://code.activestate.com/recipes/157035-tail-f-in-python/
        # f = outputFiles["speech_accuracy"]
        where = f.tell()
        line = f.readline()
        if not line:
            time.sleep(1)
            f.seek(where)
        else:
            print name+': '+str(line), # already has newline
    i+=1

print "Finished loop"