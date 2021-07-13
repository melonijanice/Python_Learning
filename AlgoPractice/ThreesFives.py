def ThreesFives(min=1,max=20):
    sum=0
    for i in range(min,max):
        if i%3==0 or i%5==0 and not (i%3==0 and i%5==0):
            print(i)
            sum=sum+i
    print(sum)

ThreesFives()
