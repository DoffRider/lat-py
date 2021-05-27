# disini kita akan memberi kondisi tambahan agar error saat membaca list kosong
buka = open('file2.txt')

#jika menggunakan or perhatikan dimana peletakannya
#karena urutan pengecekan kondisi dimulai dari depan
#kalau contoh di bawah ditukar kondisi ifnya 
#jadi pengecekan kata 'From' lalu len terlebih dahulu maka akan error seperti di latihan 42

for i in buka :
    i = i.rstrip()
    kata = i.split()
    if  len(kata) < 3 or kata[0] != 'From' :
        continue
    print(kata[2])

#atau

# for i in buka :
#     i = i.rstrip()
#     kata = i.split()
#     if len(kata) < 3 :
#         continue
#     if  kata[0] != 'From' :
#         continue
#     print(kata[2])

#atau

# for i in buka :
#     i = i.rstrip()
#     kata = i.split()
#     if kata == ' ' :
#         continue
#     if  kata[0] != 'From' :
#         continue
#     print(kata[2])