import os
from datetime import datetime

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta
from restaurante_app.servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self, base_dir: str):
        self.archivo_servicio = ArchivoServicio(base_dir)

    def validar_usuario(self, correo: str, contrasena: str):
        usuarios = self.obtener_usuarios()
        for usuario in usuarios:
            if usuario.correo == correo and usuario.contrasena == contrasena:
                return usuario
        return None

    def obtener_usuarios(self):
        datos = self.archivo_servicio.leer_json("usuarios.json")
        return [Usuario.from_dict(item) for item in datos]

    def obtener_productos(self):
        datos = self.archivo_servicio.leer_json("productos.json")
        return [Producto.from_dict(item) for item in datos]

    def obtener_ventas(self):
        datos = self.archivo_servicio.leer_json("ventas.json")
        return [Venta.from_dict(item) for item in datos]

    def registrar_venta(self, usuario_id: int, producto_id: int):
        usuarios = self.obtener_usuarios()
        productos = self.obtener_productos()

        usuario = next((u for u in usuarios if u.id == usuario_id), None)
        producto = next((p for p in productos if p.id == producto_id), None)

        if usuario is None:
            return {"ok": False, "mensaje": "Debe seleccionar un usuario registrado."}
        if producto is None:
            return {"ok": False, "mensaje": "Debe seleccionar un producto registrado."}

        ventas = self.obtener_ventas()
        nueva_venta = Venta(
            id=len(ventas) + 1,
            usuario_id=usuario.id,
            producto_id=producto.id,
            fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        ventas.append(nueva_venta)
        self.archivo_servicio.guardar_json("ventas.json", [venta.to_dict() for venta in ventas])

        return {
            "ok": True,
            "mensaje": f"Venta registrada correctamente para {usuario.nombre} - {producto.nombre}.",
            "venta": nueva_venta,
        }

    def registrar_usuario(self, usuario: Usuario):
        usuarios = self.obtener_usuarios()
        usuarios.append(usuario)
        self.archivo_servicio.guardar_json("usuarios.json", [u.to_dict() for u in usuarios])
        return True

    def registrar_producto(self, producto: Producto):
        productos = self.obtener_productos()
        productos.append(producto)
        self.archivo_servicio.guardar_json("productos.json", [p.to_dict() for p in productos])
        return True
