hitung = dict()
nama = ['udin','ujang','mamank','botak','udin','ujang','adi','botak','udin']

for i in sorted(nama):
    if i not in hitung:
        hitung[i] = 1
    else:
        hitung[i] = hitung[i]+1

print(hitung)
print(' ============================ ')

#fungsi get() untuk mengecek
#menggunakan idiom bisa menyingkat code, hasilnya sama dengan di atas
hitung1 = dict()
nama1 = ['udin','ujang','mamank','botak','udin','ujang','adi','botak','udin']
for ii in sorted(nama1) :
    #angka 0 diberikan untuk nilai default
    #jika nama tidak ada maka default 0
    #jika nama ada maka nilai default ditambah 1, atau singkatnya ditambah 1
    hitung1[ii] = hitung1.get(ii,0) + 1 #jadi lebih singkat
print(hitung1)