hit = dict()
print('Masukkan Kalimat = ')
inpt = input('')

kalimat = inpt.split()
print()

print('Kalimat Anda : ', kalimat)
print()
print('sedang di proses..')
print()


for i in kalimat:
    #mengecek apakah sudah ada kalimat yang sama di dict()
    #jika tidak ada diberi nilai deefault 0
    #jika ada maka tambahkan 1
    hit[i] = hit.get(i,0) + 1

print()
print('Jumlah kata : ',hit)