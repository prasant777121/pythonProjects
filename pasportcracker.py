from random import *
user_pass = input("enter your passport\n")
password ="abcdefeghijklmnopqrstuvwxyz1234567890"
password_list = list(password)
guess = ""
while(guess !=user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password_list[randint(0,35



        )]
        guess = str(guess_letter) + str(guess)
    print(guess)
print("your password is",guess)