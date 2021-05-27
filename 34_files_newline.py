buka = open('file.txt')
for i in buka :
    if i.startswith('halo') :
        print(i)
print('===========================')
#hasilnya akan memberikan spasi setiap ditemukannya kondisi if

# halo bu\n
# \n
# halo pak
# \n
# halo kak
# \n
# halo dek


#maka disetiap pengulangannya akan kita hapus enter kebawahnya (\n) menggunakan fungsi strip
buka1 = open('file.txt')
for i1 in buka1 :
    i1 = i1.rstrip()
    if i1.startswith('halo') :
        print(i1)