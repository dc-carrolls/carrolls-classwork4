import os
name = input('Enter your name:')
os.system('clear')
age = int(input(f'{name[::-1]} enter your age:'))
os.system('clear')
response = input(f'{name} how does it feel to be {age:b}?')
os.system('clear')
print(response)
import platform
print(platform.python_version())