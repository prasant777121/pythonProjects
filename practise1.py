print('welcome to the age dectator you ca enter your age or year you born')
a = int(input())
if a<100:
    print('age is successfully deceted')
    print(f"you will be 100 years old in {100-a}")


elif 1900<a<2020:
    print("your year has been successfully deceted ")
else:
    print("enter vaild year or age")
    exit()
if 1900<a<2020:
    b= 2020-a
    print('your age is',b)
    print(f"you will be 100 years old in {100-b}")




