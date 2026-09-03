from semana1 import Cliente


class ClienteMayorista(Cliente):
    """Cliente mayorista: 15% si compra $500 o mas; 10% en compras menores."""

    def calcularDescuento(self, subtotal):
        if subtotal < 0:
            raise ValueError("El subtotal no puede ser negativo")
        porcentaje = 0.15 if subtotal >= 500 else 0.10
        return subtotal * porcentaje


class ClienteMinorista(Cliente):
    """Cliente minorista: 5% desde $100; sin descuento por debajo de $100."""

    def calcularDescuento(self, subtotal):
        if subtotal < 0:
            raise ValueError("El subtotal no puede ser negativo")
        if subtotal >= 100:
            return subtotal * 0.05
        return 0.0
