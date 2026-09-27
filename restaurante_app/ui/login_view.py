import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from restaurante_app.servicios.restaurante_servicio import RestauranteServicio


class LoginView:
    def __init__(self, root, servicio: RestauranteServicio):
        self.root = root
        self.servicio = servicio
        self.frame = tk.Frame(root, bg="#f4f4f4")
        self.frame.pack(fill="both", expand=True)

        self._crear_ui()

    def _crear_ui(self):
        assets_dir = Path(__file__).resolve().parents[1] / "assets"
        logo_path = assets_dir / "logo.ppm"
        if logo_path.exists():
            logo = tk.PhotoImage(file=str(logo_path))
            logo_label = tk.Label(self.frame, image=logo, bg="#f4f4f4")
            logo_label.image = logo
            logo_label.pack(pady=(20, 5))

        title = tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 22, "bold"),
            bg="#f4f4f4",
            fg="#2c3e50",
        )
        title.pack(pady=(0, 10))

        info = tk.Label(
            self.frame,
            text="Inicie sesión para continuar",
            font=("Arial", 11),
            bg="#f4f4f4",
            fg="#555",
        )
        info.pack(pady=(0, 20))

        panel = tk.Frame(self.frame, bg="#ffffff", padx=30, pady=30)
        panel.pack(padx=20, pady=10)

        tk.Label(panel, text="Correo", bg="#ffffff", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.email_var = tk.StringVar(value="admin@restaurante.com")
        tk.Entry(panel, textvariable=self.email_var, width=30, font=("Arial", 11)).grid(row=1, column=0, pady=(0, 10))

        tk.Label(panel, text="Contraseña", bg="#ffffff", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
        self.password_var = tk.StringVar(value="1234")
        tk.Entry(panel, textvariable=self.password_var, show="*", width=30, font=("Arial", 11)).grid(row=3, column=0, pady=(0, 15))

        tk.Button(
            panel,
            text="Ingresar",
            command=self.login,
            width=20,
            bg="#2e86de",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
        ).grid(row=4, column=0, pady=10)

    def login(self):
        correo = self.email_var.get().strip()
        password = self.password_var.get().strip()

        if not correo or not password:
            messagebox.showerror("Error", "Debe ingresar correo y contraseña.")
            return

        usuario = self.servicio.validar_usuario(correo, password)
        if usuario is None:
            messagebox.showerror("Acceso denegado", "Credenciales incorrectas.")
            return

        self.frame.destroy()
        from restaurante_app.ui.main_view import MainView
        MainView(self.root, self.servicio, usuario)
