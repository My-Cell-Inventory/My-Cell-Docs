# Git conventions

## Ramas padre

| Rama | Uso |
| --- | --- |
| `develop` | Integración de documentación en curso |
| `qa` | Validación documental y evidencias |
| `main` | Documentación estable |

## Ramas hijas y pull requests

| Trabajo | Base | Rama hija | Destino del PR |
| --- | --- | --- | --- |
| Estructura documental | `develop` | `docs/estructura-documental` | `develop` |
| Documentación de una HU | `develop` | `hu-<numero>-dev` | `develop` |
| Validación de una HU y evidencias | `qa` | `hu-<numero>-qa` | `qa` |
| Publicación de una iteración | `main` | `release/<iteracion>` | `main` |

1. Actualiza la rama padre desde `origin` y crea la hija desde esa base.
2. Publica los cambios en la hija y abre un PR hacia la rama padre indicada.
3. Para pasar trabajo de `develop` a `qa`, incorpora en la hija de QA los commits aprobados de `develop` y agrega las evidencias en [`11-quality/evidence/`](../11-quality/evidence/README.md).
4. Para publicar una iteración, incorpora en la hija de release los commits validados en `qa` y abre el PR hacia `main`.
5. Tras la revisión y la integración, elimina la hija si ya cerró su ciclo.

Las ramas padre reciben cambios mediante PR. Evita el push directo. Usa commits como `docs(11-quality): add validation evidence` y registra en el PR la HU o el cambio que se valida.
