import re

texto = "<h1>Oferta Laboral</h1> <br> <p>Se busca Junior</p>"

etiquetas = "<[^>]+>" 

resultado = re.sub(etiquetas,"",texto)
print(resultado.strip())