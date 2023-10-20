'''
long
comments
'''

# Short comments

course = 'python for beginners'

# it´s possible to access from the final of a string using negative values to set how many numbers you want to back

print(course[-1])

# it´s possible set from/to string position you want to read using n:n

print(course[5:10])
print(course[5:])
print(course[:10])
print(course[1:-1])

# use f'' to format strings

name = 'Breno'
last = 'Macedo'

message = f'{name} [{last}] is a coder'

print(message)

# string methods

# len() shows the string size
print(len(course))

# uppercase
# the command don´t change the variable. just uppercase it
print(course.upper())
print(course)

# lowercase
# the command don´t change the variable. just lowercase it
print(course.lower())

print(course)

# find string position
# if it doesn´t find, it returns -1
print(course.find('fo'))

# replace string
# the method doesn´t change the variable
# if it doesn´t find, it doesn´t do anything
print(course.replace('ab', 'FOR'))


# search if there is a string
# it returns True or False
print('Python' in course)


# uppercase the first letters
print(course.title())
