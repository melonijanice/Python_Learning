def sum_to_digit(number):
    sum=0
    while(number>0):
        sum=number%10+sum
        number=number//10
    if(sum>9):
        sum=sum_to_digit(sum)
    return sum


sum_to_digit(1128)
