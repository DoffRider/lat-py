import datetime as t
import time
from datetime import timedelta

usrp = input("Masukkan Waktu Tujuan : \n")
usrp_list = usrp.split(":")

tujuan = usrp_list[0]
deadline = usrp_list[1]

# convert dari string ke format waktu
waktu_input = t.datetime.strptime(deadline, "%d.%m.%Y")
sekarang = t.datetime.now().replace(microsecond=0)

# menghitung hingga deadline
hit = waktu_input - sekarang
h = float(hit.seconds/3600)

print(f"sisa waktu tersisa untuk {tujuan} adalah {hit}")
print(f"sisa waktu tersisa untuk {tujuan} adalah {hit.days} hari {int(hit.seconds/3600)} Jam {hit.seconds/60} ")
print("")
print(f"sisa waktu tersisa untuk {tujuan} adalah {hit.days} hari {str(timedelta(hours=h))} jam")


# belajar piton:30.07.2021