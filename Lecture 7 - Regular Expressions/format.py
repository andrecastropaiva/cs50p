import re

'''
name = input("What's your name? ").strip()

# conditional to rearrange name if someone inputs two names with a comma in between them
if ',' in name:
    last, first = name.split(', ')
    name = f'{first} {last}'

print(f"Hello, {name}")
'''

name = input("What's your name? ").strip()
# matches = re.search(r'^(.+), *(.+)$', name) # commented out for the last option of code below

# conditionals
'''
if matches:
    last, first = matches.groups() # captures the groups we surrounded by paretheses above
    name = f'{first} {last}'
print(f'Hello, {name}')
'''

# OR

'''
if matches:
    last = matches.group(1) # captures the group 1 we surrounded by first paretheses above
    first = matches.group(2) # captures the group 2 we surrounded by 2nd paretheses above
    name = f'{first} {last}'
print(f'Hello, {name}')
'''

# OR

'''
if matches:
    name = matches.group(2) + ' ' + matches.group(1)
print(f'Hello, {name}')
'''

# OR ( with the new operator in python := allows us to assign something to a variable while getting a boolean response)

if matches:= re.search(r'^(.+), *(.+)$', name):
    name = matches.group(2) + ' ' + matches.group(1)
print(f'Hello, {name}')