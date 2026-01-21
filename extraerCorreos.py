import re

texto_ventas = """
Hola, mi correo es juan.perez@gmail.com, necesito info.
Yo también quiero, escriban a maria_123@hotmail.com o a ventas@empresa.org.
No me escriban a soporte@falso, ese no anda.
"""

patron = "\w+@[a-zA-Z]+\.[a-zA-Z]+"

resultado = re.findall(patron,texto_ventas)
print(resultado)