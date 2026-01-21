import re

html_sucio = """
<div class="product" data-price="1500.50">Zapatillas</div>
<div class="product" data-price="999.00">Remera</div>
<span id="total">Total: 2499.50</span>
"""

patron = r"data-price=.(\d+\.\d+)."

res = re.findall(patron, html_sucio)
print(res)