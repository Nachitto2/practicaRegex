import re

texto ="https://www.amazon.com/dp/B08N5K2Z12/ref=sr_1_1"

patron = r"/dp/([A-Z0-9]+)/"

resultado =re.search(patron,texto)

print(resultado.group(1))
