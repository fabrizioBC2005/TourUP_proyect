import os, csv, time, shutil, subprocess, re
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

VAULT = Path(r"C:\Users\USER\Desktop\TourUP_proyect")
INBOX = VAULT / "inbox"
WIKI  = VAULT / "wiki"

def safe(text):
    text = text.strip()
    text = re.sub(r'[<>:"/\\|?*]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def procesar_museos(path):
    print(f"[pipeline] Procesando museos: {path.name}")
    with open(path, 'r', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            nombre = safe(row.get('Nombre', ''))
            region = safe(row.get('Region', row.get('Región', '')))
            if not nombre or not region: continue
            p = WIKI / region / nombre
            p.mkdir(parents=True, exist_ok=True)
            md = f"""---
type: museo
parent: "{region}"
region: {region}
ciudad: {region}
tipo: {row.get('Tipo','').strip()}
administracion: {row.get('Administración', row.get('Administracion','')).strip()}
direccion: "{row.get('Dirección', row.get('Direccion','')).strip()}"
precio_general: "{row.get('Precio general (S/)','').strip()}"
precio_discapacidad: "{row.get('Precio personas con discapacidad','').strip()}"
discapacidades: "{row.get('Discapacidades atendidas','').strip()}"
categoria_centro_cultural: museo
tags: [museo, {region.lower().replace(' ','-')}, accesible, nivel-3]
---

# {nombre}

> {row.get('Descripción', row.get('Descripcion','')).strip()}

## Informacion general
| Campo | Detalle |
|-------|---------|
| **Pais** | [[Peru]] |
| **Ciudad** | [[{region}]] |
| **Tipo** | {row.get('Tipo','').strip()} |

## Salas
![[Salas]]

## Actividades
![[Actividades]]
"""
            (p / f"{nombre}.md").write_text(md, encoding='utf-8')
            if not (p / "Salas.md").exists():
                (p / "Salas.md").write_text(f"""---
type: sala
parent: "{nombre}"
museo: "{nombre}"
ciudad: "{region}"
tipo_sala: permanente
accesible: true
tags: [sala, nivel-4]
---

# Salas — {nombre}

| Sala | Tipo | Accesible |
|------|------|-----------|
| Sala 1 | permanente | Si |

*← [[{nombre}]]*
""", encoding='utf-8')
            if not (p / "Actividades.md").exists():
                (p / "Actividades.md").write_text(f"""---
type: actividad
parent: "{nombre}"
museo: "{nombre}"
ciudad: "{region}"
tags: [actividad, nivel-5]
---

# Actividades — {nombre}

| Actividad | Sala | Categoria | Fecha | Cupos |
|-----------|------|-----------|-------|-------|
| Visita guiada | Sala 1 | visita_guiada | — | — |

*← [[{nombre}]]*
""", encoding='utf-8')
            print(f"  [ok] {nombre} -> wiki/{region}/")
    shutil.move(str(path), str(VAULT / "sources" / path.name))

def procesar_salas(path):
    print(f"[pipeline] Procesando salas: {path.name}")
    with open(path, 'r', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            museo  = safe(row.get('Museo', ''))
            ciudad = safe(row.get('Ciudad', ''))
            sala   = safe(row.get('Sala', ''))
            if not museo or not sala: continue
            p = WIKI / ciudad / museo
            p.mkdir(parents=True, exist_ok=True)
            (p / f"{sala}.md").write_text(f"""---
type: sala
parent: "{museo}"
museo: "{museo}"
ciudad: "{ciudad}"
tipo_sala: {row.get('Tipo','permanente').strip()}
accesible: {row.get('Accesible','true').strip()}
capacidad: "{row.get('Capacidad','').strip()}"
categoria_sala: {row.get('Tipo','permanente').strip()}
tags: [sala, {ciudad.lower().replace(' ','-')}, nivel-4]
---

# {sala}

| Campo | Detalle |
|-------|---------|
| **Museo** | [[{museo}]] |
| **Ciudad** | [[{ciudad}]] |
| **Tipo** | {row.get('Tipo','').strip()} |
| **Accesible** | {row.get('Accesible','').strip()} |
| **Capacidad** | {row.get('Capacidad','').strip()} |

*← [[{museo}]]*
""", encoding='utf-8')
            print(f"  [ok] {sala} -> wiki/{ciudad}/{museo}/")
    shutil.move(str(path), str(VAULT / "sources" / path.name))

def procesar_actividades(path):
    print(f"[pipeline] Procesando actividades: {path.name}")
    with open(path, 'r', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            museo     = safe(row.get('Museo', ''))
            ciudad    = safe(row.get('Ciudad', ''))
            sala      = safe(row.get('Sala', ''))
            actividad = safe(row.get('Actividad', ''))
            if not museo or not actividad: continue
            p = WIKI / ciudad / museo
            p.mkdir(parents=True, exist_ok=True)
            (p / f"Actividad — {actividad}.md").write_text(f"""---
type: actividad
parent: "{sala if sala else museo}"
museo: "{museo}"
ciudad: "{ciudad}"
sala: "{sala}"
actividad: "{actividad}"
categoria_actividad: {row.get('Categoria','visita_guiada').strip()}
discapacidades_atendidas: "{row.get('Discapacidades','').strip()}"
fecha_inicio: "{row.get('Fecha inicio','').strip()}"
fecha_fin: "{row.get('Fecha fin','').strip()}"
cupos: "{row.get('Cupos','').strip()}"
tags: [actividad, {ciudad.lower().replace(' ','-')}, {row.get('Categoria','visita_guiada').strip()}, nivel-5]
---

# {actividad}

| Campo | Detalle |
|-------|---------|
| **Museo** | [[{museo}]] |
| **Sala** | {sala} |
| **Categoria** | {row.get('Categoria','').strip()} |
| **Fecha inicio** | {row.get('Fecha inicio','').strip()} |
| **Fecha fin** | {row.get('Fecha fin','').strip()} |
| **Cupos** | {row.get('Cupos','').strip()} |

## Fechas programadas
![[Fechas]]

*← [[{sala if sala else museo}]]*
""", encoding='utf-8')
            print(f"  [ok] {actividad} -> wiki/{ciudad}/{museo}/")
    shutil.move(str(path), str(VAULT / "sources" / path.name))

def procesar_fechas(path):
    print(f"[pipeline] Procesando fechas: {path.name}")
    with open(path, 'r', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            museo     = safe(row.get('Museo', ''))
            ciudad    = safe(row.get('Ciudad', ''))
            actividad = safe(row.get('Actividad', ''))
            fecha     = safe(row.get('Fecha', ''))
            if not museo or not fecha: continue
            p = WIKI / ciudad / museo
            p.mkdir(parents=True, exist_ok=True)
            nombre_archivo = f"Fecha — {fecha} — {actividad}"
            (p / f"{nombre_archivo}.md").write_text(f"""---
type: fecha
parent: "{actividad if actividad else museo}"
actividad: "{actividad}"
museo: "{museo}"
ciudad: "{ciudad}"
sala: "{safe(row.get('Sala',''))}"
fecha: "{fecha}"
hora_inicio: "{row.get('Hora inicio','').strip()}"
hora_fin: "{row.get('Hora fin','').strip()}"
cupos_disponibles: "{row.get('Cupos disponibles','').strip()}"
cupos_total: "{row.get('Cupos total','').strip()}"
estado: "{row.get('Estado','programado').strip()}"
temporada: "{row.get('Temporada','').strip()}"
tags: [fecha, {ciudad.lower().replace(' ','-')}, {row.get('Estado','programado').strip()}, nivel-6]
---

# {fecha} — {actividad}

| Campo | Detalle |
|-------|---------|
| **Museo** | [[{museo}]] |
| **Ciudad** | [[{ciudad}]] |
| **Actividad** | [[Actividad — {actividad}]] |
| **Sala** | {safe(row.get('Sala',''))} |
| **Fecha** | {fecha} |
| **Hora** | {row.get('Hora inicio','').strip()} - {row.get('Hora fin','').strip()} |
| **Cupos disponibles** | {row.get('Cupos disponibles','').strip()} / {row.get('Cupos total','').strip()} |
| **Estado** | {row.get('Estado','programado').strip()} |
| **Temporada** | {row.get('Temporada','').strip()} |

*← [[Actividad — {actividad}]]*
""", encoding='utf-8')
            print(f"  [ok] {fecha} {actividad} -> wiki/{ciudad}/{museo}/")
    shutil.move(str(path), str(VAULT / "sources" / path.name))

def actualizar_grafo():
    print("[pipeline] Actualizando grafo...")
    subprocess.run(["graphify", "update", "./"], cwd=VAULT)
    subprocess.run(["git", "add", "."], cwd=VAULT)
    subprocess.run(["git", "commit", "-m", "pipeline: nuevos datos desde inbox"], cwd=VAULT)
    subprocess.run(["git", "push"], cwd=VAULT)
    print("[pipeline] Listo")

class InboxHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory: return
        path = Path(event.src_path)
        time.sleep(1)
        if path.suffix.lower() != '.csv': return
        name = path.name.lower()
        if 'fecha' in name:       procesar_fechas(path)
        elif 'sala' in name:      procesar_salas(path)
        elif 'actividad' in name: procesar_actividades(path)
        else:                     procesar_museos(path)
        actualizar_grafo()

if __name__ == "__main__":
    print(f"[pipeline] Vigilando inbox/: {INBOX}")
    print("[pipeline] Tipos soportados:")
    print("  - museos_*.csv      -> Nivel 3")
    print("  - salas_*.csv       -> Nivel 4")
    print("  - actividades_*.csv -> Nivel 5")
    print("  - fechas_*.csv      -> Nivel 6")
    observer = Observer()
    observer.schedule(InboxHandler(), str(INBOX), recursive=False)
    observer.start()
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
