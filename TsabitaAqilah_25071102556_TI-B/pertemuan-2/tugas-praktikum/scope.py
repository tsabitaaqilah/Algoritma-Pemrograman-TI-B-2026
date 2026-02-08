def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

x = range(3, 10)
x = range(3, 10, 2)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (n-1) + (n-2)
    

