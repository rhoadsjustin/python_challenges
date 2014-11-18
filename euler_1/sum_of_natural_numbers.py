# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Potential Soluton 1, using a method

def multiples_of_3_or_5():
  for number in xrange(1, 1000):
    if not number % 3 or not number % 5:
      yield number

print sum(multiples_of_3_or_5())

# Potential Solution 2, without a method

print sum( number for number in xrange(1000) if not (number % 3 and number % 5) )
