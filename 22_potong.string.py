#jadi di dalam array nya ada pembatas "_ : _ "  bagian kiri mulainya dan bagian kanan akhir
#contoh di bawah menampilkan huruf dimulai dari index '0' sampai dengan index ke '3'

print('-----------')
kata = 'pisang'
print(kata[0:3])

print(kata[0:1])
print()

#jika kita input diluar nilai indexnya tidak ada masalah, dia tetap akan menampilkan hingga nilai index terakhir yang dimiliki
print('-----------')
print(kata[0:20])
print()

#mengambil potongan string
#menampilkan huruf terakhir
#contoh dibawah mengambil dari 2 huruf terakhir
#sedangkan index awalannya dikosongkan
print('-----------')
print(kata[:2])
print()

#begitu juga jika ingin memulai dari index tertentu
#contoh di bawah akan dimulai dari index yang dipilih hingga akhir

print('-----------')
print(kata[2:])
print()

#jika nilai indexnya dikosongkan hasilnya akan sama seperti memanggil semua index di dalam string tsb
print('-----------')
print(kata[:])
print()