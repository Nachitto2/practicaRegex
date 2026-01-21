import re

telemetria = "STATUS:OK | LOC:Lat=-34.6037,Lon=-58.3816 | ALT:50m"

patron = r"(-?\d+\.\d+).+?(-?\d{0,3}\.\d+)"

resultado =re.search(patron,telemetria)

print(resultado.group(1))
print(resultado.group(2))