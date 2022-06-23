"""---------------------------------------------------------------------------------------------------------------------
# This is a Python script created to convert currency.
# The currencies were copper, silver, gold, platinum and electrum
# he values of which were 1, 10, 10, 10, and 5 respectively

# When client was asked what they would like they responded with:

"Output money in the most convenient array of g,s,b (not platinum) if possible
and allow me to take off any amount of currency
Eg we had

114g 3s 2b

I wanted to spend 5 silver

It would automatically do the sum and give me

113 g 8s 2b"

---------------------------------------------------------------------------------------------------------------------"""
import sys


def start():
    # This function prints python version as well as informs user that program has started
    print("========================STARTING========================")
    print("python version: "+sys.version)
    print("\n")
    print("Please input starting currency:")
    return input_currency()


def input_currency():
    currency_type = ["B:", "S:", "G:", "P:", "E:"] # TODO : put this in a values function to be called

    # Prompts user to input currency for each currency type
    while True:
        currency = []
        i = 0
        while i < len(currency_type):
            try:
                currency.append(int(input(currency_type[i])))
                i += 1
            except:
                print("Oops, something went wrong, please try again")

        # Check to see if they put it in correctly
        y_n = ""
        while True:
            print("\nC%d S%d G%d P%d E%d input as currency" % (
                currency[0], currency[1], currency[2], currency[3], currency[4]))
            y_n = input("is that correct? (Y/N)\n").lower()

            if y_n[0].lower() == "y":
                return currency
            elif y_n[0].lower() == "n":
                print("\nPlease reenter the values")
                break
            else:
                print("\nThat was neither yes nor no.\nCould you please could you put that in again?")


def refactor(currency):
    # removes all - values for currency and sorts into smallest change possible
    currency_value = [1, 10, 10, 10, 5] # TODO : put this in a values function to be called
    # If larger than currency above, div by it and keep remainder (add division to currency above)
    for i in range(len(currency)-1):
        if currency[i] >= currency_value[i+1]:
            currency[i+1] = currency[i+1] + currency[i]//currency_value[i+1]
            currency[i] = (currency[i] % currency_value[i+1])
        # If smaller than currency above, div by it +1 and take off currency above
        # (add the div +1 times currency above value)
        elif currency[i] < 0:
            remainder = (currency[i]//currency_value[i+1])-1
            currency[i] = currency[i] - (currency_value[i+1]*remainder)
            currency[i+1] = currency[i] - remainder
        else:
            pass
    return currency


def convert(currency): # TODO : make this variable
    currency[3] = currency[4]*5 + currency[3]
    currency[2] = currency[3]*10 + currency[2]
    currency[3] = 0
    currency[4] = 0
    return currency


def calculation(currency, x):
    # if x is 2 it will add currency, if x is 3 it will subtract
    i = 0
    modifier = input_currency()
    if x == 2:
        for j in currency:
            currency[i] = currency[i] + modifier[i]
            i += 1
    elif x == 3:
        for j in currency:
            currency[i] = currency[i] - modifier[i]
            i += 1
    return currency

"""
#for saving and loading data
def pre_load_data(file_name):
    try:
        with open(file_name, 'r') as f:
            save = f.read()
            save_location = save.split("/n")
        f.close()
    except:
        f = open(file_name, "x")
    print(save_location)
    return save_location
"""

if __name__ == '__main__':
    option = 0
    currency = []
    currency = start()
    currency = refactor(currency)

    while option != 4:
        print("\nWhat would you like to do?\n")
        try:
            option = int(input("===Options===\n1-Print Current Balance \n2-Add Payment\n3-Subtract Costs\n4-End\n"))
        except:
            pass
        if option == 1:
            currency_temp = convert(currency)
            print("C%d S%d G%d "% (currency_temp[0], currency_temp[1], currency_temp[2]))

        elif option == 2 or 3:
            currency = refactor(calculation(currency, option))
            currency_temp = convert(currency)
            print("C%d S%d G%d " %(currency_temp[0], currency_temp[1], currency_temp[2]))
        else:
            print("not an option")
    exit()

