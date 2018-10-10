def missingNumbers(arr, n):
    XOR = arr[0]
    for i in range(1, n - 2):
        XOR ^= arr[i]
    for i in range(1, n + 1):
        XOR ^= i

    bitno = XOR & ~(XOR - 1)

    x = 0

    y = 0
    for i in range(0, n - 2):
        if arr[i] & bitno:
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    for i in range(1, n + 1):
        if i & bitno:
            x = x ^ i
        else:
            y = y ^ i

    print ("Two Missing Numbers are\n%d %d" % (x, y))

print "Enter array size"
arr = [0 for i in range(input())]
print "Enter elements - "
for i in range(len(arr)):
    arr[i]=input()

n = 2 + len(arr)
arr=sorted(arr,key=int)
print arr
missingNumbers(arr, n)