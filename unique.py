with open("abla.txt","r") as file:
    content = file.read() # "fdsfds\ndfhds\ndhhhf\n"
ls = content.split('\n')
unique = []
for i in ls:
    if i not in unique:
        unique.append(i)

str = '\n'.join(unique)

with open("abla.txt","w") as file:
    file.write(str)
