from abc import ABC, abstractmethod


class Producto:
    """Clase base para representar un producto de la tienda."""

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.set_precio(precio)

    # Getters y setters: encapsulacion
    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = float(precio)

    def calcular_precio_final(self):
        return self.__precio

    def mostrar_info(self):
        return f"{self.__codigo} - {self.__nombre}: ${self.__precio:.2f}"


class Cliente(ABC):
    """Clase abstracta comun para todos los tipos de cliente."""

    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.set_correo(correo)

    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        if "@" not in correo:
            raise ValueError("El correo debe contener @")
        self.__correo = correo

    @abstractmethod
    def calcularDescuento(self, subtotal):
        """Devuelve el valor monetario del descuento para un subtotal."""
        raise NotImplementedError

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} ({self.__correo})"
