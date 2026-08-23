from semana1 import Cliente
from semana2 import ProductoFisico, ProductoDigital, Pedido


def main():
    cliente = Cliente("1723456789", "Ana Perez", "ana@email.com")

    laptop = ProductoFisico(
        "P001", "Laptop", 850.00, peso_kg=2.0, costo_envio=15.00
    )
    curso = ProductoDigital(
        "D001", "Curso de Python", 30.00, formato="MP4/PDF", tamano_mb=1200
    )

    pedido = Pedido("PED-001", cliente)
    pedido.agregar_producto(laptop, 1)
    pedido.agregar_producto(curso, 2)

    print(pedido.mostrar_resumen())


if __name__ == "__main__":
    main()
