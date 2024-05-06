# Printing first terms of fibonacci series
def fibonacci(n):
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n-1)+fibonacci(n-2)
  
n = int(input("Enter the value of 'n': "))
print("Fibonacci Series:")

for i in range(0, n+1):
  print(fibonacci(i), end=' ')