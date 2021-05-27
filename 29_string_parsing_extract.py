data = 'dari iwak.institut@hehe-boay.ac.id Sab Mei  5 09:12:25 2021'

#mencari posisi no index dari '@'
posisi1 = data.find('@')
print('posisi 1 : ',posisi1)
print()

#mencari blank (spasi) pada variabel 'data' dengan starting poin 
# yang didapat dari  no index posisi1
posisi2 = data.find(' ',posisi1)
print('posisi 2 : ',posisi2)
print()

#dengan ditambahnya no index maka akan maju ke huruf selanjutnya
#maka hasilnya tampilkan kata dari posisi no index ke 19 (h) sampai 34 (d)
nama = data[posisi1+1 : posisi2]
print('Alamat web : ',nama)