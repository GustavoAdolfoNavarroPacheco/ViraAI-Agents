---
name: memory-manager
description: Lee y actualiza context/memory-log.md al inicio y al final de cada sesión de VIRA AI, registrando piezas generadas, hooks efectivos, tendencias detectadas y feedback del equipo de marketing. La encuesta de satisfacción se ejecuta después de document-exporter, cuando el entregable ya quedó guardado y el usuario resolvió el formato adicional.
---

# Memory Manager

## Función
Mantener la continuidad de aprendizaje de VIRA AI entre sesiones, mediante lectura y escritura disciplinada de `context/memory-log.md`.

## Cuándo se activa
- **Al inicio de sesión**: leer `context/memory-log.md` para recuperar hooks que funcionaron, tendencias ya usadas (evitar repetirlas), y feedback pendiente.
- **Durante la sesión**: cuando el usuario da feedback explícito sobre una pieza generada (positivo o negativo).
- **Al final de sesión**: resumir y guardar lo relevante de la sesión actual.

## Estructura de context/memory-log.md

Cada entrada DEBE ir en su propia sección con encabezado fechado y numerado. Nunca agregar texto suelto al final del archivo sin sección.

```
## Sesión S## — [YYYY-MM-DD]

- Piezas generadas: [resumen breve, no el copy completo]
- Hooks que el equipo marcó como efectivos: [...]
- Hooks o enfoques descartados: [...]
- Tendencias detectadas y ya usadas: [...]
- Feedback del equipo: [...]
- Notas para la próxima sesión: [...]
```

## Proceso de lectura (inicio de sesión)
1. Abre `context/memory-log.md`. Esta es la memoria institucional canonica del proyecto.
2. Extrae: tendencias ya usadas recientemente (para no repetir en `trend-researcher`), hooks de alto desempeño (para reutilizar patrones en `social-post-generator`/`script-writer`), y cualquier corrección de tono pedida por el equipo (para reforzar en `brand-voice-enforcer`).
3. Si es la primera sesión o el log está vacío, indícalo y procede sin contexto previo.

## Proceso de escritura — flujo de 8 pasos (fin de sesión)

El almacenamiento ocurre ÚNICAMENTE en el paso 8, después de que el usuario haya respondido la encuesta (paso 7). El orden es fijo:

| Paso | Quién actúa | Qué hace |
|---|---|---|
| 1 | Usuario | Envía la solicitud |
| 2 | VIRA | Genera entregable + `brand-voice-enforcer` |
| 3 | VIRA | `document-exporter`: guarda `.md` y pregunta formato adicional |
| 4 | Usuario | Responde la pregunta de formato |
| 5 | VIRA | Entrega el archivo en el formato pedido y confirma la ruta. **No mostrar encuesta hasta aquí.** |
| 6 | VIRA | Muestra la encuesta de calificación (1–5) |
| 7 | Usuario | Califica y opcionalmente comenta |
| 8 | VIRA | Procesa la calificación y registra en `context/memory-log.md` |

### Cómo ejecutar el paso 8
1. Resume en 3–6 líneas qué se produjo en la sesión (sin copiar el contenido completo, solo temas y formatos).
2. Registra la calificación y el comentario del usuario textualmente.
3. Agrega la entrada nueva al final del log bajo `## Sesión S## — [YYYY-MM-DD]`, sin borrar el historial previo.
4. Confirma al usuario que el aprendizaje quedó guardado.

---

## Encuesta de Retroalimentación — Paso 6 obligatorio

Solo mostrar después de confirmar la entrega del archivo (paso 5 completado):

---
**¿Cómo calificarías el contenido de esta sesión?**

`5` · Excelente — exactamente lo que necesitaba, lo publico tal cual
`4` · Muy bueno — pequeños ajustes de forma, pero el fondo es sólido
`3` · Aceptable — sirve como base pero requiere cambios importantes
`2` · Regular — no capturó bien lo que buscaba
`1` · No funcionó — hay que replantear el enfoque

*(Opcional)* ¿Qué mejorarías o qué faltó?

---

### Cómo procesar la respuesta

**Si la respuesta es 4 o 5 (positiva):**
- Registrar en `context/memory-log.md` bajo `### Retroalimentación recibida`:
  ```
  - Calificación: [X]/5
  - Detalle: [comentario del usuario si lo dio]
  - Acción: Replicar enfoque [hook / tono / formato / estructura] en sesiones futuras.
  ```
- Si el usuario mencionó algo específico que funcionó, añadirlo al **Banco de Hooks con Mejor Rendimiento** o a **Formatos que Funcionan Mejor por Avatar** según corresponda.

**Si la respuesta es 3 (neutral):**
- Registrar en `context/memory-log.md`:
  ```
  - Calificación: 3/5
  - Detalle: [comentario del usuario]
  - Ajuste para próxima sesión: [inferir del comentario qué cambiar — tono, estructura, avatar, hook, longitud]
  ```

**Si la respuesta es 1 o 2 (negativa):**
- Registrar en `context/memory-log.md`:
  ```
  - Calificación: [X]/5
  - Detalle: [comentario del usuario]
  - Problema detectado: [qué falló — tono fuera de marca, ángulo equivocado, formato inadecuado, datos incorrectos, etc.]
  - Ajuste OBLIGATORIO para próxima sesión: [instrucción concreta y accionable para VIRA AI]
  ```
- Adicionalmente, agregar una entrada en la tabla **Feedback del Equipo** de `context/memory-log.md`:
  ```
  | [fecha] | [calificación + comentario] | [ajuste a aplicar en siguiente sesión] |
  ```
- Ofrecer al usuario regenerar el contenido en la misma sesión con el ajuste aplicado:
  > “Entendido. ¿Quieres que lo regenere ahora con ese ajuste, o lo dejamos como aprendizaje para la próxima sesión?”

### Cuándo omitir la encuesta

- Si el usuario ya dio feedback explícito durante la sesión (“esto no me gustó”, “perfecto, así”), procesar ese feedback directamente sin mostrar la encuesta — el usuario ya respondió.
- Si la sesión fue de tipo analítico (VIRA Memory/Analytics) o de validación (VIRA QA) en lugar de generación de contenido, adaptar las preguntas al tipo de entregable o simplificar a: “¿El análisis / reporte fue útil? (sí / parcialmente / no)”.

---

## Restricciones
- Nunca borrar o sobrescribir entradas anteriores del log — solo agregar.
- No registrar datos sensibles o personales de usuarios/Campers reales sin anonimizar.
- La persistencia real del proyecto es `context/memory-log.md`; no usar borradores en chat como sustituto cuando el filesystem esté disponible.

## Conexión con otras skills
Alimenta a `trend-researcher` (evitar repetir tendencias) · `performance-analyst` (analiza el histórico acumulado) · es invocada implícitamente al cierre de cualquier sesión de producción de contenido.
