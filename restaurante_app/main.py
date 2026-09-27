import sys
import tkinter as tk
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
    from restaurante_app.ui.login_view import LoginView
except ImportError:
    from servicios.restaurante_servicio import RestauranteServicio
    from ui.login_view import LoginView


def main():
    root = tk.Tk()
    root.title("Restaurante App")
    root.geometry("1000x650")
    root.configure(bg="#eef2f7")

    base_dir = str(Path(__file__).resolve().parent / "datos")
    servicio = RestauranteServicio(base_dir)

    LoginView(root, servicio)
    root.mainloop()


if __name__ == "__main__":
    main()
