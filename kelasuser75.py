# nama kelas gunakan huruf besar di awal
class User:
    # fungsi init akan dijalankan setiap kali object dibuat
    # self merujuk pada intance(perwujudan) dari kelas sekarang
    # singkatnya merujuk ke diri sendiri pada kelas yang sedang dijalankan/aktif
    def __init__(self, par_email,par_nama,par_pass,par_gawe) -> None:
        # atribut
        # untuk menandakan atribut ini milik kelas ini maka ditambahkan self
        self.email = par_email
        self.nama = par_nama
        self.password = par_pass
        self.gawe = par_gawe

    # ditambahkan self pada fungsi untuk mengakses apa yang ada di dalam kelas ini
    # jika tidak ditambah self kita tidak bisa mengakses atribut/value yg ada di kelas
    def ganti_pass(self, par_pass_baru):
        self.password = par_pass_baru

    def ganti_gawe(self, par_gawe_baru):
        self.gawe = par_gawe_baru

    def get_user_info(self):
        print(f"User {self.nama} sekarang menjabat sebagai {self.gawe}. alamat email {self.email}")