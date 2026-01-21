import re

log_transacciones = """
Pago procesado tarjeta: 4500-1234-5678-9010. Estado: OK.
Error en tarjeta: 1234 5678 1234 5678. Saldo insuficiente.
"""

patron = "\d{4}[ -]\d{4}[ -]\d{4}[ -]\d{4}"

reemplazo = "XXXX-XXXX-XXXX-XXXX"

censura = re.sub(patron,reemplazo,log_transacciones)

print(censura)