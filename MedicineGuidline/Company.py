
class Beximco():
    medicine = ['napa', 'prevencid', 'domiren', 'fenadin','beclovan']

    def __init__(self,Nmedicine):
        self.Nmedicine=Nmedicine

    def companyname(self):
        for i in self.medicine:
            if i==self.Nmedicine:
               print(i,"Beximco")

            else:
                pass


class Aci():
    medicine = ['probitors', 'xcel', 'dompi', 'fexo','fenobac']
    def __init__(self,Nmedicine):
        self.Nmedicine=Nmedicine

    def companyname(self):
        for i in self.medicine:
            if i==self.Nmedicine:
               print(i, "Aci")
            else:
                pass


class Renata():
    medicine = ['procap', 'domsil', 'paradote', 'fexodin','flexibac']
    def __init__(self,Nmedicine):
        self.Nmedicine=Nmedicine

    def companyname(self):
        for i in self.medicine:
            if i==self.Nmedicine:
               print(i, "Renata")
            else:
                pass

class Skf():
    medicine = ['proceptin', 'domstal', 'fixal', 'pyralgin','lioresal']
    def __init__(self,Nmedicine):
        self.Nmedicine=Nmedicine

    def companyname(self):
        for i in self.medicine:
            if i==self.Nmedicine:
               print(i, "Skf")
            else:
                pass