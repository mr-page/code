# create empty list
# addend the number that smaller than 100 also the multiple of 7 into the list
# print the list
empty_list = []
for i in range(1, 101):
    if i < 100 and i % 7 == 0:
        empty_list.append(i)
print(empty_list)
# print the list in reverse order


# get user's age
# if the age is less than 18, print "you are not allowed to vote"
# if the age is between 18 and 65, print "you are allowed to vote"
# if the age is greater than 65, print "you are not allowed to vote"
age = int(input("Enter your age: "))
