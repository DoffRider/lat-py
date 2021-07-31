class Post:
    def __init__(self,par_pesan,par_penulis) -> None:
        self.pesan = par_pesan
        self.penulis = par_penulis

    def get_post_info(self):
        print(f"Post: {self.pesan} ditulis oleh {self.penulis}")