from ast import Global


def task1():
    stringa = 'абв бабв гггааа оаокакрпабв бвбвбвбврпгкра бвбвабвбврпгкра дададабв'
    a = stringa.split()
    c = a.copy()
    for item in a:
        if item.find('абв')!=-1:
            c.remove(item)

    b = ''
    for item in c:
        b+=item + ' '

    return b
print(task1())