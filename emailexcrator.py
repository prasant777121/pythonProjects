# Email Collector

import re

str ='''
Lorem ipsum harshitgupta7861@gmail.com dolor sit amet, charugupta2000@yahoo.com consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut omgupta352000@gmail.com aliquip ex 
ea commodo consequat. Duis aute irure gmai.@netflix.com dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non harshit@gupta comproident, sunt in culpa qui officia deserunt mollit anim id est laborum.abc@gmail.com
'''
email = re.findall(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]+",str)

print(email)

# email =re.findall("\S+@\S+.\S", str)
# print(email)
