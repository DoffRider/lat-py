fname = input('Masukkan File : ')

if len(fname) < 1 : fname = 'warning.txt'

buka = open(fname)
for i in buka :
    i = i.rstrip()
    # print(i)
    wds = i.split()
    # print(wds)
    

