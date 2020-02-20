class paracetamol():
    medicine = ['napa', 'xcel', 'paradote', 'pyralgin']
    def __init__(self,Nmedicine):
        self.Nmedicine=Nmedicine

    def paracet(self):

        for i in self.medicine:
            if i==self.Nmedicine:
                print(self.medicine)
            else:
                pass


class omeprazole():

    def __init__(self,Nmedicine):
        self.Nmedicine=Nmedicine

    def omepraz(self):
        medicine=['prevencid', 'probitors', 'procap', 'proceptin']
        for i in medicine:
            if i == self.Nmedicine:
                print(medicine)
            else:
                pass

class domperidone():

    def __init__(self,Nmedicine):
        self.Nmedicine=Nmedicine

    def domperi(self):
        medicine=['domiren', 'dompi', 'domsil', 'domstal']
        for i in medicine:
            if i == self.Nmedicine:
                print(medicine)
            else:
                pass

class fexofenadine():

    def __init__(self,Nmedicine):
        self.Nmedicine=Nmedicine

    def fexofen(self):
        medicine=['fenadin', 'fexo', 'fexodin', 'fixal']
        for i in medicine:
            if i == self.Nmedicine:
                print(medicine)
            else:
                pass

class baclofen():

    def __init__(self,Nmedicine):
        self.Nmedicine=Nmedicine

    def baclof(self):
        medicine=['beclovan', 'fenobac', 'flexibac', 'lioresal']
        for i in medicine:
            if i == self.Nmedicine:
                print(medicine)
            else:
                pass
