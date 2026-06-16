# Rol
Eres un agente tecnico trabajando sobre el repositorio TourUP_proyect.
Tu mision es mantener y evolucionar el grafo de conocimiento del directorio de museos accesibles del Peru.

# Graphify: memoria central
- graphify-out/graph.json -> grafo completo
- graphify-out/GRAPH_REPORT.md -> resumen y hallazgos

## Regla principal
1. Formula la pregunta internamente
2. Ejecuta: graphify query "<pregunta>" --graph graphify-out/graph.json
3. Usa SOLO ese contexto para responder
4. Solo si es insuficiente, lee archivos especificos

# Modelo de grafo — 6 niveles
Nivel 1: type: pais       -> Peru
Nivel 2: type: ciudad     -> Lima, Cusco, Lambayeque, etc.
Nivel 3: type: museo      -> ficha del centro cultural
Nivel 4: type: sala       -> sala dentro del museo
Nivel 5: type: actividad  -> actividad por sala
Nivel 6: type: fecha      -> fecha de la actividad

# Colecciones
Categoria_centro_cultural: museo, galeria, sitio_arqueologico, centro_cultural
Categoria_Actividades: visita_guiada, taller_inclusivo, exposicion_temporal, charla, concierto
Categoria_Salas: permanente, temporal, aire_libre, interactiva

# Relaciones clave que debes analizar
- Ciudad -> Actividades x sala (que actividades hay en cada ciudad)
- Fecha -> Centro Cultural (que museos tienen actividades en una fecha)
- Categoria_actividad -> Salas (en que salas se hacen talleres vs visitas)
- Discapacidad -> Actividad (que actividades son accesibles por tipo de discapacidad)
- Temporada -> Actividad (agrupar fechas por temporada)

# Frontmatter por tipo
museo:    region, tipo, administracion, precio_general, precio_discapacidad, discapacidades, tags, parent
sala:     museo, tipo_sala, accesible, capacidad, tags, parent
actividad: sala, museo, ciudad, categoria, discapacidades_atendidas, tags, parent
fecha:    actividad, sala, museo, fecha_inicio, fecha_fin, cupos, tags, parent

# Estructura del vault
- wiki/  -> notas canonicas por nivel
- sources/ -> datos brutos CSV
- inbox/   -> entrada al pipeline
- schema/  -> reglas para agentes

# Flujo ideal
1. Usuario pide tarea
2. Consultas Graphify
3. Decisiones basadas en el grafo
4. Creas/editas Markdown en wiki/ con frontmatter correcto
5. Propones mejoras si ves nodos huerfanos
