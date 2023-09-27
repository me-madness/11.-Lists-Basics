#First Solution

# n = int(input())

# COMMAND_EVEN = 'even'
# COMMAND_ODD = 'odd'
# COMMAND_NEGATIVE = 'negative'
# COMMAND_POSITIVE = 'positive'

    
# numbers = [int(input()) for _ in range(n)]
# filtered_numbers = []

# command = input()

# for num in numbers:
#     filtered_numbers = ((command == COMMAND_EVEN and num % 2 == 0) or
#                         (command == COMMAND_ODD and num % 2 != 0) or
#                         (command == COMMAND_POSITIVE and num >= 0) or
#                         (command == COMMAND_NEGATIVE and num < 0)
#     )
    
#     if filtered_numbers:
#         filtered_numbers.append(num)
        
# print(filtered_numbers)    

# Second Solution

n = int(input())

numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)
    
command = input()
filtered_numbers = []

if command == 'even':
    for num in numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)    
elif command == 'odd':
    for num in numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)               
elif command == 'positive':
    for num in numbers:
        if num >= 0:
            filtered_numbers.append(num)                 
elif command == 'negative':
    for num in numbers:
        if num < 0:
            filtered_numbers.append(num)                

print(filtered_numbers)            