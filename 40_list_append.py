#menyatakan variabel sebagai list 
listnomer = list()
while True :
    inputan = input('Masukkan Angka : ')
    if inputan == 'done' : break
    #dirubah dulu ke float karena awalnya string
    val = float(inputan)

    #setelah itu masukkan angka tersebut ke dalam list
    listnomer.append(val)

rata2 = sum(listnomer) / len(listnomer)
print('Rata-ratanya adalah : ',rata2)