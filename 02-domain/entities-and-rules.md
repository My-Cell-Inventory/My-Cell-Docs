# Entidades y reglas de negocio

## Entidades principales

| Entidad | Relación o dato clave | Reglas del SRS |
| --- | --- | --- |
| Usuario / local | Cada usuario tiene un número de documento único. El Encargado pertenece a un local y el Dueño secundario tiene módulos asignados por el Principal. Se conserva el historial al desactivar. | RN-1.1 a RN-1.11 |
| Vendedor | Nombre y local. Su atribución es opcional en ventas y obligatoria en dañados. | RN-2.3, RN-2.4, RN-5.6, RN-7.1 |
| Producto / categoría | Nombre único comparado sin mayúsculas, tildes ni espacios extra, margen, precio, stock mínimo y garantía. Un producto nuevo queda pendiente hasta tener precio. | RN-3.1 a RN-3.10 |
| Proveedor / carga | Carga identificada por proveedor y documento. Anulación con motivo, historial y control de stock negativo. | RN-4.6, RN-4.8 a RN-4.10 |
| Entrada / existencia | Entradas por carga, local y producto con cantidad y costo unitario. El stock se calcula a partir de los movimientos. | RN-4.1 a RN-4.5, RN-4.7 |
| Venta y detalle | Consecutivo, local y líneas con precio, costo del momento y vencimiento de garantía. | RN-5.2 a RN-5.6, RF-5.2 |
| Movimiento de caja / cierre | Ingresos y egresos, efectivo o transferencia. Cierre con total esperado, contado y diferencia. | RN-5.7, RF-5.10 |
| Cambio / garantía | Relacionados con la venta y su unidad. El cambio puede mover caja y la garantía puede consumir un reemplazo. | RN-6.1 a RN-6.9 |
| Dañado / inventario físico | Dañado al costo con vendedor responsable. Conteo semestral y monto final ingresado por el Dueño. | RN-7.1 a RN-7.8 |
| Notificación / bitácora | Panel y correo según evento. Registro con actor, acción, local y fecha. | RN-9.1 a RN-9.4 |

## Cálculos e invariantes

- Stock por local y producto: saldo inicial más entradas y devoluciones, menos salidas registradas. Se rechaza una venta que exceda las existencias (RN-4.1, RN-4.5, RN-5.5).
- Costo promedio ponderado por local: `(stock × costo actual + cantidad nueva × costo nuevo) ÷ (stock + cantidad nueva)`. Precio sugerido: `costo promedio × (1 + margen)` (RN-3.2 y RN-3.3).
- Ganancia por venta: `(precio de venta - costo del momento) × cantidad`. La pérdida incluye dañados y faltantes al costo y ventas bajo costo. Las garantías se muestran por separado (RN-8.1 a RN-8.5).
- Un cambio o garantía exige vigencia y admite un solo trámite por unidad vendida. Un cambio reingresa la devolución en buen estado. El reemplazo por garantía sale sin ingreso (RN-6.1, RN-6.4, RN-6.7, RN-6.9).
- El conteo físico muestra faltantes y sobrantes. El Dueño determina el monto final y el Encargado ve resultado y monto sin costos por producto (RN-7.4 a RN-7.8).
- Los movimientos de stock y caja se guardan juntos o se revierten. La desactivación y la anulación preservan el historial (RNF-3).

Consulta las [requisitos funcionales y reglas de negocio](../04-requirements/functional.md) para la enumeración completa.
