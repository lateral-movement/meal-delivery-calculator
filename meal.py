import numpy
import person

def main():

    error_message = "Must enter a valid USD amount."

    num_people = input("Enter number of people on the order: ")
    try:
        num_people = int(num_people)
    except ValueError:
        print("Must enter a natural number.")
        return -1

    tax = input("Enter tax: ")
    try:
        tax = float(tax)
    except ValueError:
        print(error_message)
        return -2

    tip = input("Enter tip: ")
    try:
        tip = float(tip)
    except ValueError:
        print(error_message)
        return -3

    fees = input("Enter all associated fees: ")
    fees = fees.split()
    try:
        usable_fees = [float(fee) for fee in fees]
    except ValueError:
        print(error_message)
        return -3
