n = int(input())
count_positives = []
sum_of_negatives = []

for i in range (0, n):
    current_number = int(input())
    if current_number > 0:
        count_positives.append(current_number)
    else:
        sum_of_negatives.append(current_number)
 
print(count_positives)
print(sum_of_negatives)    
print(f"Count of positives: {len(count_positives)}\nSum of negatives: {sum(sum_of_negatives)}")