# Documento de descubrimiento

## Hallazgos documentados

- El negocio necesita un saldo inicial por local para empezar a controlar movimientos.
- La venta debe ser rápida y el Encargado necesita registrar operación diaria sin acceder a costo ni stock.
- Dañados y faltantes impactan la pérdida. Las garantías por defecto se registran por separado.
- El conteo físico es semestral. El monto a favor o a cargo del Encargado lo define el Dueño.

## Datos pendientes de levantar

| Pregunta | Qué aporta |
| --- | --- |
| ¿Cuántos productos, locales y ventas habituales hay? | Define datos de prueba y carga para RNF-4. |
| ¿Qué campos trae el CSV real y qué ejemplos usa el Dueño? | Ayuda a validar plantilla y vista previa. |
| ¿Qué reportes se consultan habitualmente y cuántos pasos son aceptables para vender? | Aterriza la validación de RNF-4 y RNF-6. |
| ¿Qué diferencias de stock y caja se observan al iniciar? | Fija una línea base para medir el impacto del MVP. |

Fuente: [SRS 1.2](../04-requirements/srs-sistema-inventario-mvp-mycell.pdf). El [backlog](product-backlog.md) organiza las capacidades confirmadas.
