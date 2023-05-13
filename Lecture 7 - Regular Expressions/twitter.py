'''
url = input('URL: ').strip()

username = url.removeprefix('https://twitter.com/') # to extract only the username which in case of twitter comes at the end of the url
print(f'Username: {username}')
'''

import re

# the re library has a method called sub() meaning substitution...see below
# re.sub(pattern, repl, string, count=0, flags=0)

url = input('URL: ').strip()

# parentheses to group each part, ? to make it optional being there or not, backslash dot to escape the dot, ^ to match the start
'''
username = re.sub(r'^(https?://)?(www\.)?twitter\.com/', '', url)
print(f'Username: {username}')
'''

# OR to avoid someone just entering the main url without the username at the end (which code abve wouldn't work), we can use .search()
# in a conditional
# ?: before www means NON-capturing...regardless if we type that it won't capture it

matches = re.search(r'^(https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$', url, re.IGNORECASE) # searching user url to extract just the username (last part url)

if matches:
    print(f'Username: ', matches.group(2)) # using .group(1) referring to the 2nd position of the matches variable which is url