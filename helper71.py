def konversi(angka_konversi,unit):

    if angka_konversi > 0 and unit == "j":
        return f"{angka_konversi} hari adalah {angka_konversi * 24} Jam"
    elif angka_konversi > 0 and unit == "m":
        return f"{angka_konversi} Jam adalah {angka_konversi * 60} Menit"
    else:
        return "Unit Konversi salah atau belum didukung"

def vali_ex(hari_dict):
    # agar bisa merubah blobal variable di inisialisasi dulu disini
    global user_input
    try:
        tampung_user_input = int(hari_dict["days"]) #menampung hasil list dari loop
        if tampung_user_input > 0:
            hit_value = konversi(tampung_user_input,hari_dict["unit"])
            print(hit_value)
        elif tampung_user_input == 0:
            print("Masukkan selain angka 0")
        else:
            print("Masukkan angka positif")
    except IndexError:
        print("Input anda tidak valid")
        user_input = "exit"

pesan_default = ("Masukkan Hari dan Unit Konversi = ")