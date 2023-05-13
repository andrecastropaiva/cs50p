'''
# prompting the user for their email...strip() prevents users from accidentally add a blank space
email = input("What's your email? ").strip()

# conditional
if '@' in email and '.' in email:
    print('Valid')
else:
    print('Invalid')
'''

'''
# prompting the user for their email...strip() prevents users from accidentally add a blank space
email = input("What's your email? ").strip()

# separating the email format in 2 formats, divided by the @
username, domain = email.split('@')

# conditionals
if username and domain.endswith('.edu'):
    print('Valid')
else:
    print('False')
'''

import re

# prompting the user for their email...strip() prevents users from accidentally add a blank space
email = input("What's your email? ").strip()


# re.search(pattern, string, flags) flags are optional but can be useful like re.IGNORECASE re.MULTILINE re.DOTALL
# patterns meaning
#   . means we accept any character except a newline
#   * means we accept 0 or more repetitions
#   + means we accept 1 or more repetitions
#   ? 0 or 1 repetitions
#   {m} means m repetitions (we pass a number to m)
#   {m, n} means m-n repetitions (we pass 2 numbers inside curly braces meaning a range between the 2 numbers we pass in)
#   ^ means matches the start of the string
#   $ matches the end of the string
#   [] means a set of characters for example a-z or A-Z or 0-9
#   [^] means complementing the set (basically the opposite as []... [^] means characters we want to exclude)

# conditionals... .search() is a method from regex to match for whatever we want in the user input in this case
# below we saying username can have 1 or more character to the left or to the right of the @ including a dot
# escape character means for the dot after it actually meaning dot and not any character
# the r at the beginning of the string is to tell python to not interpret any backslashes in the usual away...we just want python to
# interpret it as part of the .search() from regex
# [^@] for example means accept anything except an @ sign
# \w means any word character, numbers and the underscore
# \W not a word character
# \d means decimal digit
# \D means not a decimal digit
# \s means whitespace character
# \S not a whitespace character
# A|B means A or B
# (...) a group, for example (com|org|net)
# (?:...) non-capturing version

#if re.search(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$', email):
if re.search(r'^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$', email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')