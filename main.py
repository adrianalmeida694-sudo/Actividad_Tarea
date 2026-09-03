from semana2 import ProductoFisico, ProductoDigital, Pedido
from semana3 import ClienteMayorista, ClienteMinorista


def crear_pedido(numero, cliente, laptop, curso):
    pedido = Pedido(numero, cliente)
    pedido.agregar_producto(laptop, 1)
    pedido.agregar_producto(curso, 2)
    return pedido


def main():
    # Dos objetos diferentes que comparten la abstraccion Cliente.
    clientes = [
        ClienteMayorista("1790012345001", "Distribuidora Andina", "ventas@andina.ec"),
        ClienteMinorista("1723456789", "Ana Perez", "ana@email.com"),
    ]

    laptop = ProductoFisico(
        "P001", "Laptop", 850.00, peso_kg=2.0, costo_envio=15.00
    )
    curso = ProductoDigital(
        "D001", "Curso de Python", 30.00, formato="MP4/PDF", tamano_mb=1200
    )

    pedidos = [
        crear_pedido("PED-MAY-001", clientes[0], laptop, curso),
        crear_pedido("PED-MIN-001", clientes[1], laptop, curso),
    ]

    # La misma operacion funciona para ambos tipos de cliente.
    for pedido in pedidos:
        print(pedido.mostrar_resumen())
        print("-" * 50)


if __name__ == "__main__":
    main()
