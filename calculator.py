# def calculator():
#     print("enter first number")
#     a=int(input())
#     print("enter second number")
#     b=int(input())
#     print("enter*,-,+,**")
#     c=(input())
#     if c== "*":
#         print(a*b)
#     elif c=="+":
#         print(a+b)
#     elif c=="-":
#         print(a-b)
#     elif c=="**":
#         print(a**b)
#     else:
#         print("enter vaild number")
#
#
#     again()
#
# def again():
#     cal_again = input('''
#     Do you want to calculate again?
#     Please type y for YES or n for NO.
#     ''')
#
#     if cal_again == 'y':
#         calculator()
#     elif cal_again == 'n':
#         print("See You Later")
#     else:
#         again()
#
# calculator()

# another way
while True:
    print("enter first number")
    a = int(input())
    print("enter second number")
    b = int(input())
    print("enter*,-,+,**")
    c = (input())
    if c == "*":
        print(a * b)

    elif c == "+":
        print(a + b)

    elif c == "-":
        print(a - b)
    elif c == "**":
        print(a ** b)
    else:
        print("enter vaild number")

    print("enter q  to quit and c to contiue")
    ab=input()

    if ab =="q":
        break