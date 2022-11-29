while True:
    import calendar
    year = int(input("enter your year\n"))
    # month = int(input("enter your month\n"))
    calendar.setfirstweekday(calendar.SUNDAY)
    mycal = calendar.calendar(year)
    # mycal = calendar.month(year,month)
    print(mycal)
    print("enter c to continue and q to quit")
    ab = input()
    if ab=="q":
       break

