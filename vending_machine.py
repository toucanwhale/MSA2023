#set the amount due
amount_due = 50
print(amount_due)

#function to pay
def main(amount_due):
    #pay for remaining balance
    while amount_due > 0:
        try:
            payment = int(input("Insert coin: "))
        except ValueError:
            continue
        if payment == 1:
            amount_due = amount_due - payment
            print(f"Amount due: {amount_due}")
            continue
        elif payment == 5:
            amount_due = amount_due - payment
            print(f"Amount due: {amount_due}")
            continue
        elif payment == 10:
            amount_due = amount_due - payment
            print(f"Amount due: {amount_due}")
            continue
        elif payment == 25:
            amount_due = amount_due - payment
            print(f"Amount due: {amount_due}")
            continue
        else:
            continue
    #finish paying
    if amount_due <= 0:
        print(f"Thank you! \nChange due: {-amount_due}")


main(amount_due)