# Schema — Directorio Museos Accesibles Perú

## Estructura del vault
- **wiki/** → notas canónicas de museos por región (fuente principal)
- **sources/** → datos brutos (CSV originales, PDFs, artículos)
- **inbox/** → capturas rápidas y notas pendientes de procesar
- **schema/** → este archivo y plantillas para agentes

## Reglas para agentes
1. Antes de responder, ejecuta: graphify query "<pregunta>" --graph graphify-out/graph.json
2. Usa wiki/ como fuente principal de información
3. Si falta info, busca en sources/ pero NO la edites
4. Para agregar contenido nuevo, créalo en wiki/ con el frontmatter correcto
5. Las notas de inbox/ deben procesarse y moverse a wiki/ cuando estén listas

## Frontmatter obligatorio para museos
- región, tipo, administración, dirección, precio_general, precio_discapacidad
- discapacidades, tags: [museo, región, accesible]

## Comandos útiles
- graphify query "museos en Lima"
- graphify query "museos con lengua de señas"
- graphify update ./ (actualizar grafo sin rebuild completo)
