#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# iReturn the resulting string.
def verbing(s):
    #making another copy of the string
    a=s
    #if the length of the string is less then 3
    # then return the string 
    if len(s)<3:
	return s
    elif s[-3:]!='ing':
	#else if the last 3 elements is not equal to
	#'ing'then concatenate 'ing'to the string
	#or else 'ly' to the string
	a=s+'ing'
    else:
	a=s+'ly'	
    return a


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    a=s.find('not')
    #s.find('asd') return the position
    #of the string starting with 'asd'
    b=s.find('bad')
    if a!=-1 and b!=-1 and b>a:
	# checking whether a and b have any value and length of b>a
	s=s[:a] + 'good'+ s[b+3:]
	#returning the elments till a then
	# concatenating 'good' and elements after b+3
    return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    #taking the half of the length of string
    alen=len(a)/2
    blen=len(b)/2
    if len(a)%2==1:
	#if the length of a is odd then add 1 to alen
	alen=alen+1
    if len(b)%2==1:
	#if the length of b is odd then add 1 to blen
	blen=blen+1
    #concatenating the elements of a till alen then 
    #b till blen then a starting from alen till 
    #last element then b starting from blen till
    # last element of b and returning.
    return a[:alen]+b[:blen]+a[alen:]+b[blen:]


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
