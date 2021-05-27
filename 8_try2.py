temp = "5 degrees"
temp2 = 5
cel = 0
try:
    fahr = float(temp)
except:
    print('bukan angka')
    quit()

cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)