from dataclasses import dataclass


@dataclass
class Producto:
    id: int
    nombre: str
    categoria: str
    precio: float

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id", 0),
            nombre=data.get("nombre", ""),
            categoria=data.get("categoria", ""),
            precio=float(data.get("precio", 0.0)),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }
