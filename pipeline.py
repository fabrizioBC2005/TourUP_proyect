import os
import csv
import time
import shutil
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

VAULT = Path(r"C:\Users\USER\Desktop\TourUP_proyect")
INBOX = VAULT / "inbox"
WIKI  = VAULT / "wiki"

def nombre_seguro(texto):
    import re
    texto = texto.strip()
    texto = re.sub(r'[<>:"/\\|?*]', '', texto)
    return re.sub(r'\s+', ' ', texto).strip()

def icono(valor):
    v = valor.strip().lower()
    if any(x in v for x in ['si', 'si —', 'acceso', 'habilitado', 'adaptado', 'rampas', 'carrito', 'circuito', 'rutas']):
        return 'Si'
    return 'No documentado'

def procesar_csv(path):
    print(f"[pipeline] Procesando CSV: {path.name}")
    with open(path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nombre  = nombre_seguro(row.get('Nombre', ''))
            region  = nombre_seguro(row.get('Region', row.get('Región', '')))
            if not nombre or not region:
                continue

            region_path = WIKI / region
            museo_path  = region_path / nombre
            museo_path.mkdir(parents=True, exist_ok=True)

            precio     = row.get('Precio general (S/)', '').strip() or 'No especificado'
            precio_d   = row.get('Precio personas con discapacidad', '').strip() or 'No especificado'
            desc       = row.get('Descripcion', row.get('Descripción', '')).strip()
            tipo       = row.get('Tipo', '').strip()
            admin      = row.get('Administracion', row.get('Administración', '')).strip()
            direccion  = row.get('Direccion', row.get('Dirección', '')).strip()
            disc       = row.get('Discapacidades atendidas', '').strip()
            notas      = row.get('Notas', '').strip()

            contenido = f"""---
type: museo
region: {region}
tipo: {tipo}
administracion: {admin}
direccion: "{direccion}"
precio_general: "{precio}"
precio_discapacidad: "{precio_d}"
discapacidades: "{disc}"
tags: [museo, {region.lower().replace(' ', '-')}, accesible]
parent: "{region}"
---

# {nombre}

> {desc}

## Informacion general

| Campo | Detalle |
|-------|---------|
| **Region** | [[{region}]] |
| **Tipo** | {tipo} |
| **Administracion** | {admin} |
| **Direccion** | {direccion} |

## Precios

| Publico | Precio |
|---------|--------|
| General | S/ {precio} |
| CONADIS | {precio_d} |

## Accesibilidad

| Servicio | Estado |
|----------|--------|
| Sillas / Carritos | {icono(row.get('Sillas de ruedas / Carritos electricos', ''))} |
| Braille | {icono(row.get('Cartillas Braille', ''))} |
| Lengua de Senas | {icono(row.get('Lengua de Senas Peruana', ''))} |
| Circuito inclusivo | {icono(row.get('Circuito inclusivo', ''))} |
| Banos accesibles | {icono(row.get('Banos accesibles', ''))} |

## Salas

![[Salas]]

## Notas
{notas if notas else 'Sin notas adicionales.'}
"""
            main_file = museo_path / f"{nombre}.md"
            with open(main_file, 'w', encoding='utf-8') as mf:
                mf.write(contenido)

            salas_file = museo_path / "Salas.md"
            if not salas_file.exists():
                with open(salas_file, 'w', encoding='utf-8') as sf:
                    sf.write(f"""# Salas - {nombre}

## Salas / Areas

| Sala | Descripcion | Accesible |
|------|-------------|-----------|
| Sala 1 | - | Si |

---
*Volver a [[{nombre}]]*
""")
            print(f"  [ok] {nombre} -> wiki/{region}/")

    shutil.move(str(path), str(VAULT / "sources" / path.name))
    print(f"[pipeline] CSV movido a sources/")
    actualizar_grafo()

def actualizar_grafo():
    print("[pipeline] Actualizando grafo...")
    env = os.environ.copy()
    subprocess.run(["graphify", "update", "./"], cwd=VAULT, env=env)
    subprocess.run(["git", "add", "."], cwd=VAULT)
    subprocess.run(["git", "commit", "-m", "pipeline: nuevos museos desde inbox"], cwd=VAULT)
    subprocess.run(["git", "push"], cwd=VAULT)
    print("[pipeline] Listo — grafo actualizado y commit hecho")

class InboxHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        time.sleep(1)
        if path.suffix.lower() == '.csv':
            procesar_csv(path)
        else:
            print(f"[pipeline] Archivo no soportado aun: {path.name}")

if __name__ == "__main__":
    print(f"[pipeline] Vigilando inbox/: {INBOX}")
    print("[pipeline] Suelta un CSV en inbox/ para procesar automaticamente")
    observer = Observer()
    observer.schedule(InboxHandler(), str(INBOX), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
