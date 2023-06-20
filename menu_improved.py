#define menu
def read():
    data_file = open("file.txt")
    menu_items = {}
    for line_of_data in data_file:
        #split line of data at the ","
        keys_values = line_of_data.split(", ")
         #create an entry to the dictionary]
        menu_items[keys_values[0]] = float(keys_values[1])
    data_file.close()
    return(menu_items)

#loop the prompt for ordering
def main():
    total = 0.00
    while True:
        try:
            prompt = input(f"Your current total: ${total:.2f}. What would you like to order?: ").title()
            if prompt == "End":
                print(f"Your total will be: ${total:.2f}")
                break
            price = (read()[prompt])
            total += price
            print(f"Total = ${total:.2f}")
        except KeyError:
            print("Please enter valid menu item")
            continue

main()