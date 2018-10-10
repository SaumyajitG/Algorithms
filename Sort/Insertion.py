def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        x = i - 1
        while x >= 0 and key < arr[x]:
            arr[x + 1] = arr[x]
            x -= 1
        arr[x + 1] = key

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
    insertionSort(arr)
    print ("Sorted array is:")
    if chk=="A":
        print arr
    else:
        print arr[::-1]