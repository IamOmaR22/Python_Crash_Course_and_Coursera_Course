
from medicine_operation import *

medicine = input("Enter your medicine name :")
medicine = medicine.lower()

obj = paracetamol(medicine)
obj.paracet()

obj = omeprazole(medicine)
obj.omepraz()

obj = domperidone(medicine)
obj.domperi()

obj = fexofenadine(medicine)
obj.fexofen()

obj = baclofen(medicine)
obj.baclof()