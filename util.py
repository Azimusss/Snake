def index(list, el):
    return print(list.index(el))

def xy(list, el):
    i = 0
    while True:
        if el in list[i]:
            x = i + 1
        else:
            i = i + 1