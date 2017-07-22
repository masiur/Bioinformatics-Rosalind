def PatternCount(string,patrn):
    cnt= 0
    indx = 0
    while True:
        indx = string.find(patrn, indx)
        if indx >= 0:
            cnt += 1
            indx += 1
        else:
            break
    return cnt
string = input()
patrn = input()
print(PatternCount(string, patrn))