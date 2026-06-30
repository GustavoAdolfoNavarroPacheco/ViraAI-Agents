---
name: performance-analyst
description: Analiza el historial acumulado en context/memory-log.md, detecta patrones de qué contenido funciona mejor (hooks, pilares, formatos, avatares) y propone ajustes concretos a la estrategia de Campuslands AI Academy. Usa esta skill cuando el usuario pida "analiza nuestro desempeño", "qué ha funcionado mejor", "ajustemos la estrategia con base en los datos", o periódicamente (ej. fin de mes) si context/memory-log.md ya tiene suficientes datos acumulados.
---

# Performance Analyst

## Función
Convertir el historial de sesiones y feedback (`context/memory-log.md`) en insights accionables: qué tipo de hook, pilar, formato o avatar ha tenido mejor recepción, y qué ajustar.

## Cuándo se activa
- "¿Qué ha funcionado mejor este mes?"
- "Ajustemos la estrategia con base en lo que sabemos"
- Sugerido proactivamente si `context/memory-log.md` acumula varias sesiones con feedback registrado y no se ha hecho un análisis reciente.

## Pre-requisito
Esta skill SOLO aporta valor real si `context/memory-log.md` tiene datos suficientes (mínimo varias sesiones con feedback explícito del equipo). Si el log está vacío o tiene muy poca información, decirlo claramente y sugerir seguir registrando con `memory-manager` antes de analizar.

## Proceso
1. Lee `context/memory-log.md` completo (vía `memory-manager`).
2. Agrupa patrones por categoría:
   - Tipos de hook que recibieron feedback positivo vs. negativo.
   - Pilares de contenido con mejor recepción reportada.
   - Formatos (post/carrusel/reel) con mejor desempeño percibido.
   - Avatares para los que el contenido resonó más.
3. Identifica 2–4 patrones claros (no sobre-interpretar con pocos datos — ser honesto sobre el nivel de certeza).
4. Propone ajustes concretos: "Considerar aumentar % de [pilar]", "Replicar el estilo de hook de [tipo] en más piezas", "Revisar el enfoque para [avatar] porque ha tenido feedback mixto".
5. Sugiere si algún ajuste debería reflejarse en `content-strategy.md` o `voice-type.md` (cambios estructurales, no solo tácticos).

## Output esperado
```
ANÁLISIS DE DESEMPEÑO — [periodo analizado]

Patrones detectados:
1. [patrón] — basado en [N] sesiones/piezas
2. ...

Recomendaciones concretas:
1. ...
2. ...

Nivel de confianza: [bajo/medio/alto, según volumen de datos disponible]
```

## Restricciones
- Nunca presentar conclusiones con más confianza de la que los datos disponibles soportan.
- No inventar métricas cuantitativas (CTR, alcance) si no fueron registradas explícitamente en `context/memory-log.md` — trabajar solo con lo que el equipo reportó.
- Ser honesto cuando los datos son insuficientes para sacar conclusiones firmes.

## Conexión con otras skills
Depende de `memory-manager` para los datos · sus recomendaciones alimentan ajustes en `content-calendar-planner`, `content-strategy.md` y `voice-type.md`.

