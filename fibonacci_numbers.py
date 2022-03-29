# Task : 
# Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

fibonacci_num = []
previous = 0
now = 1
for i in range(10) :
  fibonacci_num.append(now)
  next = previous + now
  previous = now
  now = next
print(fibonacci_num)
