


# function is called with all the items in the list and a new list is returned which contains items returned by that function for each item

list1=[1,3,4,5,7,8,11,13,2]

list1=list(map(lambda x: x+2, list1))

print(list1)