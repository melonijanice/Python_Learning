def selectionsort(arr):
    for i in range(len(arr)-1):
        minindex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minindex]:
                minindex=j
        if minindex!=i:
            arr[i],arr[minindex]=arr[minindex],arr[i]
        
    print(arr)

selectionsort([5,3,4,8,1])
