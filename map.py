nums = [2,5,7,8,22]
# mapped_nums = []
# for n in nums:
#     x = n * 2
#     mapped_nums.append(x)

#mapped_nums = [n*2 for n in nums]
mapped_nums = map(lambda n: n * 2,nums)
print(list(mapped_nums))


names = ['ahmad','samer','muhammad']
mapped_names = map(lambda n: f'Mr. {n}',names)
print(list(mapped_names))

ls = ['Mr. ahmad', 'Mr. samer', 'Mr. muhammad']
m = map(lambda n: n[:3],ls)
print(list(m))

names1 = ['ahmad','samer','muhammad']
mapped_names1 = map(str.capitalize,names1)
print(list(mapped_names1))

names2 = ['ahmad','samer','muhammad']
mapped_names2 = map(lambda n: f'{n} abla',names2)
print(list(mapped_names2))

names3 = ['ahmad','bela','amin']
names4 = ['abla','freund','mohammed']
full_names = []
for i,n in enumerate(names3):
    x = n +' '+ names4[i]
    full_names.append(x)
    
full_names2 = [n +' '+ names4[i] for i,n in enumerate(names3)]
    
print(full_names2)

    

