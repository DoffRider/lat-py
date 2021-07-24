hit_unit = 24
nama_unit = "Jam"

def konversi(angka_konversi):
    if angka_konversi > 0:
        return f"{angka_konversi} hari adalah {angka_konversi * hit_unit} {nama_unit}"

def vali_ex():
    # agar bisa merubah blobal variable di inisialisasi dulu disini
    global user_input
    try:
        tampung_user_input = int(element_list) #menampung hasil list dari loop
        if tampung_user_input > 0:
            hit_value = konversi(tampung_user_input)
            print(hit_value)
        elif tampung_user_input == 0:
            print("Masukkan selain angka 0")
        else:
            print("Masukkan angka positif")

    except ValueError:
        print("Input anda tidak valid")
        user_input = "exit"


user_input = ""
while user_input != "exit":
    user_input = input("Masukkan Hari dan Unit Konversi = ")
    list_hari = user_input.split(", ")
    for element_list in set(list_hari):
        vali_ex()
