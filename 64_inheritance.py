class PestaMeriah :
    x = 0
    nama = ""
    
    def __init__(self,z) -> None:
        self.nama = z
        print(self.nama,'Constructed')

    def pesta(self) :
        self.x = self.x +1
        print(self.nama,'Nomer Peserta',self.x)
    
class SepagBola(PestaMeriah):
    poin = 0

    def masuk(self):
        self.poin = self.poin + 7
        self.pesta()
        print(self.nama," poin ", self.poin)


s = PestaMeriah("Udin")
s.pesta()
print("\n")

j = SepagBola("Gambut")
j.pesta()
j.masuk()
