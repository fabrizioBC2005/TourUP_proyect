with open('graphify-out/graph.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

reemplazos = {
    'Community 33': 'Regiones',
    'Community 32': 'Edges',
    'Community 31': 'Nodos',
    'Community 30': 'Grafo',
    'Community 29': 'Sources',
    'Community 28': 'Inbox',
    'Community 27': 'Vault',
    'Community 26': 'Indice',
    'Community 25': 'Wiki',
    'Community 24': 'Obsidian',
    'Community 23': 'Schema',
    'Community 22': 'Quinua',
    'Community 21': 'Huacas Moche',
    'Community 20': 'Sipan',
    'Community 19': 'Chan Chan',
    'Community 18': 'Caral',
    'Community 17': 'Lima Barranca',
    'Community 16': 'Salas',
    'Community 15': 'Fechas',
    'Community 14': 'Actividades',
    'Community 13': 'Scripts',
    'Community 12': 'Pipeline',
    'Community 11': 'Arqueologia',
    'Community 10': 'Cultura Peruana',
    'Community 9': 'Peru Central',
    'Community 8': 'Lima Sur',
    'Community 7': 'Ayacucho',
    'Community 6': 'Ica Paracas',
    'Community 5': 'Arte y Cultura',
    'Community 4': 'Lima Norte',
    'Community 3': 'Pachacamac',
    'Community 2': 'Lambayeque',
    'Community 1': 'Lima Central',
    'Community 0': 'La Libertad',
}

for viejo, nuevo in reemplazos.items():
    html = html.replace(viejo, nuevo)

with open('graphify-out/graph.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Listo')
