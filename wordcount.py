#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

# 1ST STEP
# count each word
def word_count_dict(filename):
  # make a dictionary for each number of the word
  word_count = {}
  # open a file
  word_file = open(filename, encoding='utf-8')
  # we will split the space between each word for each line
  for line in word_file:
    words = line.split()
    # change all the words as lowercase
    for word in words:
      word = word.lower()
      # add the words to the word_count dict
      if word not in word_count:
        word_count[word] = 1
      # add count to the existing word
      else:
        word_count[word] += 1
  return word_count

# 2ND STEP
# make a print_words() function
def print_words(filename):
  result_word_count = word_count_dict(filename)
  words = sorted(result_word_count)
  # add loop to print 1 key 1 line
  for word in words:
    print(word, result_word_count[word])
  return



# 3RD STEP
# make a tuple for the word count



# make a print_top(filename) function
def print_top(filename):
  # sort the list by the number of each word
  result_word_count = word_count_dict(filename)

  words = sorted(result_word_count, reverse=True)
  # result_word_top = sorted_top[:20]
  
  for word in words[:20]:
    print(word, result_word_count[word])
  # print(sorted_top[:20])
  return


# call the functions
word_count_dict(r"C:\Users\rzzkt\Downloads\google-python-exercises\google-python-exercises\basic\alice.txt")
# print_words(r"C:\Users\rzzkt\Downloads\google-python-exercises\google-python-exercises\basic\alice.txt")
print_top(r"C:\Users\rzzkt\Downloads\google-python-exercises\google-python-exercises\basic\alice.txt")


sys.exit(0)






###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
