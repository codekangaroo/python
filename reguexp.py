#! /usr/bin/python3

import re

myString = 'Send an email from this@emai.com to test@gmail.com 22 33 times'

#finds strings that starts with 'Send'
result = re.findall('^Send', myString)
print(result)

#finds all a's b's anc c's
result = re.findall('[abc]', myString)
print(result)

#finds all numbers, one or more digits 
result = re.findall('[0-9]+', myString)
print(result)

#finds all that is not lower case letters 
result = re.findall('[^a-z]+', myString)
print(result)

#finds all emails nonwhitespacecharacters@nonwhitespacecharacters
result = re.findall('\S+@\S+', myString)
print(result)

