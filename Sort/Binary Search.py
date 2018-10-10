def binarySearch(arr, left, right, i):
    if right >= left:

        mid = left + (right - left) / 2

        if arr[mid] == i:
            return mid

        elif arr[mid] > i:
            return binarySearch(arr, left, mid - 1, i)

        else:
            return binarySearch(arr, mid + 1, right, i)

    else:
        return -1


print 'Enter no of array elements : '
ele=input()
arr=[0 for i in range(ele)]
print "Enter elements 1 by one"
for i in range(ele):
    arr[i] = input()

print "Enter no to be searched -"
index = binarySearch(arr, 0, len(arr) - 1, input())

if index != -1:
    print "Element is present at index %d" % (index+1)
else:
    print "Element is not present in array"