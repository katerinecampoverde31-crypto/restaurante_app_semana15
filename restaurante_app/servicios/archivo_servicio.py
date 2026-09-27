import json
from pathlib import Path


class ArchivoServicio:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)

    def _ruta(self, nombre_archivo: str) -> Path:
        archivo = self.base_dir / nombre_archivo
        archivo.parent.mkdir(parents=True, exist_ok=True)
        if not archivo.exists():
            archivo.write("[]", encoding="utf-8")
        return archivo

    def leer_json(self, nombre_archivo: str):
        with self._ruta(nombre_archivo).open("r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []

    def guardar_json(self, nombre_archivo: str, datos):
        with self._ruta(nombre_archivo).open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
