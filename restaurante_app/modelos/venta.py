from dataclasses import dataclass
from datetime import datetime


@dataclass
class Venta:
    id: int
    usuario_id: int
    producto_id: int
    fecha: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id", 0),
            usuario_id=data.get("usuario_id", 0),
            producto_id=data.get("producto_id", 0),
            fecha=data.get("fecha", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "producto_id": self.producto_id,
            "fecha": self.fecha,
        }
