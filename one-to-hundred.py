str = ""
for i in range(1,101):
    str += f"ahmad{i}\n"
with open("one-to-hundred.txt","w") as file:
    file.write(str)

# for i in range(1,101):
#     with open("one-to-hundred.txt","a") as file:
#         file.write(f"ahmad{i}\n")
