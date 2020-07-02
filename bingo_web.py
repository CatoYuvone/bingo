from jinja2 import Template
from src.bingo import intentoCartonRePro

mi_carton = intentoCartonRePro()

template = Template(open('src/plantilla.j2').read())

print(template.render(carton = mi_carton))