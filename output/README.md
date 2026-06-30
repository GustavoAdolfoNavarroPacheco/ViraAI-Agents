# Output

Carpeta de entregables finales y reportes generados por VIRA AI.

## Convencion

Cada entregable debe estar en una carpeta propia:

```text
output/[YYYY-MM-DD]_[tipo]_[descripcion-clara]/contenido.md
```

## Excepciones

```text
output/videos_output/
```

Contiene videos finales exportados. No debe contener renders intermedios.

## No Guardar Aqui

- Scripts internos reutilizables.
- Archivos temporales.
- Segmentos de video `seg_*.mp4`.
- Bases de render como `base.mp4`.
- Versiones obsoletas si ya existe una entrega final aprobada.

Ese material debe ir en `tools/`, `videos/` o `archive/` segun corresponda.

