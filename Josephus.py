def josephus(ls, skip):
    skip -= 1
    idx = skip
    while len(ls) > 1:
        print ls.pop(idx)
        idx = (idx + skip) % len(ls)
    print 'survivor: ', ls[0]

print "Enter No of survivors : "
num=input()
arr=[i for i in range(1,num)]
print "Enter value of k-skip"
josephus(arr,input())