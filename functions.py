def file_to_list(file):
    with open(file,"r") as f:
        content = f.read()

    ls = content.strip().split('\n')
    return ls

def search_word(file,str):
    ls = file_to_list(file)
    result = []
    for name in ls:
        if str in name:
            result.append(name) 
    return result