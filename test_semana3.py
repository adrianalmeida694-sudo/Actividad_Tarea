import unittest

from semana1 import Cliente
from semana2 import ProductoFisico, ProductoDigital, Pedido
from semana3 import ClienteMayorista, ClienteMinorista


class TestSemana3(unittest.TestCase):
    def setUp(self):
        self.laptop = ProductoFisico("P001", "Laptop", 850, 2, 15)
        self.curso = ProductoDigital("D001", "Curso", 30, "MP4", 1200)

    def crear_pedido(self, cliente):
        pedido = Pedido("TEST", cliente)
        pedido.agregar_producto(self.laptop, 1)
        pedido.agregar_producto(self.curso, 2)
        return pedido

    def test_cliente_es_abstracto(self):
        with self.assertRaises(TypeError):
            Cliente("1", "Nombre", "correo@email.com")

    def test_mayorista_usa_sobrescritura(self):
        cliente = ClienteMayorista("1", "Mayorista", "m@email.com")
        pedido = self.crear_pedido(cliente)
        self.assertAlmostEqual(pedido.calcular_subtotal(), 925.0)
        self.assertAlmostEqual(pedido.calcular_descuento(), 138.75)
        self.assertAlmostEqual(pedido.calcular_total(), 786.25)

    def test_minorista_usa_sobrescritura(self):
        cliente = ClienteMinorista("2", "Minorista", "n@email.com")
        pedido = self.crear_pedido(cliente)
        self.assertAlmostEqual(pedido.calcular_descuento(), 46.25)
        self.assertAlmostEqual(pedido.calcular_total(), 878.75)


if __name__ == "__main__":
    unittest.main()
