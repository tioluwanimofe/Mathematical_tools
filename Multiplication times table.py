print(" What times table would you like?")
number = int(input("Please write the number here: "))
limit = int(input("Write you write your limit: "))


def table():
    mofe = []
    num = range(limit)
    for i in num:
        mofe.append(i * number)
    print(mofe)


table()
