def file_to_list(file):
    with open(file,"r") as f:
        content = f.read()

    ls = content.strip().split('\n')
    return ls