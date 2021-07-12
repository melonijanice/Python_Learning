def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1], arr[j]
                print(arr)
    
    print(arr)

bubblesort([5,3,4,8,1])
          
