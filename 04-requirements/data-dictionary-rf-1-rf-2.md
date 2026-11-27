# Diccionario de Datos — MY CELL · Modelo de entidades de RF-1 y RF-2

**RF-1 · Acceso, usuarios, roles y permisos:** `modulo`, `permiso`, `rol`, `rol_permiso`, `usuario`, `usuario_rol`, `usuario_modulo`, `sesion`, `codigo_verificacion` y `aceptacion_aviso`.

**RF-2 · Locales y vendedores:** `local` y `vendedor`.

**Convenciones de clave:** PK = llave primaria · FK = llave foránea · UK = restricción de unicidad.

---

## 1. Tabla: modulo

| Nombre de la tabla: **modulo** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad que almacenará los módulos funcionales del sistema (RF-1 a RF-5, etc.) a los que se agrupan los permisos.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK | id_modulo | SMALLINT | | Identificador único del módulo |
| UK | codigo | VARCHAR | 5 | Código único del módulo (ej. RF-1) |
| | nombre | VARCHAR | 60 | Nombre del módulo |

**Relaciones**

- **Módulo - Permiso (1:N):** Un módulo agrupa muchos permisos y un permiso pertenece a un solo módulo.
- **Módulo - Usuario (Pivote `usuario_modulo`) (N:M):** Un módulo puede estar habilitado para muchos usuarios (dueños secundarios) y un usuario puede estar habilitado en muchos módulos.

---

## 2. Tabla: permiso

| Nombre de la tabla: **permiso** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad que almacenará los permisos individuales que pueden asignarse a los roles.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK | id_permiso | SMALLINT | | Identificador único del permiso |
| UK | codigo | VARCHAR | 40 | Código único del permiso |
| | descripcion | VARCHAR | 120 | Descripción del permiso |
| FK | id_modulo | SMALLINT | | Módulo al que pertenece el permiso (referencia a `modulo`) |

**Relaciones**

- **Permiso - Módulo (N:1):** Un permiso pertenece a un solo módulo y un módulo agrupa muchos permisos.
- **Permiso - Rol (Pivote `rol_permiso`) (N:M):** Un permiso puede asignarse a muchos roles y un rol puede tener muchos permisos.

**Nota:** Los permisos del módulo con código RF-2 son `locales_vendedores.gestionar` y `vendedores.listar_activos`.

---

## 3. Tabla: rol

| Nombre de la tabla: **rol** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad que almacenará los roles que puede desempeñar un usuario dentro del sistema.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK | id_rol | SMALLINT | | Identificador único del rol |
| UK | nombre | VARCHAR | 30 | Nombre único del rol |

**Relaciones**

- **Rol - Permiso (Pivote `rol_permiso`) (N:M):** Un rol puede tener muchos permisos y un permiso puede pertenecer a muchos roles.
- **Rol - Usuario (Pivote `usuario_rol`) (1:N):** Un rol puede asignarse a muchos usuarios; cada usuario tiene un único rol (por la restricción UK sobre `id_usuario` en `usuario_rol`).

---

## 4. Tabla: rol_permiso (pivote)

| Nombre de la tabla: **rol_permiso** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad pivote que almacenará los permisos asignados a cada rol.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK, FK | id_rol | SMALLINT | | Rol al que se asigna el permiso (referencia a `rol`) |
| PK, FK | id_permiso | SMALLINT | | Permiso asignado al rol (referencia a `permiso`) |

**Relaciones**

- **Rol_Permiso - Rol (N:1):** Cada registro pertenece a un solo rol; un rol puede tener muchos registros.
- **Rol_Permiso - Permiso (N:1):** Cada registro pertenece a un solo permiso; un permiso puede aparecer en muchos registros.

**Nota:** La llave primaria es compuesta (`id_rol`, `id_permiso`), lo que evita asignar dos veces el mismo permiso a un rol.

---

## 5. Tabla: usuario

| Nombre de la tabla: **usuario** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad que almacenará la información de los usuarios del sistema.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK | id_usuario | BIGINT | | Identificador único del usuario |
| UK | numero_documento | VARCHAR | 20 | Número de documento de identidad del usuario |
| | nombres | VARCHAR | 80 | Nombres del usuario |
| | apellidos | VARCHAR | 80 | Apellidos del usuario |
| UK | email | VARCHAR | 120 | Correo electrónico del usuario |
| | contrasena_hash | TEXT | | Contraseña del usuario almacenada como hash |
| FK | id_local | BIGINT | | Local al que pertenece el usuario como Encargado (opcional, referencia a `local`, RF-2) |
| | activo | BOOLEAN | | Indica si la cuenta está activa (true) o inactiva (false) |
| | creado_en | TIMESTAMPTZ | | Fecha y hora de creación del usuario |
| FK | creado_por | BIGINT | | Usuario que creó el registro (opcional, autorreferencia a `usuario`) |

**Relaciones**

- **Usuario - Rol (Pivote `usuario_rol`) (N:1):** Un usuario tiene un único rol y un rol puede asignarse a muchos usuarios.
- **Usuario - Módulo (Pivote `usuario_modulo`) (N:M):** Un usuario (dueño secundario) puede estar habilitado en muchos módulos y un módulo puede tener muchos usuarios habilitados.
- **Usuario - Local (N:1, opcional) — asignación de Encargado:** Un usuario puede ser Encargado de un local y un local puede tener muchos usuarios. Cada Encargado pertenece a un local; cada local tiene como máximo un Encargado activo a la vez (regla de negocio).
- **Usuario - Sesión (1:N):** Un usuario puede abrir varias sesiones y una sesión pertenece a un solo usuario.
- **Usuario - Código de verificación (1:N):** Un usuario puede solicitar muchos códigos y un código pertenece a un solo usuario.
- **Usuario - Aceptación de aviso (1:N):** Un usuario puede ser registrado en muchas aceptaciones de aviso (como registrado o como registrador).
- **Usuario - Usuario (1:N, autorreferencia):** Un usuario puede haber creado a muchos usuarios (`creado_por`) y cada usuario fue creado por uno solo.

---

## 6. Tabla: usuario_rol (pivote)

| Nombre de la tabla: **usuario_rol** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad pivote que almacenará el rol asignado a cada usuario.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK, FK, UK | id_usuario | BIGINT | | Usuario al que se asigna el rol (referencia a `usuario`) |
| PK, FK | id_rol | SMALLINT | | Rol asignado al usuario (referencia a `rol`) |
| | asignado_en | TIMESTAMPTZ | | Fecha y hora de asignación del rol |

**Relaciones**

- **Usuario_Rol - Usuario (N:1):** Cada registro pertenece a un solo usuario; por la restricción UK, un usuario tiene un único registro.
- **Usuario_Rol - Rol (N:1):** Cada registro pertenece a un solo rol; un rol puede aparecer en muchos registros.

**Nota:** La restricción UK sobre `id_usuario` garantiza que un usuario tenga un solo rol. Si se requiere que un usuario tenga varios roles (N:M), se debe quitar esa restricción.

---

## 7. Tabla: usuario_modulo (pivote — Dueños secundarios)

| Nombre de la tabla: **usuario_modulo** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad pivote que almacenará los módulos en los que un usuario (dueño secundario) está habilitado.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK, FK | id_usuario | BIGINT | | Usuario habilitado (referencia a `usuario`) |
| PK, FK | id_modulo | SMALLINT | | Módulo en el que se habilita al usuario (referencia a `modulo`) |
| FK | otorgado_por | BIGINT | | Usuario que otorgó la habilitación (referencia a `usuario`) |
| | otorgado_en | TIMESTAMPTZ | | Fecha y hora en que se otorgó la habilitación |

**Relaciones**

- **Usuario_Módulo - Usuario (N:1):** Cada registro pertenece a un usuario habilitado; un usuario puede tener muchos registros.
- **Usuario_Módulo - Módulo (N:1):** Cada registro pertenece a un módulo; un módulo puede tener muchos registros.
- **Usuario_Módulo - Usuario otorgante (N:1):** Cada registro fue otorgado por un usuario (`otorgado_por`).

---

## 8. Tabla: sesion

| Nombre de la tabla: **sesion** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad que almacenará las sesiones abiertas por los usuarios en el sistema.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK | id_sesion | UUID | | Identificador único de la sesión |
| FK | id_usuario | BIGINT | | Usuario dueño de la sesión (referencia a `usuario`) |
| | creada_en | TIMESTAMPTZ | | Fecha y hora de inicio de la sesión |
| | ultima_actividad | TIMESTAMPTZ | | Fecha y hora de la última actividad registrada |
| | expira_en | TIMESTAMPTZ | | Fecha y hora de expiración de la sesión |
| | cerrada_en | TIMESTAMPTZ | | Fecha y hora de cierre de la sesión (opcional) |
| | motivo_cierre | VARCHAR | 20 | Motivo del cierre de la sesión (opcional) |

**Relaciones**

- **Sesión - Usuario (N:1):** Un usuario puede registrar varias sesiones y una sesión pertenece a un solo usuario.

---

## 9. Tabla: codigo_verificacion

| Nombre de la tabla: **codigo_verificacion** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad que almacenará los códigos de verificación solicitados por los usuarios.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK | id_codigo | BIGINT | | Identificador único del código de verificación |
| FK | id_usuario | BIGINT | | Usuario que solicita el código (referencia a `usuario`) |
| | codigo_hash | TEXT | | Código de verificación almacenado como hash |
| | creado_en | TIMESTAMPTZ | | Fecha y hora de creación del código |
| | vence_en | TIMESTAMPTZ | | Fecha y hora de vencimiento del código |
| | intentos | SMALLINT | | Número de intentos de verificación realizados |
| | usado_en | TIMESTAMPTZ | | Fecha y hora en que se usó el código (opcional) |

**Relaciones**

- **Código de verificación - Usuario (N:1):** Un usuario puede solicitar muchos códigos y un código pertenece a un solo usuario.

---

## 10. Tabla: aceptacion_aviso

| Nombre de la tabla: **aceptacion_aviso** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad que almacenará la aceptación del aviso (política de tratamiento de datos) de un usuario registrado por otro usuario.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK | id_aceptacion | BIGINT | | Identificador único de la aceptación |
| FK | id_usuario_registrado | BIGINT | | Usuario que acepta el aviso (referencia a `usuario`) |
| FK | id_usuario_registrador | BIGINT | | Usuario que realizó el registro (referencia a `usuario`) |
| | version_aviso | VARCHAR | 10 | Versión del aviso aceptado |
| | aceptado_en | TIMESTAMPTZ | | Fecha y hora de la aceptación |

**Relaciones**

- **Aceptación de aviso - Usuario registrado (N:1):** Un usuario puede tener muchas aceptaciones y cada aceptación pertenece a un usuario registrado.
- **Aceptación de aviso - Usuario registrador (N:1):** Un usuario puede registrar muchas aceptaciones y cada aceptación fue realizada por un usuario registrador.

---

## 11. Tabla: local (RF-2)

| Nombre de la tabla: **local** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad que almacenará la información de los locales (puntos de venta) del negocio.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK | id_local | BIGINT | | Identificador único del local |
| UK | nombre | VARCHAR | 80 | Nombre único del local |
| | direccion | VARCHAR | 150 | Dirección del local (opcional) |
| | activo | BOOLEAN | | Indica si el local está activo (true) o inactivo (false) |
| | creado_en | TIMESTAMPTZ | | Fecha y hora de creación del local |

**Relaciones**

- **Local - Vendedor (1:N):** Un local tiene muchos vendedores y un vendedor pertenece a un solo local.
- **Local - Usuario (1:N, opcional) — asignación de Encargado:** Un local puede tener usuarios Encargados asignados y un usuario puede ser Encargado de un solo local. Cada local tiene como máximo un Encargado activo a la vez (regla de negocio).

---

## 12. Tabla: vendedor (RF-2)

| Nombre de la tabla: **vendedor** | Fecha de creación: **26/11/2026** |
|---|---|

**Descripción:** Entidad que almacenará los vendedores que atienden en cada local.

| Clave | Campo | Tipo de dato | Tamaño | Descripción |
|---|---|---|---|---|
| PK | id_vendedor | BIGINT | | Identificador único del vendedor |
| | nombre | VARCHAR | 100 | Nombre del vendedor |
| FK | id_local | BIGINT | | Local al que pertenece el vendedor (referencia a `local`) |
| | activo | BOOLEAN | | Indica si el vendedor está activo (true) o inactivo (false) |
| | creado_en | TIMESTAMPTZ | | Fecha y hora de creación del vendedor |

**Relaciones**

- **Vendedor - Local (N:1):** Un vendedor pertenece a un solo local y un local tiene muchos vendedores.