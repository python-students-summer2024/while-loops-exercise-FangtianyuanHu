def get_starting_number():
    number_beer = input("How many bottles of beer on the wall? ")
    while number_beer.isnumeric() == False or int(number_beer)<1:
        print("enter a correct number above or equal 1.")
        number_beer = input("How many bottles of beer on the wall? ")
    return int(number_beer)

def sing(singing):
    n = singing
    ssing = True
    while ssing:
        print(f"{n} bottle{'s' if n > 1 else ''} of beer on the wall, {n} bottle{'s' if n > 1 else ''} of beer.")
        if n > 1:
            print(f"Take one down, pass it around, {n-1} bottle{'s' if n-1 > 1 else ''} of beer on the wall.")
        else:
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            ssing = False
        n = n - 1
