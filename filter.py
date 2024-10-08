names = ['samer','sayed','sasuki','ahmad','adam','shamad']
# result = []
# for n in names:
#     if n.startswith('s') and n.endswith('r'):
#         result.append(n)
#result = [n for n in names if n.startswith('s') and n.endswith('r')]

l = lambda n: n.startswith('s')

f1 = filter(l,names)

print(list(f1))
# even: 2,4,6,8...
# odd: 3,5,7...
nums = [3,6,88,77,60,55]
f = filter(lambda n:n%2 == 1,nums)

print(tuple(f))

# ---------------------------
dict = {}