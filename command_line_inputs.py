__author__ = 'saipc'

from sys import argv
# unpacks and stores :D
script_name, first_arg, second_arg = argv

print "Script name is %s" % script_name
print "First arg is %s" % first_arg
print "Second arg is %s" % second_arg

# starts with 0 as expected :D
print "Script name is %s" % argv[0]
print "First arg is %s" % argv[1]
print "Second arg is %s" % argv[2]

# Looks like argc isnt here :(
# print "Total number of args is %s" % argc