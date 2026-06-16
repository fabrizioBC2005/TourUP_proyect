# Graph Report - C:\Users\USER\Desktop\TourUP_proyect  (2026-06-15)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 35 nodes · 38 edges · 13 communities (6 shown, 7 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]

## God Nodes (most connected - your core abstractions)
1. `Lima` - 8 edges
2. `Peru` - 6 edges
3. `TourUP_proyect` - 6 edges
4. `La Libertad` - 4 edges
5. `Lambayeque` - 4 edges
6. `Ayacucho` - 3 edges
7. `Ica` - 3 edges
8. `Lima Barranca` - 3 edges
9. `Museo de Sitio de Quinua` - 2 edges
10. `Museo de Sitio Julio C. Tello – Paracas` - 2 edges

## Surprising Connections (you probably didn't know these)
- `TourUP_proyect` --references--> `La Libertad`  [EXTRACTED]
  TourUP_proyect.md → wiki/La Libertad/00 - La Libertad.md
- `TourUP_proyect` --references--> `Lambayeque`  [EXTRACTED]
  TourUP_proyect.md → wiki/Lambayeque/00 - Lambayeque.md
- `TourUP_proyect` --references--> `Lima`  [EXTRACTED]
  TourUP_proyect.md → wiki/Lima/00 - Lima.md
- `TourUP_proyect` --references--> `Lima Barranca`  [EXTRACTED]
  TourUP_proyect.md → wiki/Lima Barranca/00 - Lima Barranca.md
- `TourUP_proyect` --references--> `Ayacucho`  [EXTRACTED]
  TourUP_proyect.md → wiki/Ayacucho/00 - Ayacucho.md

## Import Cycles
- None detected.

## Communities (13 total, 7 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.40
Nodes (5): Complejo Arqueológico Chan Chan – Museo de Sitio, Salas — Complejo Arqueológico Chan Chan – Museo de Sitio, Huacas de Moche – Museo de Sitio Huaca de la Luna, Salas — Huacas de Moche – Museo de Sitio Huaca de la Luna, La Libertad

### Community 1 - "Community 1"
Cohesion: 0.40
Nodes (5): Lambayeque, Museo de Sitio Huaca Rajada – Sipán, Salas — Museo de Sitio Huaca Rajada – Sipán, Museo Tumbas Reales de Sipán, Salas — Museo Tumbas Reales de Sipán

### Community 2 - "Community 2"
Cohesion: 0.67
Nodes (4): Ayacucho, Ica, Peru, TourUP_proyect

### Community 3 - "Community 3"
Cohesion: 0.67
Nodes (3): Ciudad Sagrada de Caral, Salas — Ciudad Sagrada de Caral, Lima Barranca

### Community 4 - "Community 4"
Cohesion: 0.67
Nodes (3): Complejo Arqueológico Mateo Salado, Salas — Complejo Arqueológico Mateo Salado, Lima

## Knowledge Gaps
- **13 isolated node(s):** `Salas — Museo de Sitio de Quinua`, `Salas — Museo de Sitio Julio C. Tello – Paracas`, `Salas — Complejo Arqueológico Chan Chan – Museo de Sitio`, `Salas — Huacas de Moche – Museo de Sitio Huaca de la Luna`, `Salas — Museo de Sitio Huaca Rajada – Sipán` (+8 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lima` connect `Community 4` to `Community 2`, `Community 5`, `Community 8`, `Community 9`, `Community 10`, `Community 11`?**
  _High betweenness centrality (0.556) - this node is a cross-community bridge._
- **Why does `Peru` connect `Community 2` to `Community 0`, `Community 1`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.347) - this node is a cross-community bridge._
- **Why does `TourUP_proyect` connect `Community 2` to `Community 0`, `Community 1`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.347) - this node is a cross-community bridge._
- **What connects `Salas — Museo de Sitio de Quinua`, `Salas — Museo de Sitio Julio C. Tello – Paracas`, `Salas — Complejo Arqueológico Chan Chan – Museo de Sitio` to the rest of the system?**
  _13 weakly-connected nodes found - possible documentation gaps or missing edges._