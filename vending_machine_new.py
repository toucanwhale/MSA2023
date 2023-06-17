#get user input for amount
def userinput():
    while True:
        try: 
            pay_amount = int(input("Insert Coin: "))
            if pay_amount not in [1, 5, 10, 25]:
                print("please enter in a valid coin")
            else: 
                return pay_amount
        except ValueError:
            print("enter in a valid coin")
            continue

#use user input to subtract from amount due
def pay():
    amount_due = 50
    print("You owe:", amount_due)
    while amount_due > 0:
        amount_due = amount_due - userinput()
        if amount_due >0:
            print(amount_due, "cents")
        else:
            break
    if amount_due <= 0:
        print(f"Thank you! \nChange Due: {-amount_due} cents")

pay()