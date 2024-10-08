def sum(*args):
    accumulate = 0
    for arg in args:
        accumulate += arg
        
    return accumulate
sum(8,3,5)
#print(sum(8,3,5))

def rm():
    with open("abla1.txt","w") as file:
        file.write('')
        
def last(*args):
    ls = list(args)
    st = list(set(ls))
   # return sorted(st)
    print(sorted(args)) 
st = {100,2,23200,235,373}
print(sorted(st))