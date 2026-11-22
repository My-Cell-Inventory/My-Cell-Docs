# Convenciones ágiles

El [backlog](../03-product/product-backlog.md) agrupa el MVP por capacidades. Usa los IDs RF, RN y RNF del [SRS 1.1](../04-requirements/srs-sistema-inventario-mvp-mycell.pdf) en historias, criterios de aceptación y evidencias.

## Flujo propuesto

1. Refinar la historia con la persona responsable de producto. Delimitar rol, local, acción, resultado y errores.
2. Revisar la [Definition of Ready](definition-of-ready.md) antes de planearla.
3. Trabajar desde una [rama hija](git-conventions.md) y relacionar el PR con la historia y los requisitos.
4. Validar con datos ficticios. Registrar ambiente, versión y resultados en [evidencias](../11-quality/evidence/README.md).
5. Cerrar con la [Definition of Done](definition-of-done.md).

Formato sugerido para historias: `HU-<número>`. Usa criterios «Dado / Cuando / Entonces» cuando ayuden a reproducir el caso. La asignación y el estado de cada historia se registrarán en el tracker que adopte el equipo.
