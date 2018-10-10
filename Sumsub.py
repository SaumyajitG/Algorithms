def subset(array, num):
    if num < 0:
        return
    if len(array) == 0:
        if num == 0:
            yield []
        return
    for solution in subset(array[1:], num):
        yield solution
    for solution in subset(array[1:], num - array[0]):
        yield [array[0]] + solution

print "Enter size of array - "
n=input()
arr = [0 for i in range(n)]
print "Enter values - "
for i in range(len(arr)):
    arr[i]=input()
print "Enter sum = "
sum=input()
print sum
print list(subset(arr,sum))
