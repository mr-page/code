#create empty list
#addend the number that smaller than 100 also the multiple of 7 into the list
#print the list
empty_list = []
for i in range(1,101):
    if i < 100 and i % 7 == 0:
        empty_list.append(i)
print(empty_list)
#print the list in reverse order
print(empty_list[::-1])