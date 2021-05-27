buka = open('file2.txt')

for i in buka :
    i = i.rstrip()
    kata = i.split()
    if kata[0] != 'From':
        continue
    print(kata[2])
    print(len(kata))

#kode bisa berjalan tapi akan error
#karena pada kondisi if mencari di dalam list yang ada kata 'from'
#tapi karena di file tersebut juga ada blank atau list kosong
#maka itu yang menyebabkan error
#pada saat looping di awal berhasil tapi disaat bertemu list kosong maka error
#untuk itu diberi kondisi lagi untuk mencegah membaca list kosong

