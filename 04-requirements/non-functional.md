# Requisitos no funcionales

> Fuente: [SRS del Sistema de Inventario MVP, versión 1.2](srs-sistema-inventario-mvp-mycell.pdf) · 26 de noviembre de 2026

Los IDs corresponden a la sección 5 del SRS (pp. 13–14). La última columna propone cómo verificar cada requisito durante QA.

| ID | Tipo | Requisito | Cómo se verifica |
| --- | --- | --- | --- |
| RNF-1 | Plataforma | Aplicación web utilizable en celular y computador, sin instalación. | Abrir la aplicación en ambos tipos de dispositivo y ejecutar los flujos principales desde el navegador. |
| RNF-2 | Seguridad | Contraseñas protegidas mediante cifrado según la redacción del SRS, HTTPS, sesiones con vencimiento, códigos de verificación con vencimiento y límite de intentos, y permisos validados por el servidor. | Revisar credenciales y HTTPS. Probar expiración de sesiones y códigos, límite de intentos y solicitudes con rol, local o módulo no autorizado. |
| RNF-3 | Integridad | Las operaciones de stock y caja se guardan completas o se revierten. Los registros con historial se desactivan o anulan. Solo se pueden eliminar productos que nunca tuvieron movimientos. | Simular un fallo parcial y comprobar la reversión. Verificar que un producto con movimientos, incluso de una carga anulada, no se pueda eliminar. |
| RNF-4 | Rendimiento | Registrar una venta y consultar reportes habituales en menos de 3 segundos. | Medir ambos flujos. El SRS deja por definir los reportes de prueba, el volumen de datos y el perfil de carga. |
| RNF-5 | Respaldo | Crear copias de seguridad automáticas al menos una vez al día. | Revisar la programación y los registros de ejecución para comprobar la frecuencia diaria. |
| RNF-6 | Usabilidad | Interfaz en español, registro de venta en pocos pasos, moneda en pesos colombianos y zona horaria de Colombia. | Recorrer el flujo de venta y revisar textos, importes y fechas. El SRS deja por definir el máximo de pasos. |
| RNF-7 | Correo | Enviar correo por SMTP mediante un servidor configurable y conservar la alerta en el panel cuando el envío falle. | Cambiar la configuración SMTP y verificar un envío. Simular un fallo y comprobar que la alerta siga visible en el panel. |
| RNF-8 | Costo | Usar tecnologías de código abierto y hosting básico, sin servicios de pago obligatorios. | Revisar licencias, dependencias y requisitos del alojamiento. |
| RNF-9 | Mantenibilidad | Organizar el sistema en un módulo por área funcional para ampliar a la V2 sin rehacerlo. | Revisar el mapa de módulos y su correspondencia con las áreas funcionales. |
| RNF-10 | Escalabilidad | Admitir varios locales sin rediseño, con información propia por local. | Agregar otro local con el mismo despliegue y verificar la separación de inventario, caja y ventas. |
