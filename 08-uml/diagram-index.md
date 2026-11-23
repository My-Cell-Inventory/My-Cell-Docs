# Orden de elaboración de diagramas

Este plan define la secuencia para modelar el comportamiento y los datos del MVP de MY CELL. Parte de los [requisitos funcionales](../04-requirements/functional.md).

| Orden | Entregable | Propósito en esta etapa |
| --- | --- | --- |
| 1 | Casos de uso | Identificar quién hace qué a partir de los RF. Ubicar las acciones del Dueño y el Encargado, con el alcance por local. Los demás diagramas parten de estos casos. |
| 2 | Tabla de priorización | Ordenar los casos de uso por prioridad y dependencias. Usar ese orden para decidir qué construir y diagramar primero. |
| 3 | Diagramas de actividad | Mostrar el flujo paso a paso, con decisiones y excepciones, de los casos que tienen lógica de negocio. Por ejemplo, validar una venta según el stock disponible. |
| 4 | Diagramas de secuencia | Mostrar quién llama a quién y en qué orden durante un caso de uso. Incluir interfaz, servidor, base de datos y correo cuando participen. |
| 5 | Diagramas de transición de estados | Mostrar los estados, transiciones y condiciones de elementos con ciclo de vida, como la venta, la garantía y el inventario físico. |
| 6 | Diagrama de dominio | Identificar los conceptos de negocio y sus relaciones a partir de los flujos revisados. Incluir local, producto, venta, caja y movimientos de inventario. |
| 7 | Diagrama de clases | Detallar las clases a partir del modelo de dominio. Definir responsabilidades, atributos, operaciones y relaciones según los casos de uso. |
| 8 | MER y diagrama ER | Definir el modelo entidad-relación (MER) y representarlo en el diagrama ER. Mostrar las entidades persistentes, sus claves, relaciones y cardinalidades. |

Al elaborar cada entregable, indica de qué caso de uso o RF parte. Guarda los archivos en las carpetas de [fuentes editables](diagrams/source/README.md) y [exportaciones](diagrams/exports/README.md), según corresponda.

## Diagramas registrados

| Diagrama | Tipo | Referencia |
| --- | --- | --- |
| Diagramas de casos de uso del MVP de MY CELL | Casos de uso | [Ver los diagramas de casos de uso en Google Drive](https://drive.google.com/file/d/1crknSn2f4_yJcCooH0gF7Rk925qNBy9K/view?usp=sharing) |
| Tablero de priorización de MY CELL | Priorización de casos de uso | [Abrir tablero en Claude](https://claude.ai/artifact/CyW6F5KXKASgzYUtaJHeCS) · [Archivo HTML](diagrams/exports/tablero-priorizacion-my-cell.html) |
| Diagrama de actividades de MY CELL | Actividad | [Ver el diagrama en Google Drive](https://drive.google.com/file/d/1xk0R3M2os1-ztKDA7OPRayBu6HVXVKGF/view?usp=sharing) |
| Diagrama de secuencia de MY CELL | Secuencia | [Ver el diagrama en Google Drive](https://drive.google.com/file/d/1OdxisakzvcdQj-t7NMnDvZRUGsuGGV8F/view?usp=sharing) |
| Diagrama de transición de estados de MY CELL | Transición de estados | [Ver el diagrama en Google Drive](https://drive.google.com/file/d/1WYFgxKDreh5wzRbe61E3TENfvQ3RA3EG/view?usp=sharing) |
