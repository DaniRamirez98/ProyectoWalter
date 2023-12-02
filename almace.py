from guizero import App, Box, PushButton, Text, TextBox, ListBox, Combo, CheckBox, info

# Datos de ejemplo para iniciar el programa
productos = [
    {"codigo": "001", "descripcion": "Producto A", "precio": 10.0, "stock": 100, "proveedor": "Proveedor1", "ubicacion": "Almacen1"},
    # Agregar más productos según sea necesario
]

proveedores = ["Proveedor1", "Proveedor2", "Proveedor3"]

# Función para actualizar la ListBox de productos
def actualizar_lista():
    lista_productos.clear()
    for producto in productos:
        lista_productos.append(producto["descripcion"])

# Función para agregar un nuevo producto
def agregar_producto():
    nuevo_producto = {
        "codigo": codigo_entry.value,
        "descripcion": descripcion_entry.value,
        "precio": float(precio_entry.value),
        "stock": int(stock_entry.value),
        "proveedor": proveedor_combo.value,
        "ubicacion": ubicacion_entry.value
    }
    productos.append(nuevo_producto)
    actualizar_lista()
    limpiar_campos()

# Función para eliminar un producto
def eliminar_producto():
    indice = lista_productos.value
    if indice is not None:
        del productos[indice]
        actualizar_lista()

# Función para limpiar los campos del formulario
def limpiar_campos():
    codigo_entry.value = ""
    descripcion_entry.value = ""
    precio_entry.value = ""
    stock_entry.value = ""
    proveedor_combo.value = proveedores[0]
    ubicacion_entry.value = ""

# Crear la aplicación
app = App("Sistema de Gestión de Inventario")

# Crear widgets
lista_productos = ListBox(app, items=[], width=40, height=10, command=limpiar_campos)
detalles_box = Box(app, layout="grid")
codigo_label = Text(detalles_box, text="Código:", grid=[0, 0])
codigo_entry = TextBox(detalles_box, grid=[1, 0])
descripcion_label = Text(detalles_box, text="Descripción:", grid=[0, 1])
descripcion_entry = TextBox(detalles_box, grid=[1, 1])
precio_label = Text(detalles_box, text="Precio:", grid=[0, 2])
precio_entry = TextBox(detalles_box, grid=[1, 2])
stock_label = Text(detalles_box, text="Stock:", grid=[0, 3])
stock_entry = TextBox(detalles_box, grid=[1, 3])
proveedor_label = Text(detalles_box, text="Proveedor:", grid=[0, 4])
proveedor_combo = Combo(detalles_box, options=proveedores, grid=[1, 4])
ubicacion_label = Text(detalles_box, text="Ubicación:", grid=[0, 5])
ubicacion_entry = TextBox(detalles_box, grid=[1, 5])
agregar_button = PushButton(detalles_box, text="Agregar", command=agregar_producto, grid=[0, 6])
eliminar_button = PushButton(detalles_box, text="Eliminar", command=eliminar_producto, grid=[1, 6])

# Actualizar la lista de productos al inicio
actualizar_lista()

# Ejecutar la aplicación
app.display()
