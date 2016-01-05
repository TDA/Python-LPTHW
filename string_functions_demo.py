__author__ = 'saipc'

from string_functions import *

string = "Hello I am Sai, and I am a programmer (hopefully)"

words = break_words(string)
print words

sorted_words = sort_words(words)
print sorted_words

# does the same as breaking and sorting
print sort_sentence(string) == sorted_words

print_first_word(sorted_words)
# did it pop the actual list as well?
print sorted_words
# sadly yes, so references, not copies

print_last_word(sorted_words)
print sorted_words

# same as the composite of the previous
# functions, but the string is unmodified
print_first_and_last(string)
print_first_and_last_sorted(string)