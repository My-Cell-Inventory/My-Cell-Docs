# Mapa de dominio

El MVP se organiza en nueve áreas funcionales. El mapa describe responsabilidades de negocio.

| Módulo | Área | Conceptos | Responsabilidad |
| --- | --- | --- | --- |
| RF-1 | Acceso | Usuario y asignación | Sesión, permisos por rol y local, y habilitación de módulos para Dueños secundarios |
| RF-2 | Locales y vendedores | Local y vendedor | Ubicación de inventario, caja, ventas y vendedores |
| RF-3 | Productos y precios | Producto, categoría y cambio de precio | Nombre único, precio, margen, productos pendientes y garantía |
| RF-4 | Mercancía e inventario | Proveedor, carga, entrada, movimiento y existencia | Inventario inicial, registro y anulación de cargas, costo promedio y kardex |
| RF-5 | Ventas y caja | Venta, detalle, movimiento de caja y cierre | Existencias, precio y costo histórico, garantía y caja |
| RF-6 | Cambios y garantías | Cambio y garantía | Vigencia, reingreso, reemplazo y diferencia de precio |
| RF-7 | Control físico | Dañado, conteo y resultado | Responsable, diferencias del conteo y monto manual |
| RF-8 | Reportes | Consultas de operación | Stock, ventas, caja, ganancias y pérdidas |
| RF-9 | Alertas y bitácora | Notificación y entrada de bitácora | Alertas de negocio e historial de acciones |

## Relaciones principales

- Local delimita existencias, vendedores, ventas, cierres y conteos. Acceso restringe la operación del Encargado a su local.
- Mercancía actualiza el stock y el costo promedio. Ventas usan el stock y conservan el costo de ese momento para reportes.
- Cambios y garantías consultan la venta y pueden mover mercancía y caja. Dañados y conteos explican pérdidas y diferencias.
- Reportes consultan las operaciones registradas. Alertas y bitácora ofrecen visibilidad al Dueño y los avisos de caja al Encargado.

Ver [entidades y reglas](entities-and-rules.md) y [requisitos funcionales y reglas de negocio](../04-requirements/functional.md).
