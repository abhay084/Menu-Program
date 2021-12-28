#linear search algorithm use the sequential approch to find the targeted data.
# Best-case complexity is O(1)
# Worst-case Performance is O(n)
# Average Performance O(n/2)

def LinearSearch(arr,target):

    for i in range(len(arr)):
        if(arr[i]==target):
            return i


    return -1


lst = [1,2,3,4,5,6,7,8,9,10]

target = int(input("value to be found : "))

result = LinearSearch(lst,target)

if(result == -1):
    print("target element is not found.")

else:
    print("element is present at the index ",result)


