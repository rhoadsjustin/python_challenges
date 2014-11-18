## Potential Solution 1: Using looping technique
def fib(n):
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
  return a
print(fib(100))

## Potential Solution 2: Using recursion
def fibR(n):
 if n==1 or n==2:
  return 1
 return fib(n-1)+fib(n-2)
print(fibR(100))


## Potential Solution 3: Using memoization
def memoize(fn, arg):
  memo = {}
  if arg not in memo:
    memo[arg] = fn(arg)
    return memo[arg]

## Using fibR() as written in example 2.
fibm = memoize(fibR,100)
print(fibm)
