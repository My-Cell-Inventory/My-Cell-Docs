# Requisitos funcionales

> Fuente: [SRS del Sistema de Inventario MVP, versión 1.1](srs-sistema-inventario-mvp-mycell.pdf) · 19 de noviembre de 2026

Los identificadores `RF-módulo.número` y `RN-módulo.número` corresponden a la sección 3 del SRS. La matriz de permisos se encuentra en la sección 4 (p. 13). El MVP tiene un Dueño Principal, puede tener Dueños secundarios con permisos por módulo y tiene un Encargado activo por local. Las operaciones del Encargado se limitan a su local y los vendedores se registran como datos.

## 1. Acceso, usuarios y roles

SRS, pp. 4–5.

### Reglas de negocio

- **RN-1.1** — Solo existen dos roles con acceso: Dueño y Encargado. El rol Dueño tiene dos tipos: Dueño Principal y Dueño secundario. Los vendedores no tienen cuenta.
- **RN-1.2** — Cada Encargado pertenece a un solo local y solo puede operar sobre ese local.
- **RN-1.3** — Los permisos se validan en el servidor, no solo ocultando botones en pantalla.
- **RN-1.4** — Los usuarios nunca se eliminan: se desactivan para conservar su historial. Aplica a Dueños y Encargados.
- **RN-1.5** — Se inicia sesión con número de documento (único por usuario) y contraseña.
- **RN-1.6** — El Dueño Principal se crea con datos semilla al instalar el sistema. Tiene todos los permisos, no se puede desactivar y es el único que asigna permisos a los Dueños secundarios.
- **RN-1.7** — Los permisos de un Dueño secundario se asignan por módulo (RF-1 a RF-9). Un módulo no habilitado no se ve ni se puede operar.
- **RN-1.8** — En los demás módulos, «Dueño» se refiere a cualquier Dueño que tenga ese módulo habilitado (el Principal siempre lo tiene).
- **RN-1.9** — Solo los Dueños crean, editan, desactivan y reactivan Dueños y Encargados. Un Dueño secundario no puede editar ni desactivar al Principal ni cambiar permisos. El Encargado no edita sus datos; solo cambia su contraseña con la recuperación.
- **RN-1.10** — El sistema es solo para mayores de edad. Al registrar un Encargado o un Dueño se muestra un aviso que debe aceptarse; la aceptación queda en bitácora. No se pide tipo de documento. La responsabilidad recae en quien registra.
- **RN-1.11** — El código de verificación de 6 dígitos tiene vencimiento corto y límite de intentos (valores por definir; sugerencia: 10 minutos y 5 intentos). El mensaje no revela si el correo existe.

### Requisitos

| ID | Requisito | Rol |
| --- | --- | --- |
| RF-1.1 | Inicio de sesión con número de documento y contraseña. | Dueño y Encargado |
| RF-1.2 | Cierre de sesión y expiración automática por inactividad. | Dueño y Encargado |
| RF-1.3 | Restablecer contraseña: en «¿Olvidaste tu contraseña?» se pide el correo, se envía un código de 6 dígitos (SMTP) y se define la nueva contraseña. | Dueño y Encargado |
| RF-1.4 | Registrar Encargados con nombre, apellidos, número de documento y email, asignarlos a un local y mostrar el aviso de mayoría de edad. | Dueño |
| RF-1.5 | Cambiar el Encargado de un local: el anterior pierde acceso al instante y el nuevo lo recibe. | Dueño |
| RF-1.6 | Desactivar y reactivar Dueños y Encargados conservando todo su historial. El Dueño Principal no se puede desactivar. | Dueño |
| RF-1.7 | Mostrar menús, datos y acciones según el rol y los módulos habilitados, y rechazar en el servidor cualquier acción no permitida. | Sistema |
| RF-1.8 | Registrar Dueños secundarios con los mismos datos y el aviso de mayoría de edad. | Dueño |
| RF-1.9 | Editar los datos de Dueños y Encargados. | Dueño |
| RF-1.10 | Asignar y cambiar los módulos habilitados de cada Dueño secundario. | Dueño Principal |

> **Texto sugerido del aviso (RN-1.10):** «Este sistema es solo para personas mayores de 18 años. No se permite registrar menores de edad. Al continuar, declaras que la persona que registras es mayor de edad y asumes la responsabilidad por esa declaración.»

## 2. Locales y vendedores

SRS, pp. 5–6.

### Reglas de negocio

- **RN-2.1** — Admitir uno o varios locales.
- **RN-2.2** — Cada local tiene inventario, caja y ventas propios.
- **RN-2.3** — El vendedor se identifica por nombre y local y carece de acceso.
- **RN-2.4** — Un vendedor desactivado conserva su historial de ventas y dañados.

### Requisitos

| ID | Requisito | Rol |
| --- | --- | --- |
| RF-2.1 | Crear, editar y desactivar locales. | Dueño |
| RF-2.2 | Consultar locales y su Encargado actual. | Dueño |
| RF-2.3 | Registrar vendedores y asociarlos a un local. | Dueño |
| RF-2.4 | Editar y desactivar vendedores. | Dueño |
| RF-2.5 | Listar los vendedores activos del local al registrar una venta o un producto dañado. | Dueño y Encargado |

## 3. Productos y precios

SRS, p. 6.

### Reglas de negocio

- **RN-3.1** — El SKU es único.
- **RN-3.2** — Precio sugerido = costo promedio × (1 + margen). El Dueño puede ajustar el precio final.
- **RN-3.3** — Costo promedio por local = (stock actual × costo actual + cantidad nueva × costo nuevo) ÷ (stock actual + cantidad nueva).
- **RN-3.4** — El Encargado solo ve nombre y precio de venta.
- **RN-3.5** — La garantía se define en días, admite 0 y aplica por igual a cambios y garantías.

### Requisitos

| ID | Requisito | Rol |
| --- | --- | --- |
| RF-3.1 | Crear y editar productos con SKU, nombre, categoría, costo, margen, precio, stock mínimo y días de garantía. | Dueño |
| RF-3.2 | Gestionar categorías. | Dueño |
| RF-3.3 | Definir margen por categoría o producto. | Dueño |
| RF-3.4 | Consultar el precio sugerido calculado por el sistema y fijar el precio final. | Dueño |
| RF-3.5 | Recalcular el costo promedio al ingresar mercancía. | Sistema |
| RF-3.6 | Consultar el catálogo con nombre y precio de venta. | Encargado |
| RF-3.7 | Desactivar productos y conservar su historial. | Dueño |
| RF-3.8 | Guardar quién y cuándo cambió el precio o margen, junto con los valores anterior y nuevo. | Sistema |

## 4. Entradas de mercancía e inventario

SRS, p. 7.

### Reglas de negocio

- **RN-4.1** — El stock se calcula como entradas menos salidas (ventas, cambios, dañados, garantías y faltantes) más devoluciones.
- **RN-4.2** — Cada entrada guarda fecha, local, proveedor, producto, cantidad y costo unitario.
- **RN-4.3** — Solo el Dueño carga mercancía y consulta inventario.
- **RN-4.4** — Se valida todo el CSV antes de guardar. Un error impide guardar la carga.
- **RN-4.5** — El primer conteo del local es el inventario inicial y sirve como base de los cálculos.

### Requisitos

| ID | Requisito | Rol |
| --- | --- | --- |
| RF-4.1 | Registrar una entrada manual de mercancía. | Dueño |
| RF-4.2 | Descargar la plantilla CSV con las columnas requeridas. | Dueño |
| RF-4.3 | Cargar entradas de un CSV para un local de destino. | Dueño |
| RF-4.4 | Validar columnas obligatorias, números mayores que 0 y detectar SKUs repetidos. | Sistema |
| RF-4.5 | Revisar antes de confirmar los productos nuevos, existentes y las filas con error. | Dueño |
| RF-4.6 | Guardar toda la carga en una única operación atómica. | Sistema |
| RF-4.7 | Crear automáticamente los productos cuyo SKU aún no existe. | Sistema |
| RF-4.8 | Registrar el inventario inicial de un local. | Dueño |
| RF-4.9 | Calcular stock por producto y local. | Sistema |
| RF-4.10 | Consultar stock, costo y valor total del inventario por local. | Dueño |
| RF-4.11 | Consultar el kardex de cada producto. | Dueño |

## 5. Ventas y caja

SRS, p. 8.

### Reglas de negocio

- **RN-5.1** — El vendedor informa y entrega dinero fuera del sistema. El Encargado registra la venta.
- **RN-5.2** — Cada venta conserva precio, costo vigente y vencimiento de garantía calculado desde la fecha de venta.
- **RN-5.3** — El Dueño corrige anulando con motivo. El Encargado carece de permisos de edición y borrado.
- **RN-5.4** — El Encargado ve las ventas del día de su local, con la consulta limitada de RF-5.9.
- **RN-5.5** — El sistema rechaza ventas por encima del stock sin mostrar existencias al Encargado.
- **RN-5.6** — Elegir vendedor es opcional.
- **RN-5.7** — Caja = ingresos menos egresos. Los medios de pago son efectivo y transferencia.

### Requisitos

| ID | Requisito | Rol |
| --- | --- | --- |
| RF-5.1 | Registrar ventas con productos, cantidades, medio de pago y vendedor opcional. | Dueño y Encargado |
| RF-5.2 | Asignar un consecutivo a cada venta para el recibo. | Sistema |
| RF-5.3 | Calcular el vencimiento de garantía por producto vendido. | Sistema |
| RF-5.4 | Validar existencias sin mostrar la cantidad al Encargado. | Sistema |
| RF-5.5 | Registrar cada venta como ingreso de caja. | Sistema |
| RF-5.6 | Registrar retiros de dinero del Dueño como egresos de caja. | Dueño y Encargado |
| RF-5.7 | Consultar ventas del día y lo vendido. El Encargado consulta su local y el Dueño todos los locales. | Dueño y Encargado |
| RF-5.8 | Consultar ventas por rango de fechas y local. | Dueño |
| RF-5.9 | Buscar ventas anteriores por número y ver únicamente producto, fecha y vigencia de garantía. | Encargado |
| RF-5.10 | Cerrar caja a diario con total esperado, contado y diferencia. | Encargado |
| RF-5.11 | Anular una venta con motivo, reponer el stock y ajustar caja. | Dueño |
| RF-5.12 | Consultar historial de cierres y diferencias. | Dueño |

## 6. Cambios y garantías

SRS, p. 9.

### Reglas de negocio

- **RN-6.1** — Ambos trámites usan los días de garantía contados desde la venta. Se bloquean al vencer el plazo.
- **RN-6.2** — La venta se identifica por su número.
- **RN-6.3** — Si el nuevo producto vale más se cobra la diferencia. Si vale menos se devuelve. Ambos casos se registran en caja.
- **RN-6.4** — El producto devuelto en buen estado vuelve al stock. El resto se registra como garantía.
- **RN-6.5** — El Encargado aprueba cambios y el Dueño recibe un aviso por panel y correo.
- **RN-6.6** — La garantía corresponde a defecto de fábrica. Sale del stock disponible y no cuenta como faltante, dañado ni cobro al Encargado.
- **RN-6.7** — El reemplazo sale de stock sin ingreso.
- **RN-6.8** — El sistema registra y avisa. El reclamo al proveedor se gestiona fuera del sistema.
- **RN-6.9** — Cada unidad puede cambiarse o entrar en garantía una sola vez.

### Requisitos

| ID | Requisito | Rol |
| --- | --- | --- |
| RF-6.1 | Buscar la venta por número y verificar vigencia. | Dueño y Encargado |
| RF-6.2 | Bloquear trámites vencidos con un mensaje claro. | Sistema |
| RF-6.3 | Registrar cambio con producto devuelto, su estado y producto nuevo. | Dueño y Encargado |
| RF-6.4 | Calcular la diferencia de precio y registrar el movimiento en caja. | Sistema |
| RF-6.5 | Reingresar al stock el producto devuelto en buen estado. | Sistema |
| RF-6.6 | Registrar la garantía con producto, descripción del defecto y reemplazo si aplica. | Dueño y Encargado |
| RF-6.7 | Separar los productos en garantía del stock disponible. | Sistema |
| RF-6.8 | Descontar el reemplazo sin registrar ingreso. | Sistema |
| RF-6.9 | Notificar al Dueño cada cambio y garantía registrados. | Sistema |
| RF-6.10 | Consultar cambios y garantías por local y fecha. | Dueño |

## 7. Dañados, faltantes e inventario físico

SRS, p. 10.

### Reglas de negocio

- **RN-7.1** — Un dañado por el personal exige identificar al vendedor responsable.
- **RN-7.2** — El dañado sale del stock y se registra como pérdida al costo.
- **RN-7.3** — Las garantías se excluyen de dañados y faltantes.
- **RN-7.4** — El Dueño hace inventario físico cada seis meses por local. El Encargado solo ve el resultado.
- **RN-7.5** — Faltante = stock del sistema menos cantidad contada. También se muestran sobrantes.
- **RN-7.6** — El Encargado paga faltantes y dañados. Si no los hay, recibe el porcentaje pactado.
- **RN-7.7** — El Dueño ingresa el monto final de cobro o pago. El sistema no calcula el porcentaje ni el cobro.
- **RN-7.8** — El Encargado ve el resultado y el monto sin costos por producto.

### Requisitos

| ID | Requisito | Rol |
| --- | --- | --- |
| RF-7.1 | Registrar el dañado con vendedor responsable, fecha y observación. | Dueño y Encargado |
| RF-7.2 | Descontar del stock y registrar la pérdida al costo. | Sistema |
| RF-7.3 | Avisar al Dueño de cada producto dañado e identificar al responsable. | Sistema |
| RF-7.4 | Crear un inventario físico por local. | Dueño |
| RF-7.5 | Registrar el conteo por producto. | Dueño |
| RF-7.6 | Comparar el conteo con el stock y mostrar faltantes y sobrantes. | Sistema |
| RF-7.7 | Mostrar dañados del periodo con el vendedor responsable. | Dueño y Encargado |
| RF-7.8 | Registrar monto a cargo o a favor del Encargado y una observación. | Dueño |
| RF-7.9 | Cerrar el inventario físico y conservar el historial. | Dueño |
| RF-7.10 | Consultar el resultado y el monto de su local. | Encargado |
| RF-7.11 | Recordar al Dueño por panel y correo el próximo inventario de cada local. | Sistema |

## 8. Reportes

SRS, p. 11.

### Reglas de negocio

- **RN-8.1** — Ganancia = (precio de venta menos costo en el momento de venta) × cantidad vendida.
- **RN-8.2** — Pérdida = dañados y faltantes valorados al costo, más las ventas por debajo del costo.
- **RN-8.3** — Las garantías se reportan por separado y se excluyen de la pérdida del local.
- **RN-8.4** — El Encargado consulta las ventas y caja del día de su local.
- **RN-8.5** — El costo histórico de cada venta se conserva para que los reportes pasados no cambien.

### Requisitos

| ID | Requisito | Rol |
| --- | --- | --- |
| RF-8.1 | Consultar stock actual y valor de inventario por local. | Dueño |
| RF-8.2 | Consultar productos bajo el stock mínimo. | Dueño |
| RF-8.3 | Consultar ganancias y pérdidas por producto en un rango de fechas. | Dueño |
| RF-8.4 | Consultar ganancias y pérdidas por local. | Dueño |
| RF-8.5 | Comparar locales por margen real. | Dueño |
| RF-8.6 | Consultar los productos más vendidos y los que no tienen movimiento. | Dueño |
| RF-8.7 | Consultar dañados por vendedor. | Dueño |
| RF-8.8 | Consultar cambios y garantías. | Dueño |
| RF-8.9 | Consultar ventas del día y lo vendido. | Dueño y Encargado |
| RF-8.10 | Consultar caja del día y diferencias de cierre. | Dueño y Encargado |
| RF-8.11 | Filtrar reportes por fecha, local y producto. | Dueño |
| RF-8.12 | Exportar reportes a CSV. | Dueño |

## 9. Notificaciones y bitácora

SRS, p. 12.

### Reglas de negocio

- **RN-9.1** — Las alertas del Dueño llegan por panel y correo SMTP.
- **RN-9.2** — El Encargado solo recibe alertas por descuadres de caja.
- **RN-9.3** — WhatsApp queda fuera del MVP.
- **RN-9.4** — La bitácora guarda quién, qué, en qué local y cuándo.

### Requisitos

| ID | Requisito | Rol |
| --- | --- | --- |
| RF-9.1 | Mostrar panel de notificaciones con contador de no leídas. | Dueño y Encargado |
| RF-9.2 | Marcar notificaciones como leídas. | Dueño y Encargado |
| RF-9.3 | Enviar correo SMTP al Dueño por cambios aprobados, garantías, dañados, diferencias de caja y stock bajo. | Sistema |
| RF-9.4 | Alertar sobre ventas por debajo del costo. | Sistema |
| RF-9.5 | Alertar al Dueño y al Encargado cuando el cierre de caja tenga diferencia. | Sistema |
| RF-9.6 | Configurar el correo destinatario y el servidor SMTP. | Dueño |
| RF-9.7 | Registrar acciones sobre ventas, caja, cambios, garantías, dañados, precios, mercancía, usuarios e inventarios. | Sistema |
| RF-9.8 | Consultar la bitácora por usuario, local, acción y fecha. | Dueño |
