# Eventos de dominio

Hechos de negocio derivados del SRS. Las consecuencias de la tabla describen el comportamiento esperado. La implementación y los contratos técnicos se definirán con la arquitectura.

| Hecho | Consecuencia de negocio | Fuente |
| --- | --- | --- |
| Encargado reemplazado | Se revoca el acceso anterior y se habilita al nuevo Encargado. | RF-1.5 |
| Mercancía ingresada | Se actualizan stock y costo promedio por local. Un CSV confirmado se aplica completo. | RF-3.5, RF-4.1, RF-4.6, RF-4.9 |
| Venta registrada | Se registra ingreso a caja y se descuentan existencias. Se conserva precio, costo y garantía. | RN-4.1, RN-5.2, RF-5.5 |
| Venta anulada | Se repone stock, se ajusta caja y se conserva el motivo. | RF-5.11 |
| Cierre de caja con diferencia | Se alerta al Dueño y al Encargado del local. | RF-5.10, RF-9.5 |
| Cambio aprobado | Se actualizan mercancía y caja según el caso. Se avisa al Dueño. | RF-6.3 a RF-6.5, RF-6.9 |
| Garantía registrada | Se separa el producto defectuoso, se descuenta el reemplazo si aplica y se avisa al Dueño. | RF-6.6 a RF-6.9 |
| Dañado registrado | Se descuenta stock, se reconoce la pérdida y se avisa al Dueño con el responsable. | RF-7.1 a RF-7.3 |
| Inventario físico cerrado | Se conserva el resultado y el monto del conteo por local. | RF-7.6 a RF-7.10 |
| Stock bajo o venta bajo costo | Se genera la alerta prevista por el SRS. | RF-9.3, RF-9.4 |

Ver [requisitos funcionales y reglas de negocio](../04-requirements/functional.md).
