""" fibonacci algorithim function """
def fib(number):
    """ fibonacci """
  # Your code here
    if number < 2:
        return number
    return fib(number - 1) + fib(number - 2)


print(fib(12))
