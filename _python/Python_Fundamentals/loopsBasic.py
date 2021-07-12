#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    numbers=[]
    for x in range(num,-1,-1):
        numbers.append(x)
    return numbers
print(countdown(5))

#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def printone_returnother(num):
    print(num[0])
    return num[1]

printone_returnother([1,2])

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(list):
    return(list[0]+len(list))

first_plus_length([1,2,3])

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(list):
    newList=[]
    if len(list)>2:
        for element in list:
            if element>list[1]:
                newList.append(element)
        return newList
    else:
        return False

values_greater_than_second([5,2,3,2,1,4])


#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(a,b):
    newList=[]
    for i in range(0,a):
        newList.append(b)
    return newList

length_and_value(4,7)



