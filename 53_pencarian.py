import re
x = '2 angka Favoritku adalah nomer 14 dan 46'

#mencari semua angka yang mengandung anga 0 sampai 9
y = re.findall('[0-9]+',x)
print(y)

#saat menggunakan re.findall() biasanya akan mengembalikan list nol atau lebih sub-string yang cocok dengan ekspresi

#mencari huruf yang mengandung huruf vokal dan huruf besar
#jika hasil pencarian tidak ada, maka akan mengambalikan list kosong
yy = re.findall('[AEIOU]+',x)
print(yy)

#greedy match
x2 = 'From: Using the: character'
#mencocokan string dengan dimulai huruf F dan di akhiri ':' (titik dua)
#pada variabel x2 terdapat dua buah tanda ':' jika menyesuaikan kondisi yang kita atur maka akan pencarian akan berhenti di From:
#tapi di greedy match akan mencari yang terpanjang/terbesar.
#maksudnya jika ternyata huruf/tanda ada banyak maka akan berhenti di lokasi ditemukannya terakhir.
y2 = re.findall('^F.+:',x2)
print(y2)

#non-greedy match
#kebalikannya dari greedy match pada non greedy akan berhenti pencariannya di huruf atau tanda tepat dimana dia ditemukan walaupun huruf/tandanya ada banyak di kalimat selanjutnya.
y3 = re.findall('^F.+?:',x2)
print(y3)

#pencarian dengan kodisi berada ditengah
#akan mencari dengan awalan \S (white space) yang diantaranya ada tanda '@' dan diakhiri dengan \S lagi.
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)