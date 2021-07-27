# normalnya memanggil modul seperti berikut :
#  import helper71 
# atau bisa disingkat dengan membuat alias
# import helper71 as hlp

# tapi jika hanya spesifik di fungsi tertentu maka menggunakan from
# untuk import semua yg ada di modul tujuan tambahkan "*"
# from helper71 import *

# kelebihan menggunakan sintax "from" ketimbang import biasa kita tidak perlu menuliskan nama modul setiap kali memanggilnya.
# tapi akan agak membingungkan jika memiliki banyak modul yang di import.
# akan mudah tracking fungsi dari modul mana yang akan dipanggil jika kita menuliskan nama modulnya setiap memanggil sesuatu di modul tersebut.

from helper71 import vali_ex, pesan_default

user_input = ""
while True:
    user_input = input(pesan_default)
    # secara default split akan memisahkan berdasarkan spasi
    list_hari = user_input.split(":")
    if user_input == "exit":
        break
    else:
        if len(list_hari) <= 1:
            print("format penulisan salah || Contoh = angka:unit_konversi")
        else:    
            hari_dict = {"days":list_hari[0],"unit":list_hari[1]}
            # jika import biasa maka didepannya harus dituliskan nama modulnya
            # helper71.vali_ex(hari_dict)

            # karena diatas dipanggil secara spesifik di fungsi tertentu maka tidak perlu dituliskan nama modulnya di depan
            vali_ex(hari_dict)

