from jinja2 import Template
from src.bingo import intentoCartonRePro

mi_carton = intentoCartonRePro()

template = Template(open('src/plantilla.j2').read())

file = open("bingo.html", "w")
file.write(template.render(carton = mi_carton))
file.close()
print("Generóse \"bingo.html\".")