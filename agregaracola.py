# Simulación de la base de datos de stock
stock_de_productos = {
    'producto1': 10,
    'producto2': 0,
    'producto3': 5,
}

def verificar_stock(producto_id):
    """
    Verifica si hay stock disponible para el producto dado.

    Args:
    - producto_id (str): El identificador del producto.

    Returns:
    - bool: True si hay stock disponible, False si no hay stock.
    """
    # Obtiene el stock del producto; retorna 0 si el producto no existe
    cantidad_stock = stock_de_productos.get(producto_id, 0)

    # Verifica si hay stock disponible
    return cantidad_stock > 0

# Ejemplo de uso
producto_id = 'producto1'
if verificar_stock(producto_id):
    print(f"El {producto_id} está disponible y puede agregarse al carrito.")
else:
    print(f"El {producto_id} no está disponible.")
