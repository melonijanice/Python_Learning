#1
for x in range(150):
    print(x)

#2
for x in range(5,1000,5):
    print(x)
#3
for x in range(1,101):
    if x % 5==0:
        print("Coding")
    elif x % 10==0:
        print("Coding Dojo")
    else:
        print(x)

#4
sum=0
for x in range(500000):
    if x%2 !=0:
        sum=sum+x
print(sum)

#5
for x in range(2018,0,-4):
    print(x)

#6
lowNum=2
highNum=13
mul=3
for x in range(lowNum,highNum,1):
    if x%mul==0:
        print(f"{lowNum},{highNum},{x}")