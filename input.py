__author__ = 'saipc'

# #notice the newlines and no-newlines
# print "What is your name?",
# # always take raw_input instead of input, input takes in strings enclosed in quotes
# name = raw_input()
# print "How old are you?",
# age = raw_input()
# print "What do you do?"
# profession = raw_input()
#
# print "Hi %s, you are %s years old, and you %s" % (name, age, profession)

# Does the same, well, almost, without newlines and spaces
name = raw_input("What is your name? ")
age = raw_input("How old are you? ")
profession = raw_input("What do you do? ")

print "Hi %s, you are %s years old, and you %s" % (name, age, profession)

# Apparently input(prompt) === eval(raw_input(prompt))
# so these will search for variables named Sai, 22 and Work instead of strings :D
name = eval(raw_input("What is your name? "))
age = eval(raw_input("How old are you? "))
profession = eval(raw_input("What do you do? "))

print "Hi %s, you are %s years old, and you %s" % (name, age, profession)
