---
name: skills-son-archivos-skill-md
description: Las skills de VIRA AI son archivos SKILL.md en la carpeta skills/, no skills invocables del sistema con la herramienta Skill
metadata:
  type: feedback
---

Las skills de VIRA AI (social-post-generator, brand-voice-enforcer, hashtag-optimizer, etc.) son archivos de instrucción en `skills/<nombre>/SKILL.md`. No son skills registradas del sistema que se puedan invocar con la herramienta Skill del harness.

**Why:** Intentar invocarlas con `Skill("social-post-generator")` produce error "Unknown skill". El flujo correcto es leer el SKILL.md correspondiente y ejecutar su lógica internamente como instrucciones.

**How to apply:** Al iniciar cualquier sesión de producción, leer directamente los archivos SKILL.md relevantes (`skills/social-post-generator/SKILL.md`, etc.) y aplicar su proceso como instrucciones internas, sin intentar invocarlos como herramientas del sistema.
