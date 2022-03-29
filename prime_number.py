# Task : 
# Write a program that takes a number from the user and prints the result to check if it is a prime number.

num = int(input("Enter a number: "))
prime_num = True
for i in range(2,num) :
  if num % i == 0 :
    prime_num = False
    break
if prime_num:
  print(num, "is a prime number.")
else:
  print(num, "is not a prime number.")
