from sys import argv

__author__ = 'saipc'

script, file_name = argv

with open(file_name, 'r') as file:
    # for an array of lines
    print file.readlines()
    # rewind after previous read
    file.seek(0)
    # for plaintext string
    print file.read()
    # rewind after previous read
    file.seek(0)
    # for one line
    print file.readline()
    # rewind after previous read
    file.seek(0)
