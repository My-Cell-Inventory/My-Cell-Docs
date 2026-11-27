# Visión general de MY CELL

My Cell Tecnología necesita formalizar el control de mercancía y conocer ganancias y pérdidas por producto y local. El MVP es una aplicación web para almacenes de accesorios de celulares, utilizable en celular y computador.

| Actor | Responsabilidad |
| --- | --- |
| Dueño Principal | Tiene acceso a todos los módulos. Asigna permisos a los Dueños secundarios. |
| Dueño secundario | Opera en los módulos habilitados por el Dueño Principal. |
| Encargado | Registra ventas, caja, cambios, garantías y dañados de su local. Consulta ventas del día y resultados permitidos. |
| Vendedor | Se registra como referencia de la venta o responsable de un dañado. Carece de cuenta. |

El flujo comienza con el inventario inicial de cada local. Las entradas y salidas determinan el stock. El cierre diario registra diferencias de caja y el inventario físico semestral contrasta existencias calculadas con el conteo.

Consulta el [alcance](scope.md), el [mapa de dominio](../02-domain/domain-map.md) y el [SRS 1.2](../04-requirements/srs-sistema-inventario-mvp-mycell.pdf) (§§ 1–2).
