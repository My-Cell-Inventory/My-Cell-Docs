# Backlog de producto

Agrupación inicial de capacidades del MVP. Las historias y fechas de entrega quedan por estimar.

| Capacidad | Cobertura | Dependencia de refinamiento |
| --- | --- | --- |
| Acceso | `RF-1.1–1.7` | Asignación de local junto con RF-2 |
| Locales y vendedores | `RF-2.1–2.5` | Usuarios y permisos RF-1 |
| Productos y precios | `RF-3.1–3.8` | Costo promedio coordinado con RF-4 |
| Mercancía e inventario | `RF-4.1–4.11` | Locales RF-2 y catálogo RF-3 |
| Ventas y caja | `RF-5.1–5.12` | Inventario RF-4 y catálogo RF-3 |
| Cambios y garantías | `RF-6.1–6.10` | Venta, caja y stock RF-5 / RF-4 |
| Control físico | `RF-7.1–7.11` | Movimientos RF-4 y vendedores RF-2 |
| Reportes | `RF-8.1–8.12` | Datos de RF-3 a RF-7 |
| Alertas y bitácora | `RF-9.1–9.8` | Integración con los módulos que generan alertas o acciones auditables |

Los [RNF](../04-requirements/non-functional.md) se refinan junto con las capacidades afectadas. Para cada historia registra los IDs específicos, criterios de aceptación, dependencia y validación. Consulta [requisitos funcionales y reglas de negocio](../04-requirements/functional.md) y la [convención de historias](../00-governance/agile-conventions.md).
