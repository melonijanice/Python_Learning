#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(list):
    for index in range(0,len(list),1):
        if list[index]>0:
            list[index]='Big'
    return list

biggie_size([-1, 3, 5, -5])

#Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def count_positives(list):
    sum=0
    for element in list:
        if element>0:
            sum=sum+1
    list[len(list)-1]=sum
    return list

count_positives([1,6,-4,-2,-7,-2])

#Create a function that takes a list and returns the sum of all the values in the array.
def sum_total(list):
    sum=0
    for elements in list:
        sum=sum+elements
    return sum

sum_total([1,2,3,4])

#Average - Create a function that takes a list and returns the average of all the values.
def average(list):
    sum=0
    for elements in list:
        sum=sum+elements
    return sum/len(list)

average([1,2,3,4])

def Length(list):
    return len(list)

Length([37,2,1,-9])

#Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def Minimun(list):
    if(len(list)==0):
        return False
    else:
        temp=list[0]
        for element in list:
            if(element<temp):
                temp=element
        return temp

Minimun([])

#Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def Maximum(list):
    if(len(list)==0):
        return False
    else:
        temp=list[0]
        for element in list:
            if(element>temp):
                temp=element
        return temp

Maximum([])

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

def ultimate_analysis(list):
    sum=0
    Min=list[0]
    Max=list[0]
    ultdict={}
    for elements in list:
        sum=sum+elements
        if(elements<Min):
            Min=elements
        elif(elements>Min):
            Max=elements
    print(Min)
    ultdict["Sum"]=sum
    ultdict["Average"]=sum/len(list)
    ultdict["Length"]=len(list)
    ultdict["Min"]=Min
    ultdict["Max"]=Max
    return ultdict

ultimate_analysis([37,2,1,-9])


#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)

def reverse_list(list):
    temp=list[0]
    for index in range(int(len(list)/2)):
        temp=list[index]
        list[index]=list[len(list)-1-index]
        list[len(list)-1-index]=temp
    return list

print(reverse_list([37,2,1,-9]))




