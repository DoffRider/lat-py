buka = input('Masukkan nama file : ')
bbuka = open(buka)

kamus = dict()
#looping file tadi setiap baris
for i in bbuka :
    #kata di baris itu dipecah per kata menjadi array dan disimpan di variabel
    kata = i.split()
    #setelah dipecah menghitung berapa kali kata tersebut muncul
    for o in kata:
        kamus[o] = kamus.get(o,0) + 1

kata_muncul = None
jumlah_kata = None

#kita atur i sebagai key dan o sebagai value
for i,o in kamus.items():
    if jumlah_kata is None or o > jumlah_kata:
        kata_muncul = i
        jumlah_kata = o

print('Yang sering muncul : ', kata_muncul,' ,Berjumlah : ',jumlah_kata, ' kali')
