#menyatakan variabel sebagai dictionary
kumpulan = dict()

#mengisi key (kiri) dan Value(kanan)
kumpulan['buku komedi'] = 12
kumpulan['buku pelajaran'] = 5

print(kumpulan)
print()
#atau di isi sekaligus (dictionary literals)
perkakas = {'tukul' : 1, 'paku' : 22, 'meteran' : 14, }
print(perkakas)

#isinya juga bisa dirubah
print()
perkakas['tukul'] = 111
print(perkakas)

#atau ditambah(atau operasi lainnya) valuenya
print()
perkakas['tukul'] = perkakas['tukul'] + 1
print(perkakas)