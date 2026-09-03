from semana1 import Producto, Cliente


class ProductoFisico(Producto):
    """Hereda de Producto y agrega peso y costo de envio."""

    def __init__(self, codigo, nombre, precio, peso_kg, costo_envio):
        super().__init__(codigo, nombre, precio)
        self.set_peso_kg(peso_kg)
        self.set_costo_envio(costo_envio)

    def get_peso_kg(self):
        return self.__peso_kg

    def set_peso_kg(self, peso_kg):
        if peso_kg <= 0:
            raise ValueError("El peso debe ser mayor que cero")
        self.__peso_kg = float(peso_kg)

    def get_costo_envio(self):
        return self.__costo_envio

    def set_costo_envio(self, costo_envio):
        if costo_envio < 0:
            raise ValueError("El costo de envio no puede ser negativo")
        self.__costo_envio = float(costo_envio)

    def calcular_precio_final(self):
        return self.get_precio() + self.__costo_envio


class ProductoDigital(Producto):
    """Hereda de Producto y agrega formato y tamano del archivo."""

    def __init__(self, codigo, nombre, precio, formato, tamano_mb):
        super().__init__(codigo, nombre, precio)
        self.__formato = formato
        self.set_tamano_mb(tamano_mb)

    def get_formato(self):
        return self.__formato

    def set_formato(self, formato):
        self.__formato = formato

    def get_tamano_mb(self):
        return self.__tamano_mb

    def set_tamano_mb(self, tamano_mb):
        if tamano_mb <= 0:
            raise ValueError("El tamano debe ser mayor que cero")
        self.__tamano_mb = float(tamano_mb)

    def calcular_precio_final(self):
        return self.get_precio()


class DetallePedido:
    """Elemento que forma parte de un Pedido; demuestra composicion."""

    def __init__(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise TypeError("producto debe ser una instancia de Producto")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        self.__producto = producto
        self.__cantidad = int(cantidad)

    def get_producto(self):
        return self.__producto

    def get_cantidad(self):
        return self.__cantidad

    def calcular_subtotal(self):
        return self.__producto.calcular_precio_final() * self.__cantidad


class Pedido:
    """Pedido compuesto por DetallePedido y asociado a un Cliente abstracto."""

    def __init__(self, numero, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("cliente debe ser una instancia de una subclase de Cliente")
        self.__numero = numero
        self.__cliente = cliente
        self.__detalles = []

    def get_numero(self):
        return self.__numero

    def get_cliente(self):
        return self.__cliente

    def get_detalles(self):
        return tuple(self.__detalles)

    def agregar_producto(self, producto, cantidad=1):
        detalle = DetallePedido(producto, cantidad)
        self.__detalles.append(detalle)

    def calcular_subtotal(self):
        return sum(detalle.calcular_subtotal() for detalle in self.__detalles)

    def calcular_descuento(self):
        # Polimorfismo: Pedido no necesita preguntar que tipo de cliente tiene.
        return self.__cliente.calcularDescuento(self.calcular_subtotal())

    def calcular_total(self):
        return self.calcular_subtotal() - self.calcular_descuento()

    def mostrar_resumen(self):
        lineas = [
            f"Pedido: {self.__numero}",
            self.__cliente.mostrar_info(),
            f"Tipo de cliente: {type(self.__cliente).__name__}",
            "Productos:"
        ]
        for detalle in self.__detalles:
            producto = detalle.get_producto()
            lineas.append(
                f"- {producto.get_nombre()} x{detalle.get_cantidad()} = "
                f"${detalle.calcular_subtotal():.2f}"
            )
        lineas.append(f"SUBTOTAL: ${self.calcular_subtotal():.2f}")
        lineas.append(f"DESCUENTO: ${self.calcular_descuento():.2f}")
        lineas.append(f"TOTAL: ${self.calcular_total():.2f}")
        return "\n".join(lineas)
