from dataclasses import dataclass


@dataclass
class Usuario:
    id: int
    nombre: str
    correo: str
    contrasena: str
    rol: str = "cliente"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id", 0),
            nombre=data.get("nombre", ""),
            correo=data.get("correo", ""),
            contrasena=data.get("contrasena", ""),
            rol=data.get("rol", "cliente"),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "contrasena": self.contrasena,
            "rol": self.rol,
        }
