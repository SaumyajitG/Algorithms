def heap(arr, n, i):
    largest = i  
    l = 2 * i + 1
    r = 2 * i + 2


    if l < n and arr[i] < arr[l]:
        largest = l


    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 
        heap(arr, n, largest)


def heapDes(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]

        heapDes(arr, n, smallest)



def sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heap(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)

def sortDes(arr):
    n = len(arr)

    for i in range(n/2-1, 0, -1):
        heapDes(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapDes(arr, i, 0)


print 'Enter no of array elements : '
ele=input()
arr=[0 for i in range(ele)]
print "Enter elements 1 by one"
for i in range(ele):
    arr[i] = input()
chk=0
while chk != 1:
    print "Ascending or Descending (A/D) : "
    inp = raw_input()
    if (inp.upper() not in {"A", "D"}):
        print "Choose correctly"
    else:
         chk+=1
         if inp.upper() == "A":
            sort(arr)
            n = len(arr)
            print "Sorted array is"
            for i in range(n):
                print "%d" % arr[i]

         else:
            sortDes(arr)
            n = len(arr)
            print "Sorted array is"
            for i in range(n):
                print "%d" % arr[i]