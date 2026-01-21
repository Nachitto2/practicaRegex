import re

texto ="¡Increíble el partido de hoy! #futbol #Mundial2026. No se pierdan el resumen en #ESPN."
patron = "#\\w+"

print(re.findall(patron,texto))