#Finding the greatest value from the list given by the user
num = int(input('Enter number of elements:\n')) #getting number of elements in list
list = [] #creating blank list
i=1
while i<=num: #looping to get all elements
    element = int(input(f'Enter number {i}:\n'))
    list.append(element) #inserting elements
    i=i+1
list.sort(reverse=True) #sorting list, reversing to get greatest first
print(f'Greatest value in the list is: {list[0]}') 