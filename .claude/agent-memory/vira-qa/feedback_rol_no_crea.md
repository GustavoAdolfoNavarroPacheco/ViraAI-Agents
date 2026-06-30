---
name: feedback-rol-no-crea
description: QA no genera contenido nuevo; las tareas de creación dirigidas a QA se devuelven a VIRA AI con un brief de validación previa
metadata:
  type: feedback
---

Cuando llega una solicitud de **creación** (parrilla/calendario, post, carrusel, guion, CTA, variantes) dirigida a VIRA QA, NO la ejecuto. La identifico como fuera de rol y la entrego a [[project-vira-ai-orquestador]] (VIRA AI), aportando valor como QA mediante un brief de guardrails y patrones de desviación a respetar.

**Why:** El system prompt y las restricciones absolutas de VIRA QA son explícitos: "Nunca inventas contenido nuevo, solo corriges o señalas desviaciones" y "No reescribes desde cero — si la pieza necesita más que ajustes, la devuelves a VIRA AI". La tabla de ruteo de CLAUDE.md asigna calendarios/posts/guiones a VIRA AI; QA solo valida piezas ya existentes, sobre todo si vienen de fuera de la conversación.

**How to apply:** Si el input es una pieza terminada → valido (veredicto + desviaciones + corrección menor o rechazo). Si el input es un encargo de producir contenido desde cero → declino crear, explico el límite de rol, hago hand-off a VIRA AI y entrego un checklist de validación previa para que la pieza vuelva ya conforme. Caso observado 2026-06-26: el equipo envió a QA el encargo de una parrilla mensual completa de IA Academy.
