# import kelasuser75
# atau
from kelasuser75 import User
from cetak75 import Post


pengguna1 = User("Uwawa@wauw.com","Udin","pwd123","kang baso")

pengguna1.get_user_info()
pengguna1.ganti_gawe("kang nasgor")
pengguna1.get_user_info()
print("\n")

Post("lagi gawe apa?", pengguna1.nama).get_post_info()