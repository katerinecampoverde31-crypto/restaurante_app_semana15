import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox


class MainView:
    def __init__(self, root, servicio, usuario):
        self.root = root
        self.servicio = servicio
        self.usuario_actual = usuario
        self.root.title("Restaurante App")
        self.root.geometry("1100x700")
        self.root.configure(bg="#f2f4f8")

        icon_path = Path(__file__).resolve().parents[1] / "assets" / "icono.ppm"
        if icon_path.exists():
            icon = tk.PhotoImage(file=str(icon_path))
            self.root.iconphoto(False, icon)

        self._crear_menu()
        self._crear_contenido()
        self._mostrar_usuarios()

    def _crear_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.menu_app = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Sistema", menu=self.menu_app)
        self.menu_app.add_command(label="Usuarios", command=self._mostrar_usuarios)
        self.menu_app.add_command(label="Productos", command=self._mostrar_productos)
        self.menu_app.add_command(label="Ventas", command=self._mostrar_ventas)
        self.menu_app.add_separator()
        self.menu_app.add_command(label="Salir", command=self.root.destroy)

    def _crear_contenido(self):
        self.main_frame = tk.Frame(self.root, bg="#f2f4f8")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.header = tk.Frame(self.main_frame, bg="#1d3557", height=80)
        self.header.pack(fill="x", padx=2, pady=(0, 10))

        logo_path = Path(__file__).resolve().parents[1] / "assets" / "logo.ppm"
        if logo_path.exists():
            logo = tk.PhotoImage(file=str(logo_path))
            logo_label = tk.Label(self.header, image=logo, bg="#1d3557")
            logo_label.image = logo
            logo_label.pack(side="left", padx=(20, 10), pady=15)

        tk.Label(
            self.header,
            text=f"Bienvenido/a: {self.usuario_actual.nombre}",
            font=("Arial", 16, "bold"),
            bg="#1d3557",
            fg="white",
        ).pack(anchor="w", padx=20, pady=20)

        self.content = tk.Frame(self.main_frame, bg="#f2f4f8")
        self.content.pack(fill="both", expand=True)

    def _mostrar_usuarios(self):
        self._limpiar_contenido()
        tk.Label(self.content, text="Usuarios", font=("Arial", 18, "bold"), bg="#f2f4f8").pack(anchor="w", pady=(0, 10))

        columnas = ("ID", "Nombre", "Correo", "Rol")
        tree = ttk.Treeview(self.content, columns=columnas, show="headings", height=15)
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=180, anchor="center")
        tree.pack(fill="both", expand=True)

        for usuario in self.servicio.obtener_usuarios():
            tree.insert("", "end", values=(usuario.id, usuario.nombre, usuario.correo, usuario.rol))

    def _mostrar_productos(self):
        self._limpiar_contenido()
        tk.Label(self.content, text="Productos", font=("Arial", 18, "bold"), bg="#f2f4f8").pack(anchor="w", pady=(0, 10))

        columnas = ("ID", "Nombre", "Categoría", "Precio")
        tree = ttk.Treeview(self.content, columns=columnas, show="headings", height=15)
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=180, anchor="center")
        tree.pack(fill="both", expand=True)

        for producto in self.servicio.obtener_productos():
            tree.insert("", "end", values=(producto.id, producto.nombre, producto.categoria, f"S/. {producto.precio:.2f}"))

    def _mostrar_ventas(self):
        self._limpiar_contenido()
        tk.Label(self.content, text="Ventas", font=("Arial", 18, "bold"), bg="#f2f4f8").pack(anchor="w", pady=(0, 10))

        form = tk.Frame(self.content, bg="#f2f4f8", pady=10)
        form.pack(fill="x")

        usuarios = self.servicio.obtener_usuarios()
        productos = self.servicio.obtener_productos()

        tk.Label(form, text="Usuario:", bg="#f2f4f8", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")
        self.combo_usuario = ttk.Combobox(form, values=[f"{u.id} - {u.nombre}" for u in usuarios], state="readonly", width=35)
        self.combo_usuario.grid(row=0, column=1, padx=(0, 20), pady=5)
        if usuarios:
            self.combo_usuario.current(0)

        tk.Label(form, text="Producto:", bg="#f2f4f8", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=(0, 10), pady=5, sticky="w")
        self.combo_producto = ttk.Combobox(form, values=[f"{p.id} - {p.nombre}" for p in productos], state="readonly", width=35)
        self.combo_producto.grid(row=0, column=3, padx=(0, 20), pady=5)
        if productos:
            self.combo_producto.current(0)

        tk.Button(
            form,
            text="Registrar venta",
            command=self._callback_registrar_venta,
            bg="#2a9d8f",
            fg="white",
            font=("Arial", 10, "bold"),
            width=18,
            relief="flat",
        ).grid(row=0, column=4, padx=(0, 10), pady=5)

        self.mensaje_var = tk.StringVar(value="")
        tk.Label(form, textvariable=self.mensaje_var, bg="#f2f4f8", fg="#1d3557", font=("Arial", 10, "bold")).grid(row=1, column=0, columnspan=5, sticky="w", pady=(10, 0))

        tabla = ttk.Treeview(self.content, columns=("ID", "Usuario", "Producto", "Fecha"), show="headings", height=15)
        tabla.heading("ID", text="ID")
        tabla.heading("Usuario", text="Usuario")
        tabla.heading("Producto", text="Producto")
        tabla.heading("Fecha", text="Fecha")
        tabla.column("ID", width=60, anchor="center")
        tabla.column("Usuario", width=180, anchor="center")
        tabla.column("Producto", width=180, anchor="center")
        tabla.column("Fecha", width=220, anchor="center")
        tabla.pack(fill="both", expand=True, pady=(10, 0))
        self.tabla_ventas = tabla

        self._cargar_ventas_tabladas()

    def _callback_registrar_venta(self):
        usuario_text = self.combo_usuario.get()
        producto_text = self.combo_producto.get()

        if not usuario_text or not producto_text:
            self.mensaje_var.set("Debe seleccionar un usuario y un producto.")
            return

        usuario_id = int(usuario_text.split(" - ")[0])
        producto_id = int(producto_text.split(" - ")[0])

        resultado = self.servicio.registrar_venta(usuario_id, producto_id)
        if resultado["ok"]:
            self.mensaje_var.set(resultado["mensaje"])
            self._cargar_ventas_tabladas()
            messagebox.showinfo("Venta registrada", resultado["mensaje"])
        else:
            self.mensaje_var.set(resultado["mensaje"])
            messagebox.showerror("Error de venta", resultado["mensaje"])

    def _cargar_ventas_tabladas(self):
        if not hasattr(self, "tabla_ventas"):
            return
        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        for venta in self.servicio.obtener_ventas():
            usuario = next((u for u in self.servicio.obtener_usuarios() if u.id == venta.usuario_id), None)
            producto = next((p for p in self.servicio.obtener_productos() if p.id == venta.producto_id), None)
            self.tabla_ventas.insert(
                "",
                "end",
                values=(venta.id, usuario.nombre if usuario else "Desconocido", producto.nombre if producto else "Desconocido", venta.fecha),
            )

    def _limpiar_contenido(self):
        for widget in self.content.winfo_children():
            widget.destroy()
