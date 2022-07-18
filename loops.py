def linearSearch(arr,n,x):
    for i in range(0,n):
        if(arr[i] == x):
            return i
    return -1

array = [2,3,4,10,40,50,35]
x = 35
n = len(array)
result = linearSearch(array,n,x)

if result == -1:
    print("Element not found")
else:
    print(f"Element found in {result}")