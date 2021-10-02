def binary_search(list, term):
    #finding length of list
    list_size = len(list)
    #loop through list and returns True if term equals number in list otherwise returns false
    for i in range(list_size):
        if term == list[i]:
            return True
    return False

my_list= [0,1,3,8,14,18,19,34,52]

print(binary_search(my_list,3))
print(binary_search(my_list,17))