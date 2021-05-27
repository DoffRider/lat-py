input_file = input('Buka filenya : ')
#memberi pesan error jika file tidak ad
try:
    buka = open(input_file)
except:
    print('File tidak bisa dibuka atau salah')
    quit()

hitung = 0
for i in buka :
    if i.startswith('halo') :
        hitung = hitung +1
print('Ada : ',hitung,' kata halo di ',input_file)