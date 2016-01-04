__author__ = 'saipc'
from sys import argv
from os.path import exists

script, from_file, to_file = argv

def copy(from_file, to_file):
    print "Copying from %s to %s" % (from_file, to_file)
    # Does the input file exist?
    if exists(from_file):
        with open(from_file, 'r') as infile:
            indata = infile.read()
        print "The input file is %d bytes long" % len(indata)

        print "Does the output file exist? %r" % exists(to_file)
        print "Ready, hit RETURN to continue, CTRL-C to abort."
        raw_input()

        with open(to_file, 'w') as out_file:
            out_file.write(indata)
        print "Alright, all done."
    else:
        print "Input file does not exist, exiting"
        exit(-1)

copy(from_file, to_file)