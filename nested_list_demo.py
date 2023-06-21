#create a list
demo_list = [15, 8, 64, 25, 9, 11, 32, 41]

list_of_lists = [[2, 4, 7, 9], 
                 [3, 7, 8, 4],
                 [1, 8, 5, 2]]

#get data from lists
#print(demo_list[2])

#print the 8 in list of lists
#print(list_of_lists[1][2])

#print all the values in my list_of_lists matrix
#for number in demo_list:
    #print(number)
#for list in list_of_lists:
    #for number in list:
      #  print(number)

#iterate over the rows
for row in range(len(list_of_lists)):
    print(f"Row {row + 1} Values")
    for column in range(len(list_of_lists[row])):
        print(list_of_lists[row][column])