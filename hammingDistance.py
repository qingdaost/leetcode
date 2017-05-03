def hammingDistance(x, y):
    xlist = list(bin(x))
    ylist = list(bin(y))
    xlist.reverse()
    ylist.reverse()
    i = 0
    n = 0
    while xlist[i] != 'b' and ylist[i] != 'b':
        if xlist[i] != ylist[i]:
            n += 1
        i += 1
    if xlist[i] == 'b':
        while ylist[i] != 'b':
            print(ylist[i])
            if ylist[i] == '1':
                n += 1
            i += 1
    else:
        while xlist[i] != 'b':
            if xlist[i] == '1':
                n += 1
            i += 1
    return n
    
def main():
    print(hammingDistance(1577268,258755))
    
main()
            