# Definición del problema

## Situación actual

El negocio carece de inventario formal. El problema definido en el [SRS 1.2](../04-requirements/srs-sistema-inventario-mvp-mycell.pdf) es controlar lo que llega y sale, y conocer ganancias y pérdidas por producto y local.

| Actor | Necesidad |
| --- | --- |
| Dueño | Saber cuánto hay, cuánto vale, por qué cambió y qué pérdidas debe revisar. |
| Encargado | Registrar ventas, caja e incidencias del día de forma ágil y con alcance por local. |
| Vendedor | Quedar identificado en las ventas cuando se seleccione y en los dañados cuando sea responsable. |

## Criterios de éxito del MVP

- Conciliar stock calculado con movimientos registrados e inventario físico.
- Registrar una venta sin superar stock, conservar su costo histórico y registrar su ingreso a caja.
- Limitar al Encargado a los datos autorizados y permitir al Dueño reportar resultados por local.
- Registrar ventas y consultar reportes habituales en menos de 3 segundos (RNF-4).

La línea base de tiempos y discrepancias se levantará con la operación. Ver [descubrimiento](discovery-brief.md).
