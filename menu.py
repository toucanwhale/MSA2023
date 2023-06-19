#define menu
menu = {"Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00}
total = 0.00
#loop the prompt for ordering
while True:
    try:
        prompt = input(f"Your current total: {total:.2f}. What would you like to order?: ").title()
        if prompt == "End":
            print(f"Your total will be: {total:.2f}")
            break
        price = (menu[prompt])
        total += price
        print(f"Total = ${total:.2f}")
    except KeyError:
        print("Please enter valid menu item")
        continue