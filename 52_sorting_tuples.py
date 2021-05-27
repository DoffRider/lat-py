from abc import abstractproperty
from os import read


fname = input('Masukkan File : ')
#mengecek apakah file dimasukkan ada
if len(fname) < 1 : fname = 'clown.txt'
try:
    op = open(fname)
except:
    print('File tidak bisa dibuka atau salah')
    quit()

dc = dict()
for i in op:
    i = i.strip()
    kata = i.split()
    for i in kata:
        #masukkan ke dictionary
        dc[i] = dc.get(i,0) + 1

print(dc)
print('\n')

#coba dirubah ke list dan ditambah sortir
#saat dirubah ke list maka menjadi tuple
#dan jika menjadi list akan berubah pasangannya jadi key - (key,value)
#(key,value) dari dict, ketika dirubah ke list maka yg didalam kurung jadi value
x = sorted(dc.items())

#tampilkan data (key) dari 0 sampai 4
print(x[:5])
print('\n')

tmp = list()
for k,v in dc.items():
    #key dan value dari dict diatas kedalam variabel baru
    #sesuaikan kebutuhan jika ingin value atau key duluan
    newtuple = (v,k)
    #lalu di tambahkan ke dalam list
    #maka setiap key+value dari dict akan mempunyai key lagi pada list
    tmp.append(newtuple)

tmp = sorted(tmp, reverse=True)
print('Sortir ',tmp)
print('\n')

for i,o in tmp[:5]:
    print(o,i)
print('\n')

#contoh penulisan 1 line
# print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )