# calculating user input (5 inputs) without using max()function
count = 0
all_num = []
while count < 5:
  num = int(input("Please, enter the number: "))
  all_num.append(num)
  count = count +1
num_max = 0
for i in all_num:
  if i > num_max:
    num_max = i
print(num_max)
