str = 'X-DSPAM-Confidence: 0.8475 '
posisi1 = str.find(':')

print(posisi1)
pecah = str[posisi1+1:]
value = float(pecah)
print(pecah)

print(value)
