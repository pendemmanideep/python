

#filter is called with all the items in the list and a new list to returned which contains items for which evalutes the true


list1=[1,5,4,6,8,11,3,12]

list1=list(filter(lambda x: (x%3==0),list1))

print(list1)