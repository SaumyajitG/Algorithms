
def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    strc=""

    Length = [[None] * (len2 + 1) for i in xrange(len1 + 1)]
    #print Length

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0 or j == 0:
                Length[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                Length[i][j] = Length[i - 1][j - 1] + 1
            else:
                Length[i][j] = max(Length[i - 1][j], Length[i][j - 1])

    return Length[len1][len2]







print "Enter 2 String one after the other : "
str1 = raw_input().upper()
str2 = raw_input().upper()
print "Length of LCS is ", lcs(str1, str2)