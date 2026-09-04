# Actividad Semanas 1, 2 y 3 - Programación Orientada a Objetos

## Descripción

Proyecto de una tienda en línea desarrollado en Python para aplicar los principales conceptos de Programación Orientada a Objetos.

Durante las tres semanas se implementaron progresivamente:

- Clases y objetos.
- Encapsulación mediante atributos privados y getters/setters.
- Herencia con `ProductoFisico` y `ProductoDigital` a partir de `Producto`.
- Composición entre `Pedido` y `DetallePedido`.
- Clase abstracta `Cliente`.
- Herencia mediante `ClienteMayorista` y `ClienteMinorista`.
- Sobrescritura del método `calcularDescuento()`.
- Polimorfismo para calcular diferentes descuentos según el tipo real de cliente.

## Objetivo

Desarrollar un sistema básico de tienda en línea utilizando Python, aplicando los conceptos de Programación Orientada a Objetos estudiados durante las semanas 1, 2 y 3, como clases, objetos, encapsulación, herencia, composición, clases abstractas y polimorfismo.

## Principales funcionalidades

- Creación y gestión de productos físicos y digitales.
- Creación de clientes mayoristas y minoristas.
- Registro de productos dentro de un pedido.
- Cálculo del subtotal del pedido.
- Cálculo de descuentos según el tipo de cliente.
- Cálculo del valor total a pagar.

## Semana 1

Se desarrollaron las clases base del sistema, aplicando clases, objetos y encapsulación.

## Semana 2

Se extendió la solución mediante herencia y composición, incorporando diferentes tipos de productos y la gestión de pedidos.

## Semana 3 - Polimorfismo, interfaces y clases abstractas

Se extendió la solución desarrollada durante las semanas anteriores.

`Cliente` se definió como una clase abstracta que establece el método `calcularDescuento()`.

Las clases `ClienteMayorista` y `ClienteMinorista` heredan de `Cliente` y sobrescriben dicho método, proporcionando un comportamiento diferente para el cálculo del descuento.

El sistema utiliza polimorfismo debido a que la clase `Pedido` puede trabajar con cualquier objeto que herede de `Cliente`. Al ejecutar `calcularDescuento()`, Python selecciona automáticamente el comportamiento correspondiente al tipo real de cliente, evitando condicionales innecesarios.

### Descuentos implementados

- Cliente Mayorista:
  - 15% de descuento para compras iguales o superiores a $500.
  - 10% de descuento para compras menores a $500.

- Cliente Minorista:
  - 5% de descuento para compras iguales o superiores a $100.
  - Sin descuento para compras menores a $100.

## Estructura del proyecto

- `semana1.py`: clases base desarrolladas en la Semana 1.
- `semana2.py`: herencia, composición y funcionalidades de la Semana 2.
- `semana3.py`: clase abstracta Cliente, ClienteMayorista y ClienteMinorista.
- `main.py`: demostración funcional del sistema.
- `test_semana3.py`: pruebas del comportamiento implementado.
- `uml_semana1.png`: diagrama UML de la Semana 1.
- `uml_semana2.png`: diagrama UML de la Semana 2.
- `uml_semana3.png`: diagrama UML actualizado de la Semana 3.

## Ejecución

Para ejecutar el programa:

```bash
python main.py
```

## Lenguaje utilizado

Python
