def divider(arr, low, high):
    i = (low - 1)  
    pvt = arr[high] 

    for j in range(low, high):
        if arr[j] <= pvt:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort(arr, low, high):
    if low < high:
        piv = divider(arr, low, high)

        quickSort(arr, low, piv - 1)
        quickSort(arr, piv + 1, high)



print 'Enter no of array elements : '
ele=input()
arr=[0 for i in range(ele)]
print "Enter elements 1 by one"
for i in range(ele):
    arr[i] = input()
ch = 0
while ch!=1:
    print "Ascending or Descending (A/D) -"
    chk=raw_input().upper()
    if chk not in {"A", "D"}:
        print "Provide correct option"
        continue
    else:
        ch+=1
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print ("Sorted array is:")
    if chk=="A":
        print arr
    else:
        print arr[::-1]