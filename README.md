# Actividad Semanas 1 y 2 - POO, UML, Herencia y Composicion

## Descripcion
Proyecto sencillo de una tienda en linea desarrollado en Python. Demuestra:

- Clases y objetos.
- Encapsulacion mediante atributos privados y getters/setters.
- Herencia con `ProductoFisico` y `ProductoDigital` a partir de `Producto`.
- Composicion entre `Pedido` y `DetallePedido`.
- Polimorfismo al redefinir `calcular_precio_final()`.

## Estructura
- `codigo/semana1.py`: clases base `Producto` y `Cliente`.
- `codigo/semana2.py`: herencia, composicion y clases de la segunda semana.
- `codigo/main.py`: ejemplo funcional.
- `diagramas/`: diagramas UML de las semanas 1 y 2.

## Ejecucion
Desde la carpeta `codigo`:

```bash
python main.py
```

Salida esperada aproximada:

```text
Pedido: PED-001
Cliente: Ana Perez (ana@email.com)
Productos:
- Laptop x1 = $865.00
- Curso de Python x2 = $60.00
TOTAL: $925.00
```
