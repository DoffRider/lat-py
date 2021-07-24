def konversi(angka_konversi):
    tampung_user_unit = hari_dict["unit"]

    if angka_konversi > 0 and tampung_user_unit == "j":
        return f"{angka_konversi} hari adalah {angka_konversi * 24} Jam"
    elif angka_konversi > 0 and tampung_user_unit == "m":
        return f"{angka_konversi} Jam adalah {angka_konversi * 60} Menit"
    else:
        return "Unit Konversi salah atau belum didukung"

def vali_ex():
    # agar bisa merubah blobal variable di inisialisasi dulu disini
    global user_input
    try:
        tampung_user_input = int(hari_dict["days"]) #menampung hasil list dari loop
        if tampung_user_input > 0:
            hit_value = konversi(tampung_user_input)
            print(hit_value)
        elif tampung_user_input == 0:
            print("Masukkan selain angka 0")
        else:
            print("Masukkan angka positif")
    except IndexError:
        print("Input anda tidak valid")
        user_input = "exit"


user_input = ""
while True:
    user_input = input("Masukkan Hari dan Unit Konversi = ")
    # secara default split akan memisahkan berdasarkan spasi
    list_hari = user_input.split(":")
    # print(len(list_hari))
    if user_input == "exit":
        break
    else:
        if len(list_hari) <= 1:
            print("format penulisan salah || Contoh = angka:unit_konversi")
            # print(len(list_hari))
            # break
        else:    
            hari_dict = {"days":list_hari[0],"unit":list_hari[1]}
            vali_ex()
            # print(len(list_hari))

