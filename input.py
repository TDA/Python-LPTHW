__author__ = 'saipc'

#notice the newlines and no-newlines
print "What is your name?",
# always take raw_input instead of input, input takes in strings enclosed in quotes
name = raw_input()
print "How old are you?",
age = raw_input()
print "What do you do?"
profession = raw_input()

print "Hi %s, you are %s years old, and you %s" % (name, age, profession)