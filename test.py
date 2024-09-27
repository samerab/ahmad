
def add(leng,first=0,second=1):
    numbs = [first,second]
    while len(numbs) != leng:
        added_n = numbs[-1] + numbs[-2]
        numbs.append(added_n)
    print(numbs)

add(20,2,3)
