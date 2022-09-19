mystr = 'AAABBBBCCCCCDDDE   FFFFOO4'

def rle_compress(s:str):
    encoding = []
 
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i += 1
 
        # добавляет к результату текущий символ и его количество в виде кортежа
        encoding.append((s[i], count))
        i += 1

    return encoding

def rle_decompress(encS:str):
    s = ''
    a = eval(encS)
    for item in a:
        s += item[0]*int(item[1])

    return s
    

def task4(s):
    with open('encode.txt', 'w') as file:
        file.write(str(rle_compress(s)))

    with open('encode.txt', 'r') as file:
        encode = file.read() 

    with open('decode.file', 'w') as file2:
        file2.write(rle_decompress(encode))

task4(mystr)