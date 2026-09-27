import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
sys.path.insert(0, str(root))

from restaurante_app.servicios.restaurante_servicio import RestauranteServicio

base = root / "restaurante_app" / "datos"
servicio = RestauranteServicio(str(base))
usuario = servicio.validar_usuario('admin@restaurante.com', '1234')
print('usuario=', usuario.nombre if usuario else None)
print('productos=', len(servicio.obtener_productos()))
print('ventas_iniciales=', len(servicio.obtener_ventas()))
resultado = servicio.registrar_venta(1, 1)
print('resultado_ok=', resultado['ok'])
print('resultado_msg=', resultado['mensaje'])
print('ventas_finales=', len(servicio.obtener_ventas()))
ventas = json.loads((base / 'ventas.json').read_text(encoding='utf-8'))
print('ultima_venta=', ventas[-1])

# Keep a clean default state for the project repo.
(base / 'ventas.json').write_text('[]', encoding='utf-8')
