angka = 0
counter = 0
print('Sebelum, ', angka)
for i in [9,41,12,3,74,15] :
    angka = angka + i
    counter = counter + 1
    print('total saat ini              : ',angka)
    print('angka saat array saat ini   : ',i)
    print('counter saat ini            : ',counter)

    print('')
print('rata2 = ', angka/counter)