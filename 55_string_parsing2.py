import re

#spam confidence

hand = open('mbox-short.txt')
numlist = list()

for i in hand:
    i = i.rstrip()
    #perhatikan ada titik berarti mencari nilai 0.0 bukan desimal
    isi = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',i) #jika tdk ada akan menjadi list kosong
    if len(isi) != 1 : continue #jika tidak ada isinya lanjutkan
    num = float(isi[0])
    numlist.append(num)
print('Maximum: ',max(numlist))
print('\n')

#escape character
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)