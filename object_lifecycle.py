class PestaMeriah :
    x = 0
    nama = ""
    
    def __init__(self,z) -> None:
        self.nama = z
        print(self.nama,'Constructed')

    def pesta(self) :
        self.x = self.x +1
        print(self.nama,'Nomer Peserta',self.x)
    
s = PestaMeriah("Udin")
s.pesta()

j = PestaMeriah("Gambut")
j.pesta()
s.pesta()
