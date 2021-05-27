abc = 'halo selamat pagi !'
pisah = abc.split()
print(pisah)
print(len(pisah))

#akan memecah string dan menyimpannya ke dalam list setiap ada spasi

#split jika ad karakter di dalamnya
abc2 = 'halo;selamat;pagi'
pisah2 = abc2.split()
print()
print(pisah2)
print(len(pisah2))

#untuk bisa memecahnya berikan isian di fungsi splitnya
abc3 = 'halo;selamat;pagi'
pisah3 = abc3.split(';')
print()
print(pisah3)
print(len(pisah3))