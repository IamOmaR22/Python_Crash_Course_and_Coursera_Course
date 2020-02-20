from MedicineGuidline2.MedicineOperation import *
from MedicineGuidline2.Company import *
medicine=input("Enter your medicine name :")
medicine=medicine.lower()

obj=paracetamol(medicine)
pera=obj.paracet()
# print(pera)
try:
    for i in pera:
        com1=Beximco(i)
        com1.companyname()
        com2=Aci(i)
        com2.companyname()
        com3=Renata(i)
        com3.companyname()
        com4=Skf(i)
        com4.companyname()
except:
    pass


obj=omeprazole(medicine)
omep=obj.omepraz()
try:
    for i in omep:
        com1=Beximco(i)
        com1.companyname()
        com2=Aci(i)
        com2.companyname()
        com3=Renata(i)
        com3.companyname()
        com4=Skf(i)
        com4.companyname()
except:
    pass


obj=domperidone(medicine)
domp=obj.domperi()
try:
    for i in domp:
        com1=Beximco(i)
        com1.companyname()
        com2=Aci(i)
        com2.companyname()
        com3=Renata(i)
        com3.companyname()
        com4=Skf(i)
        com4.companyname()
except:
    pass

obj=fexofenadine(medicine)
fex=obj.fexofen()
try:
    for i in fex:
        com1=Beximco(i)
        com1.companyname()
        com2=Aci(i)
        com2.companyname()
        com3=Renata(i)
        com3.companyname()
        com4=Skf(i)
        com4.companyname()
except:
    pass


obj=baclofen(medicine)
bac=obj.baclof()
try:
    for i in bac:
        com1=Beximco(i)
        com1.companyname()
        com2=Aci(i)
        com2.companyname()
        com3=Renata(i)
        com3.companyname()
        com4=Skf(i)
        com4.companyname()
except:
    pass
