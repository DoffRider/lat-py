#pada python dalam perulangan for bisa memanggil 2 variabel sekaligus
#karena berisikan key dan value maka menggunakan kurung kurawal
nama = {'udin':2,'ujang' : 2,'mamank' : 2,'botak': 22,'udin':13,'ujang':21,'adi':90,'botak':45,'udin':88}

#jika ditambah fungsi items maka akan mendapat key dan value
#jika nama.key hanya key
#jika nama.value hanya value
for i,ii in nama.items():
    print(i,ii)
