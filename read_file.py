#reading files in python
#open the file
data_file = open("file.txt", "r")

menu_items = {}

for line_of_data in data_file:
    print(line_of_data)
    #split line of data at the ","
    keys_values = line_of_data.split(", ")
    #create an entry to the dictionary]
   # deece = [keys_values[0]]
    #nuts = float(keys_values[1])
    menu_items[keys_values[0]] = float(keys_values[1])
print(menu_items)
data_file.close()

for item, price in menu_items.items():
    print(f"{item}: {price}")