names = ['breno', 'bruno', 'bred', 'brenna', 'brenda']

print(names[:])

numbers = [2, 5, 3, 7, 2, 34, 7, 2]

print(max(numbers))

largest_number = numbers[0]

for n in numbers:
    if largest_number < n:
        largest_number = n

print(largest_number)

'''
list methods:
clear()
remove()
append()
insert()
pop()
count()
sort()
reverse()
copy()
index() - if the index doesn´t find the value, it returns an error. Another way is using 'in' to certify if the value 
exists. It returns True or False. By example:
v in v
'''

number_list = [2, 4, 5, 2, 74, 8, 3, 5, 2]

for number in number_list:
    if number_list.count(number) > 1:
        number_list.remove(number)


print(number_list)
