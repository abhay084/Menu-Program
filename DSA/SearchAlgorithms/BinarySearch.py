def BinarySearch(arr,value):
    
    min_index = 0
    max_index = len(arr)
    while True:
        while(min_index<max_index):


            mid_index = int((min_index + max_index)/2)
            if(arr[mid_index]==value):
                return mid_index
            else:
                if(value>arr[mid_index]):
                    min_index=mid_index
            
                else:
                    max_index=mid_index
            




print("To process with Binary Search your data must be in sorted order.")
print("Here i am cosidering the sorted data is in ascending oeder.")

print("Time complexity for binary search is O(log n) where n is equal to number of elements.")

lst = [0,1,2,3,4,5,6,7,8,9,10]

target = int(input("enter the element to be found : "))

x=BinarySearch(lst,target)

print("the value present at index ",x)
