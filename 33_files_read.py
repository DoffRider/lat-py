ffile = open('file.txt')
#membaca isi file
baca = ffile.read()

#menghitung karakter dari string yang ada di objek
print(len(baca))
print()

#membaca karakter dari awal hingga no index yang di tuju
print(baca[:26])