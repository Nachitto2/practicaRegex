import re

texto1 ="El precio es 1500.00"
texto2 ="El precio es 1500"
texto3 ="El precio es 1500.9"

patron = "\d+.\d{2}"

resultado1 = re.search(patron,texto1)
resultado2= re.search(patron,texto2)
resultado3= re.search(patron,texto3)

print(resultado1.string)
print(resultado2)
print(resultado3)