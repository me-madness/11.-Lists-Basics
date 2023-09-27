n = int(input())
magic_word = input()

strings = []

for _ in range(n):
    string = input()
    strings.append(string)
    
filtered_strings = []    

for current_string in strings:
    if magic_word in current_string:
        filtered_strings.append(current_string)
        
print(strings)        
print(filtered_strings)