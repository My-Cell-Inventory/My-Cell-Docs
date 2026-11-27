# Especificación de Requisitos de Software (SRS)

## Sistema de Inventario – Producto Mínimo Viable (MVP)

**Control de mercancía, ganancias y pérdidas por local**

| | |
|---|---|
| **Proyecto** | Sistema de Inventario para almacenes de accesorios de celulares |
| **Cliente** | My Cell Tecnología |
| **Versión del documento** | 1.2 (MVP) |
| **Fecha** | 26 de noviembre de 2026 |
| **Documento previo** | SRS v1.1 y análisis de la remisión del proveedor (GREEN TECH) |

### Historial de versiones

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | 18/11/2026 | Primera versión del SRS con los 9 módulos. |
| 1.1 | 19/11/2026 | Módulo 1 actualizado por seguridad: inicio de sesión con documento, Dueño Principal y Dueños secundarios con permisos por módulo, código de verificación para restablecer contraseña y aviso de mayoría de edad. Los módulos 2 a 9 no cambian. |
| 1.2 | 26/11/2026 | Módulos 3 y 4: identificación del producto por nombre, cargas por documento del proveedor, productos pendientes hasta tener precio, anulación de cargas y eliminación de productos sin historial. |

---

## Índice

1. [Introducción](#1-introducción)
2. [Descripción general](#2-descripción-general)
3. [Requisitos funcionales por módulo](#3-requisitos-funcionales-por-módulo)
4. [Matriz de permisos por módulo](#4-matriz-de-permisos-por-módulo)
5. [Requisitos no funcionales](#5-requisitos-no-funcionales)
6. [Alcance: qué entra y qué queda fuera](#6-alcance-qué-entra-y-qué-queda-fuera)
7. [Supuestos del documento](#7-supuestos-del-documento)

---

## 1. Introducción

### 1.1 Propósito

Este documento define qué debe hacer el sistema de inventario, módulo por módulo, para que el equipo de desarrollo y el dueño del negocio tengan el mismo entendimiento antes de construirlo.

### 1.2 Alcance del producto

El sistema permite a un negocio con uno o varios locales, que hoy no lleva un inventario formal, controlar **la mercancía que llega y sale** y conocer sus **ganancias y pérdidas por producto y por local**. Es solo de productos: no incluye arriendos, servicios, nómina ni gastos.

> **Enfoque MVP:** se construye como producto mínimo viable: sencillo, de bajo costo y totalmente funcional. Lo que no es indispensable queda para una V2 (ver sección 6).

### 1.3 Definiciones

| Término | Significado |
|---|---|
| **Carga** | Entrega de un proveedor registrada en el sistema e identificada por proveedor y número de documento. |
| **Producto pendiente** | Producto nuevo sin precio. No se puede vender hasta que el Dueño lo complete. |
| **Stock** | Unidades disponibles. Se calcula, nunca se escribe a mano. |
| **Margen** | Porcentaje de ganancia sobre el costo del producto. |
| **Costo promedio** | Costo del producto cuando llegan lotes a precios distintos. |
| **Dañado** | Producto dañado por el personal del local. |
| **Garantía** | Producto con defecto de fábrica, dentro del plazo de garantía. |
| **Faltante** | Diferencia entre lo que dice el sistema y lo contado físicamente. |
| **CSV** | Archivo de lista (Excel) usado para cargar mercancía. |
| **SMTP** | Servicio de correo electrónico por el que el sistema envía avisos. |
| **MVP** | Producto mínimo viable. |
| **Dueño Principal** | Primer Dueño, creado con datos semilla. Tiene todos los permisos, no se puede desactivar y habilita módulos a los demás Dueños. |
| **Dueño secundario** | Dueño creado desde el sistema, con los módulos que le habilite el Principal. |
| **Código de verificación** | Código de 6 dígitos enviado al correo para restablecer la contraseña. |

---

## 2. Descripción general

### 2.1 Roles y jerarquía

Solo dos roles inician sesión: Dueño (Principal o secundario) y Encargado. Los vendedores existen únicamente como un dato dentro del sistema.

```
DUEÑO PRINCIPAL  (semilla; todos los permisos; no se desactiva)
  │
  ├── DUEÑOS SECUNDARIOS  (módulos habilitados por el Principal)
  │
  ├── LOCAL 1 ── ENCARGADO 1  (ventas del día, caja, cambios, dañados)
  │                 └── Vendedores (sin acceso, solo un dato: quién vende o daña)
  │
  └── LOCAL 2 ── ENCARGADO 2  (igual, solo en su local)
                    └── Vendedores (sin acceso, solo un dato)
```

### 2.2 Restricciones de diseño acordadas con el dueño

- El Encargado **solo ve las ventas del día** y lo que vendió. No ve inventario, costos, márgenes ni ganancias.
- Solo el Dueño define precios y márgenes, carga la mercancía y hace el inventario físico.
- Cada 6 meses se hace un inventario físico por local: los faltantes y dañados los paga el Encargado; si todo está bien, recibe el porcentaje pactado.
- Los vendedores no tienen usuario. Se registran para saber **qué vendieron** y **quién dañó qué producto**.
- Los correos de aviso se envían por **SMTP**. No se usa WhatsApp en el MVP.
- El sistema es **solo para mayores de edad**. Al registrar un Encargado o un Dueño se muestra un aviso que debe aceptarse.
- Los productos se identifican solo por su nombre. El MVP prescinde de SKU y de seguimiento por color o serial.

### 2.3 Módulos del sistema

| Módulo | Nombre |
|---|---|
| RF-1 | Acceso, usuarios y roles |
| RF-2 | Locales y vendedores |
| RF-3 | Productos y precios |
| RF-4 | Entradas de mercancía e inventario |
| RF-5 | Ventas y caja |
| RF-6 | Cambios y garantías |
| RF-7 | Dañados, faltantes e inventario físico |
| RF-8 | Reportes |
| RF-9 | Notificaciones y bitácora |

---

## 3. Requisitos funcionales por módulo

Cada módulo tiene su propia lógica, expresada en reglas de negocio (**RN**) y en requisitos funcionales (**RF**). Los requisitos se identifican como **RF-módulo.número**.

---

### RF-1 ACCESO, USUARIOS Y ROLES

**Objetivo:** controlar quién entra al sistema y qué puede hacer cada persona.
**Roles que participan:** Dueño (Principal y secundarios), Encargado.

#### Reglas de negocio del módulo

- **RN-1.1** Solo existen dos roles con acceso: Dueño y Encargado. El rol Dueño tiene dos tipos: Dueño Principal y Dueño secundario. Los vendedores no tienen cuenta.
- **RN-1.2** Cada Encargado pertenece a un solo local y solo puede operar sobre ese local.
- **RN-1.3** Los permisos se validan en el servidor, no solo ocultando botones en pantalla.
- **RN-1.4** Los usuarios nunca se eliminan: se desactivan para conservar su historial. Aplica a Dueños y Encargados.
- **RN-1.5** Se inicia sesión con número de documento (único por usuario) y contraseña.
- **RN-1.6** El Dueño Principal se crea con datos semilla al instalar el sistema. Tiene todos los permisos, no se puede desactivar y es el único que asigna permisos a los Dueños secundarios.
- **RN-1.7** Los permisos de un Dueño secundario se asignan por módulo (RF-1 a RF-9). Un módulo no habilitado no se ve ni se puede operar.
- **RN-1.8** En los demás módulos, «Dueño» se refiere a cualquier Dueño que tenga ese módulo habilitado (el Principal siempre lo tiene).
- **RN-1.9** Solo los Dueños crean, editan, desactivan y reactivan Dueños y Encargados. Un Dueño secundario no puede editar ni desactivar al Principal ni cambiar permisos. El Encargado no edita sus datos; solo cambia su contraseña con la recuperación.
- **RN-1.10** El sistema es solo para mayores de edad. Al registrar un Encargado o un Dueño se muestra un aviso que debe aceptarse; la aceptación queda en bitácora. No se pide tipo de documento. La responsabilidad recae en quien registra.
- **RN-1.11** El código de verificación de 6 dígitos tiene vencimiento corto y límite de intentos (valores por definir; sugerencia: 10 minutos y 5 intentos). El mensaje no revela si el correo existe.

#### Requisitos funcionales

| ID | Requisito | Rol |
|---|---|---|
| RF-1.1 | Inicio de sesión con número de documento y contraseña | Dueño, Encargado |
| RF-1.2 | Cierre de sesión y expiración automática por inactividad | Dueño, Encargado |
| RF-1.3 | Restablecer contraseña: en «¿Olvidaste tu contraseña?» se pide el correo, se envía un código de 6 dígitos (SMTP) y se define la nueva contraseña | Dueño, Encargado |
| RF-1.4 | Registrar Encargados con nombre, apellidos, número de documento y email, asignarlos a un local y mostrar el aviso de mayoría de edad | Dueño |
| RF-1.5 | Cambiar el Encargado de un local: el anterior pierde acceso al instante y el nuevo lo recibe | Dueño |
| RF-1.6 | Desactivar y reactivar Dueños y Encargados conservando todo su historial. El Dueño Principal no se puede desactivar | Dueño |
| RF-1.7 | Mostrar menús, datos y acciones según el rol y los módulos habilitados, y rechazar en el servidor cualquier acción no permitida | Sistema |
| RF-1.8 | Registrar Dueños secundarios con los mismos datos y el aviso de mayoría de edad | Dueño |
| RF-1.9 | Editar los datos de Dueños y Encargados | Dueño |
| RF-1.10 | Asignar y cambiar los módulos habilitados de cada Dueño secundario | Dueño Principal |

> **Texto sugerido del aviso (RN-1.10):** «Este sistema es solo para personas mayores de 18 años. No se permite registrar menores de edad. Al continuar, declaras que la persona que registras es mayor de edad y asumes la responsabilidad por esa declaración.»

---

### RF-2 LOCALES Y VENDEDORES

**Objetivo:** registrar los locales del negocio y las personas que venden en cada uno.
**Roles que participan:** Dueño, Encargado.

#### Reglas de negocio del módulo

- **RN-2.1** El sistema funciona con uno o varios locales.
- **RN-2.2** Cada local tiene su propio inventario, caja y ventas.
- **RN-2.3** El vendedor es solo un dato (nombre y local): no inicia sesión ni tiene permisos.
- **RN-2.4** Un vendedor desactivado conserva su historial de ventas y dañados.

#### Requisitos funcionales

| ID | Requisito | Rol |
|---|---|---|
| RF-2.1 | Crear, editar y desactivar locales | Dueño |
| RF-2.2 | Consultar el listado de locales con su Encargado actual | Dueño |
| RF-2.3 | Registrar vendedores y asociarlos a un local | Dueño |
| RF-2.4 | Editar y desactivar vendedores | Dueño |
| RF-2.5 | Listar los vendedores activos del local al registrar una venta o un producto dañado | Dueño, Encargado |

---

### RF-3 PRODUCTOS Y PRECIOS

**Objetivo:** Mantener el catálogo con su margen, precio, stock mínimo y tiempo de garantía. El costo viene de las entradas de mercancía.
**Roles que participan:** Dueño (completo), Encargado (solo consulta)

#### Reglas de negocio del módulo

- **RN-3.1** Cada producto se identifica por su nombre, que debe ser único. Se compara sin importar mayúsculas, tildes ni espacios de más. No hay SKU.
- **RN-3.2** Precio sugerido = costo promedio × (1 + margen). El Dueño puede ajustar el precio final.
- **RN-3.3** Costo promedio = (stock actual × costo actual + cantidad nueva × costo nuevo) ÷ (stock actual + cantidad nueva). Se calcula por local.
- **RN-3.4** El Encargado solo ve nombre y precio de venta. Nunca costo, margen ni cantidades.
- **RN-3.5** Cada producto tiene un tiempo de garantía en días (puede ser 0). Ese mismo plazo aplica a cambios y garantías.
- **RN-3.6** Un producto nuevo, creado por una carga o a mano, queda pendiente de completar hasta que el Dueño le defina el precio. Un producto pendiente no se puede vender ni aparece en el catálogo del Encargado.
- **RN-3.7** El costo de un producto es el costo de entrada que informa el proveedor (se recalcula como promedio con cada entrada). El Dueño define el margen y el precio de venta.
- **RN-3.8** El color o la forma no se controlan por separado: dos unidades con el mismo nombre son el mismo producto. Si el Dueño quiere controlar una variante, debe escribirla en el nombre. Los equipos con serial se manejan igual: sin seguimiento por serial o IMEI.
- **RN-3.9** Un producto se elimina solo si nunca tuvo movimientos de ningún tipo (ni siquiera de una carga anulada). Si tiene historial, solo se desactiva.
- **RN-3.10** Al cambiar el nombre de un producto, el sistema advierte que las próximas cargas del proveedor deberán usar el nombre nuevo; de lo contrario aparecerán como producto nuevo.

#### Requisitos funcionales

| ID | Requisito | Rol |
|---|---|---|
| RF-3.1 | Crear y editar productos a mano: nombre, categoría, margen, precio, stock mínimo y días de garantía | Dueño |
| RF-3.2 | Gestionar categorías de productos | Dueño |
| RF-3.3 | Definir el margen por categoría o por producto | Dueño |
| RF-3.4 | Calcular y mostrar el precio sugerido, y permitir fijar el precio final | Dueño |
| RF-3.5 | Recalcular el costo promedio automáticamente con cada entrada de mercancía | Sistema |
| RF-3.6 | Consultar el catálogo mostrando solo nombre y precio de venta de los productos con precio (los pendientes no aparecen) | Encargado |
| RF-3.7 | Desactivar productos sin perder su historial | Dueño |
| RF-3.8 | Guardar el historial de cambios de precio y margen (quién, cuándo, valor anterior y nuevo) | Sistema |
| RF-3.9 | Eliminar un producto que nunca tuvo movimientos | Dueño |
| RF-3.10 | Listar los productos pendientes de completar para definirles categoría y precio | Dueño |

---

### RF-4 ENTRADAS DE MERCANCÍA E INVENTARIO

**Objetivo:** Registrar la mercancía que llega a cada local y calcular cuánto hay de cada producto.
**Roles que participan:** Dueño

#### Reglas de negocio del módulo

- **RN-4.1** El stock nunca se escribe a mano. Stock = entradas − salidas (ventas, cambios, dañados, garantías y faltantes) + devoluciones.
- **RN-4.2** Cada entrada pertenece a una carga (un documento del proveedor) y guarda: fecha de registro, local, proveedor, número y fecha del documento, producto, cantidad y costo unitario.
- **RN-4.3** Solo el Dueño carga mercancía y ve el inventario.
- **RN-4.4** La carga por CSV se valida completa antes de guardar: si algo falla, no se guarda nada.
- **RN-4.5** El primer conteo de un local se registra como inventario inicial y es el punto de partida de todos los cálculos.
- **RN-4.6** Una carga se identifica por proveedor + número de documento y no se puede registrar dos veces; para repetirla hay que anular la anterior. Si el documento no trae número, se identifica por proveedor + fecha + total (la suma de las líneas) y el sistema solo avisa de un posible duplicado.
- **RN-4.7** Un producto del archivo se reconoce por su nombre exacto (sin importar mayúsculas, tildes ni espacios de más). Nunca se comparan nombres parecidos: si no coincide exactamente, se trata como producto nuevo y se ve en la vista previa.
- **RN-4.8** El stock y el costo promedio cuentan desde la fecha en que se registra la carga. La fecha del documento se guarda solo como referencia.
- **RN-4.9** Solo el Dueño anula una carga, con un motivo. No se puede anular si algún producto quedaría con stock negativo. La carga anulada queda en el historial y el mismo documento puede volver a cargarse. Los productos que esa carga creó permanecen en el catálogo y el Dueño puede desactivarlos.
- **RN-4.10** El proveedor se identifica por su nombre; si no existe, se crea al registrar la carga.

#### Requisitos funcionales

| ID | Requisito | Rol |
|---|---|---|
| RF-4.1 | Registrar una entrada de mercancía de forma manual: proveedor, número y fecha del documento, local y los productos con cantidad y costo | Dueño |
| RF-4.2 | Descargar una plantilla CSV con las columnas: proveedor, número de documento, fecha del documento, descripción, cantidad, costo unitario y categoría (opcional) | Dueño |
| RF-4.3 | Cargar entradas desde un archivo CSV, eligiendo el local de destino | Dueño |
| RF-4.4 | Validar el CSV: columnas obligatorias, números válidos mayores a 0, descripciones repetidas dentro del archivo y que la carga no esté ya registrada | Sistema |
| RF-4.5 | Mostrar una vista previa antes de confirmar: productos nuevos, existentes, filas con error y la suma de las líneas | Dueño |
| RF-4.6 | Guardar toda la carga en una sola operación (todo o nada) | Sistema |
| RF-4.7 | Crear automáticamente los productos nuevos, en estado pendiente de completar, cuando la descripción no coincide exactamente con un producto existente | Sistema |
| RF-4.8 | Registrar el inventario inicial de un local | Dueño |
| RF-4.9 | Calcular el stock por producto y por local | Sistema |
| RF-4.10 | Consultar el inventario con stock, costo y valor total por local | Dueño |
| RF-4.11 | Consultar el historial de movimientos (kardex) de cada producto | Dueño |
| RF-4.12 | Anular una carga de mercancía indicando el motivo; el sistema recalcula el costo promedio y no la permite si algún producto quedaría con stock negativo | Dueño |
| RF-4.13 | Consultar el listado de cargas: proveedor, número y fecha del documento, local, total y estado (activa o anulada) | Dueño |

**Ejemplo de columnas del CSV:**

```csv
proveedor,numero_documento,fecha_documento,descripcion,cantidad,costo_unitario,categoria
ProvX,REM-001,2026-11-26,Funda iPhone 14 negra,50,4500,Fundas
```

---

### RF-5 VENTAS Y CAJA

**Objetivo:** registrar las ventas, el dinero recibido y el cierre diario de cada local.
**Roles que participan:** Encargado, Dueño.

#### Reglas de negocio del módulo

- **RN-5.1** El vendedor informa y entrega el dinero fuera del sistema; el Encargado registra la venta.
- **RN-5.2** Cada venta guarda el precio de venta, el costo de ese momento y la fecha de vencimiento de la garantía (fecha de venta + días de garantía del producto).
- **RN-5.3** El Encargado no puede editar ni borrar ventas. Las correcciones las hace el Dueño anulando la venta con un motivo.
- **RN-5.4** El Encargado solo ve las ventas del día de su local.
- **RN-5.5** No se puede vender más unidades que el stock; el sistema rechaza la venta sin mostrar la cantidad al Encargado.
- **RN-5.6** Elegir el vendedor al registrar una venta es opcional.
- **RN-5.7** Dinero en caja = ingresos − egresos. Formas de pago: efectivo y transferencia.

#### Requisitos funcionales

| ID | Requisito | Rol |
|---|---|---|
| RF-5.1 | Registrar una venta: productos, cantidades, forma de pago y vendedor (opcional) | Dueño, Encargado |
| RF-5.2 | Asignar a cada venta un número consecutivo para el recibo del cliente | Sistema |
| RF-5.3 | Calcular la fecha de vencimiento de la garantía de cada producto vendido | Sistema |
| RF-5.4 | Validar existencias al vender sin revelar la cantidad al Encargado | Sistema |
| RF-5.5 | Registrar el ingreso a caja de cada venta | Sistema |
| RF-5.6 | Registrar retiros de dinero del Dueño como egreso de caja | Dueño, Encargado |
| RF-5.7 | Consultar las ventas del día y lo vendido (Encargado: su local; Dueño: todos los locales) | Dueño, Encargado |
| RF-5.8 | Consultar ventas por rango de fechas y por local | Dueño |
| RF-5.9 | Buscar una venta anterior por su número y ver solo producto, fecha y si la garantía sigue vigente | Encargado |
| RF-5.10 | Hacer el cierre de caja diario: total esperado, total contado y diferencia | Encargado |
| RF-5.11 | Anular una venta indicando el motivo, devolviendo el stock y ajustando la caja | Dueño |
| RF-5.12 | Consultar el historial de cierres de caja y sus diferencias | Dueño |

---

### RF-6 CAMBIOS Y GARANTÍAS

**Objetivo:** registrar los cambios de producto y las garantías, validando el plazo y manteniendo el inventario correcto.
**Roles que participan:** Encargado, Dueño.

#### Reglas de negocio del módulo

- **RN-6.1** Cambios y garantías comparten el mismo plazo: los días de garantía del producto, contados desde la fecha de venta. Si ya venció, no se puede reclamar.
- **RN-6.2** La venta se identifica por su número de venta.
- **RN-6.3** Cambio con diferencia de precio: si el producto nuevo vale más, el cliente paga y entra a caja; si vale menos, se le devuelve y sale de caja.
- **RN-6.4** El producto devuelto en un cambio vuelve al stock si está en buen estado; si no, se registra como garantía.
- **RN-6.5** El Encargado aprueba los cambios sin autorización previa, pero el Dueño es informado automáticamente (panel y correo).
- **RN-6.6** Garantía = defecto de fábrica. El producto pasa al estado «en garantía», sale del stock disponible y no cuenta como faltante ni como dañado. No se cobra al Encargado.
- **RN-6.7** El reemplazo entregado por una garantía sale del stock sin generar ingreso.
- **RN-6.8** El sistema solo registra y avisa. El reclamo al proveedor se resuelve fuera del sistema.
- **RN-6.9** Cada unidad vendida solo puede cambiarse o entrar en garantía una vez.

#### Requisitos funcionales

| ID | Requisito | Rol |
|---|---|---|
| RF-6.1 | Buscar la venta por número y verificar si el plazo sigue vigente | Dueño, Encargado |
| RF-6.2 | Bloquear el cambio o la garantía con un mensaje claro si el plazo venció | Sistema |
| RF-6.3 | Registrar un cambio: producto devuelto, producto nuevo y estado del producto devuelto | Dueño, Encargado |
| RF-6.4 | Calcular la diferencia de precio y registrar el movimiento de caja correspondiente | Sistema |
| RF-6.5 | Reingresar al stock el producto devuelto en buen estado | Sistema |
| RF-6.6 | Registrar una garantía: producto defectuoso, descripción del defecto y reemplazo entregado (si aplica) | Dueño, Encargado |
| RF-6.7 | Mantener los productos en garantía separados del stock disponible | Sistema |
| RF-6.8 | Descontar del stock el reemplazo de una garantía sin registrar ingreso | Sistema |
| RF-6.9 | Notificar al Dueño cada cambio y cada garantía registrados | Sistema |
| RF-6.10 | Consultar el listado de cambios y garantías por local y fecha | Dueño |

---

### RF-7 DAÑADOS, FALTANTES E INVENTARIO FÍSICO

**Objetivo:** controlar los productos dañados y los faltantes, y registrar el resultado del inventario físico de cada 6 meses.
**Roles que participan:** Encargado, Dueño.

#### Reglas de negocio del módulo

- **RN-7.1** Dañado = producto dañado por el personal. Al registrarlo es **obligatorio** indicar el vendedor responsable.
- **RN-7.2** Un dañado sale del stock y se contabiliza como pérdida al costo del producto.
- **RN-7.3** Las garantías no cuentan como dañados ni como faltantes.
- **RN-7.4** El inventario físico se hace cada 6 meses por local y lo realiza el Dueño. El Encargado solo ve el resultado.
- **RN-7.5** Faltante = stock según el sistema − cantidad contada. Los sobrantes también se muestran.
- **RN-7.6** Los faltantes y dañados los paga el Encargado. Si no hay, no pasa nada y recibe el porcentaje pactado.
- **RN-7.7** El sistema no calcula el porcentaje ni el cobro: el Dueño escribe el monto final.
- **RN-7.8** El Encargado ve el resultado y el monto, sin costos por producto.

#### Requisitos funcionales

| ID | Requisito | Rol |
|---|---|---|
| RF-7.1 | Registrar un producto dañado con el vendedor responsable, la fecha y una observación | Dueño, Encargado |
| RF-7.2 | Descontar el dañado del stock y registrar la pérdida al costo | Sistema |
| RF-7.3 | Notificar al Dueño cada producto dañado, indicando quién lo dañó | Sistema |
| RF-7.4 | Crear un inventario físico para un local | Dueño |
| RF-7.5 | Registrar la cantidad contada de cada producto | Dueño |
| RF-7.6 | Comparar lo contado contra el stock y mostrar faltantes y sobrantes | Sistema |
| RF-7.7 | Mostrar los dañados del periodo con su vendedor responsable | Dueño, Encargado |
| RF-7.8 | Registrar el monto resultante (a cargo del Encargado o a su favor) con una observación | Dueño |
| RF-7.9 | Cerrar el inventario físico y conservarlo en el historial | Dueño |
| RF-7.10 | Consultar el resultado y el monto del inventario de su local | Encargado |
| RF-7.11 | Recordar al Dueño, por panel y correo, cuándo toca el próximo inventario de cada local | Sistema |

---

### RF-8 REPORTES

**Objetivo:** dar al Dueño la visión de stock, ganancias y pérdidas, y al Encargado el resumen de su día.
**Roles que participan:** Dueño, Encargado.

#### Reglas de negocio del módulo

- **RN-8.1** Ganancia = (precio de venta − costo del momento) × cantidad vendida.
- **RN-8.2** Pérdida = (dañados + faltantes) × costo, más las ventas hechas por debajo del costo.
- **RN-8.3** Las garantías no cuentan como pérdida del local en los reportes; se muestran por separado.
- **RN-8.4** El Encargado solo accede a ventas del día y caja de su local.
- **RN-8.5** El costo de cada venta es el del momento en que se vendió, así los reportes pasados no cambian.

#### Requisitos funcionales

| ID | Requisito | Rol |
|---|---|---|
| RF-8.1 | Reporte de stock actual y valor del inventario por local | Dueño |
| RF-8.2 | Reporte de productos con stock por debajo del mínimo | Dueño |
| RF-8.3 | Ganancias y pérdidas por producto en un rango de fechas | Dueño |
| RF-8.4 | Ganancias y pérdidas por local | Dueño |
| RF-8.5 | Comparativo entre locales con el margen real que dejó cada uno | Dueño |
| RF-8.6 | Productos más vendidos y productos sin movimiento | Dueño |
| RF-8.7 | Reporte de dañados por vendedor | Dueño |
| RF-8.8 | Reporte de cambios y garantías | Dueño |
| RF-8.9 | Reporte de ventas del día y de lo vendido | Dueño, Encargado |
| RF-8.10 | Resumen de caja del día y diferencias de cierre | Dueño, Encargado |
| RF-8.11 | Filtrar reportes por fecha, local y producto | Dueño |
| RF-8.12 | Exportar reportes a CSV | Dueño |

---

### RF-9 NOTIFICACIONES Y BITÁCORA

**Objetivo:** avisar al Dueño de lo importante y dejar registro de quién hizo qué.
**Roles que participan:** Dueño, Encargado.

#### Reglas de negocio del módulo

- **RN-9.1** Las alertas llegan al Dueño en un panel dentro del sistema y por correo (SMTP).
- **RN-9.2** El Encargado solo recibe alertas de lo que maneja directamente: caja descuadrada.
- **RN-9.3** En el MVP no se envían mensajes por WhatsApp.
- **RN-9.4** Las acciones importantes quedan en la bitácora con quién, qué, en qué local y cuándo.

#### Requisitos funcionales

| ID | Requisito | Rol |
|---|---|---|
| RF-9.1 | Mostrar un panel de notificaciones con contador de no leídas | Dueño, Encargado |
| RF-9.2 | Marcar notificaciones como leídas | Dueño, Encargado |
| RF-9.3 | Enviar correo SMTP al Dueño cuando: se apruebe un cambio, se registre una garantía, se registre un dañado, la caja no cuadre o haya stock bajo | Sistema |
| RF-9.4 | Alertar cuando una venta se registre por debajo del costo | Sistema |
| RF-9.5 | Alertar al Dueño y al Encargado cuando el cierre de caja tenga diferencia | Sistema |
| RF-9.6 | Configurar el correo destinatario y los datos del servidor SMTP | Dueño |
| RF-9.7 | Registrar en la bitácora las acciones sobre ventas, caja, cambios, garantías, dañados, precios, mercancía, usuarios e inventarios | Sistema |
| RF-9.8 | Consultar la bitácora con filtros por usuario, local, acción y fecha | Dueño |

---

## 4. Matriz de permisos por módulo

| Módulo / acción | Dueño | Encargado |
|---|:---:|:---:|
| RF-1 Gestionar usuarios y roles | ✓ (Principal siempre; secundarios si tienen el módulo) | ✗ |
| RF-1 Asignar módulos a otros Dueños | Solo Dueño Principal | ✗ |
| RF-2 Gestionar locales y vendedores | ✓ | ✗ |
| RF-3 Productos, costos, márgenes y precios | ✓ | Solo nombre y precio |
| RF-4 Cargar mercancía y ver inventario | ✓ | ✗ |
| RF-5 Registrar ventas y manejar caja | ✓ | ✓ |
| RF-5 Ver ventas | Todos los locales | Del día, su local |
| RF-5 Anular ventas | ✓ | ✗ |
| RF-6 Registrar cambios y garantías | ✓ | ✓ |
| RF-7 Registrar dañados | ✓ | ✓ |
| RF-7 Inventario físico (conteo y monto) | ✓ | Solo ve resultado |
| RF-8 Reportes de ganancias, pérdidas y stock | ✓ | ✗ |
| RF-8 Ventas y caja del día | ✓ | ✓ |
| RF-9 Recibir alertas por correo y panel | Todas | Solo caja |
| RF-9 Consultar bitácora | ✓ | ✗ |

---

## 5. Requisitos no funcionales

| ID | Tipo | Requisito |
|---|---|---|
| RNF-1 | Plataforma | Aplicación web que funcione bien en celular y en computador, sin instalar nada. |
| RNF-2 | Seguridad | Contraseñas cifradas, conexión segura (HTTPS), sesiones con vencimiento, códigos de verificación con vencimiento y límite de intentos, y permisos validados en el servidor. |
| RNF-3 | Integridad | Operaciones que afectan stock y caja se guardan completas o no se guardan. Nada con historial se borra: se desactiva o se anula. Solo un producto que nunca tuvo movimientos puede eliminarse. |
| RNF-4 | Rendimiento | Registrar una venta y consultar reportes habituales en menos de 3 segundos. |
| RNF-5 | Respaldo | Copias de seguridad automáticas de la información, como mínimo una diaria. |
| RNF-6 | Usabilidad | Interfaz en español, registrar una venta en pocos pasos, moneda en pesos colombianos y zona horaria de Colombia. |
| RNF-7 | Correo | Envío por SMTP con servidor configurable. Si el correo falla, la alerta igual queda en el panel. |
| RNF-8 | Costo | Tecnologías de código abierto y hosting básico, sin servicios de pago obligatorios. |
| RNF-9 | Mantenibilidad | Un módulo por cada área funcional, para poder crecer a la V2 sin rehacer el sistema. |
| RNF-10 | Escalabilidad | Soportar varios locales sin cambios en el diseño; cada local con su propia información. |

---

## 6. Alcance: qué entra y qué queda fuera

| ✅ Incluido en el MVP | ❌ Fuera del MVP (V2 o descartado) |
|---|---|
| Un solo sistema web para uno o varios locales | Notificaciones por WhatsApp |
| Dos roles: Dueño y Encargado | Transferencias de mercancía entre locales |
| Carga de mercancía manual y por CSV, con inventario inicial | Cálculo automático del porcentaje y cobro de faltantes |
| Ventas, caja y cierre diario | Comisiones o reportes de ventas por vendedor |
| Cambios con diferencia de precio y garantías con plazo automático | Margen mínimo y aprobaciones |
| Dañados con vendedor responsable | Seguimiento de la garantía con el proveedor |
| Inventario físico de 6 meses con monto definido por el Dueño | Facturación electrónica y tienda en línea |
| Reportes de ganancias y pérdidas por local | Arriendos, servicios, gastos y nómina |
| Alertas en panel y por correo SMTP | Acceso al sistema para los vendedores |
| Productos reconocidos por su nombre, sin SKU | Seguimiento por serial o IMEI y control de colores por separado |
| Anular cargas de mercancía | Lectura directa del PDF del proveedor y deudas con proveedores |

---

## 7. Supuestos del documento

- Hay un Dueño Principal (semilla) y puede haber Dueños secundarios. Hay un Encargado activo por local. Las correcciones de ventas las hace solo un Dueño, anulando con motivo.
- El porcentaje del Encargado y el monto de los faltantes los define el Dueño; el sistema solo guarda el monto.
- Los reclamos de garantía a proveedores se gestionan fuera del sistema. Idioma español, moneda en pesos colombianos y zona horaria de Colombia.
- El Dueño transcribe las líneas del documento del proveedor a la plantilla CSV. Si el nombre no coincide, el producto aparece como nuevo en la vista previa y el Dueño puede corregirlo antes de confirmar.
