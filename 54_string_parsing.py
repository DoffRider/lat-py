import re

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
posisi1 = data.find('@') #mencari posisi dimana simbol '@' berada
print(posisi1,'\n')

posisi2= data.find(' ',posisi1) #setelah koma artinya dimulai dari poin itu
print(posisi2,'\n')

nama_host = data[posisi1+1:posisi2] #ditambah satu untuk maju satu huruf
print(nama_host,'\n')


#double split patern
kata = data.split() #memecah perkata dan menjadikannya list
email = kata[1] #mengambil kata dari no indeks 1
pecah = email.split('@') #dipecah jika ada simbol '@'
print('Dipecah double Split')
print(pecah[1])
print('\n')

#regex (regular expression)
#cari simbol @ 
#simbol ^ artinya not
reg = re.findall('@([^ ]*)', data) #cari simbol @ dan juga Not a blank
print('Regex')
print(reg)
print('\n')

#atau yang lebih presisi
print('or more precision')
#carikan yang dimulai dari "From " tapi tidak include (hanya starting point saja)
#kemudian lanjut carikan yg ada simbol @ diakhiri dengan spasi (blank character)
reg2 = re.findall('^From .*@([^ ]*)',data)
print(reg2)
print('\n')

