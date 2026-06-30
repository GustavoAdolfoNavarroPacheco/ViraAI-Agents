---
name: quality-patrones-desviacion
description: Patrones de desviación de marca recurrentes que QA debe vigilar en piezas de Campuslands IA Academy
metadata:
  type: project
---

Patrones de desviación recurrentes a vigilar en toda validación de contenido de IA Academy.

**Why:** Se repiten en distintas fuentes y canales; documentarlos acelera la detección y evita reincidencia. Base: histórico memory-log (S1–S20) y caso de validación del freelancer con claim "100% de graduados consigue trabajo en menos de 30 días".

**How to apply:** Revisar específicamente estos focos en cada pieza:

1. **Empleabilidad absoluta (DESVIACIÓN MAYOR → rechazo).** Frases tipo "100% consigue empleo", "trabajo garantizado", "en X días". Regla: nunca prometer empleabilidad de forma absoluta no verificable. Reemplazo válido: lenguaje de oportunidad/preparación ("fórmate para las oportunidades que ya están llegando").

2. **Campos de datos inventados o sin confirmar (MAYOR).** Riesgo alto en cifras, % de adopción, número de empresas/egresados formados, cupos limitados, precios y fechas/horas de masterclass. Antecedentes: S14 dejó un campo `[X]` (número de empresas formadas) pendiente de dato real; S20 advierte definir período/fecha y confirmar evento antes de insertar flujo. Regla: solo datos verificados en campuslands.md; los faltantes se dejan como placeholder marcado, nunca se inventan.

3. **Urgencia falsa / cupos no confirmados (MAYOR si es manipulador).** Cuidar "últimos cupos", contadores, escasez no verídica.

4. **Repetición de ángulo B2B (MENOR, coherencia).** Ángulos LinkedIn Empresas ya usados: ROI/productividad (S4), retención de talento (S11), soberanía tecnológica (S13). Señalar si una pieza nueva repite uno sin rotación.

5. **"Formar sin migrar".** Verificar que se conecte cuando el tema lo permite; mejor integrado de forma natural (ej. "no tienes que irte a otra ciudad") que como slogan pegado.
