#list demo
demo_list = [10, 16, 24, 77, 2, 14, 9]

#add values to the list
demo_list.append(5)
print(demo_list)

#get number of items in the list
number_of_items = len(demo_list)
print(len(demo_list))

#get values from the list
#get first value from the list
print("\n", demo_list[0], sep='')

#print all items in list
print("\n")
for deece in range(number_of_items):
    print(demo_list[deece])

#print items at even indexes
print("\n")
for index in range(1,number_of_items, 2):
    print(demo_list[index])
