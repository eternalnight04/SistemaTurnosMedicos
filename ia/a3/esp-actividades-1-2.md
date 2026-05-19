# Especialista de Actividades 

## Objetivo

Generar diagramas de actividades utilizando PlantUML, a partir del análisis de los casos de uso 01 y 02 previamente definidos.

---

## Prompt utilizado

Se utilizó Copilot en modo agente dentro de VS Code con el siguiente enfoque:

```
Necesito que actúes como analista UML senior y generes 2 diagramas de actividades UML basados EXCLUSIVAMENTE en el contexto y documentación proporcionada del sistema.

Objetivo

Diseñar los diagramas de actividades correspondientes a los siguientes casos de uso:

Crear Turno
Reprogramar Turno
Reglas obligatorias
Debes utilizar TODO el contexto proporcionado previamente.
Los diagramas deben reflejar fielmente:
los actores definidos en el diagrama de casos de uso,
los pasos del escenario principal,
flujos alternativos,
validaciones,
decisiones,
confirmaciones,
errores y excepciones si existen.
Requisitos UML
Utilizar notación UML estándar.
Cada actor o participante debe representarse mediante swimlanes/carriles.
Las actividades deben ubicarse en el carril correspondiente según quién ejecuta la acción.
Incluir:
nodo inicial,
nodo final,
decisiones (if/else),
forks/joins si corresponde,
transiciones correctamente etiquetadas.
Restricciones importantes
NO inventar actores ni pasos que no existan en el contexto.
NO resumir procesos.
NO simplificar escenarios.
Debes respetar exactamente la lógica del caso de uso original.
Si falta información, indicarlo explícitamente antes de generar el diagrama.
Formato requerido

Generar:

Explicación breve del flujo.
Diagrama en formato:
PlantUML
y además versión Mermaid (si es posible).
Estructura esperada
Caso de Uso 1 — Crear Turno
Objetivo
Actores
Flujo principal
Flujos alternativos
Código PlantUML
Código Mermaid
Caso de Uso 2 — Reprogramar Turno
Objetivo
Actores
Flujo principal
Flujos alternativos
Código PlantUML
Código Mermaid
Muy importante

Los pasos del escenario y los actores del diagrama de casos de uso deben reflejarse fielmente en los carriles y actividades del diagrama de actividades.
No omitir interacciones entre usuario, sistema y servicios externos si aparecen en el contexto.
```

---

## Archivos de contexto utilizados

- `diagramas/02-casos-de-uso`
- `diagramas/02-casos-de-uso/02-caso-uso-crear-turno.puml`
- `diagramas/02-casos-de-uso/02-caso-uso-crear-turno.png`
- `diagramas/02-casos-de-uso/02-caso-uso-reprogramar-turno.puml`
- `diagramas/02-casos-de-uso/02-caso-uso-reprogramar-turno.png`
- `diagramas/03-escenarios-casos-de-uso`

---

## Resultado generado por IA

Copilot generó diagramas de actividades con el contexto proporcionado.

```
Caso de Uso 1 — Crear Turno
Objetivo
Registrar un nuevo turno médico a nombre de un paciente, validando disponibilidad y evitando superposiciones, y notificar al paciente.

Actores
Secretaria
Paciente
Sistema (participante interno)
Flujo principal
Secretaria selecciona Nuevo Turno.
Busca o selecciona al paciente.
Si el paciente no existe, lo da de alta antes de continuar.
Selecciona profesional, fecha, hora y tipo de consulta.
Sistema valida que el horario esté dentro de la disponibilidad del profesional.
Sistema verifica que no exista superposición con otro turno.
Si pasa las validaciones, sistema registra el turno como Confirmado.
Sistema guarda el evento en el historial.
Sistema notifica al paciente.
Secretaria visualiza la confirmación y el turno en la agenda.
Flujos alternativos
FA-01A: Si el horario está fuera de disponibilidad, el sistema informa el conflicto y no registra el turno.
FA-01B: Si el horario ya está ocupado, el sistema advierte la superposición y bloquea el registro. La secretaria puede elegir otro horario o solicitar sobreturno.
FA-01C: Si el paciente no existe, la secretaria da de alta al paciente antes de continuar.
```

```
Caso de Uso 2 — Reprogramar Turno
Objetivo
Modificar la fecha/hora de un turno existente, validar el nuevo horario, actualizar la agenda, registrar la reprogramación y notificar al paciente.

Actores
Secretaria
Paciente
Sistema (participante interno)
Flujo principal
Paciente solicita cambio de horario.
Secretaria busca y selecciona el turno a reprogramar.
Secretaria ingresa nueva fecha/hora.
Sistema valida que el nuevo horario esté dentro de la disponibilidad del profesional.
Sistema verifica que no haya superposición con otro turno.
Si el horario es válido, sistema actualiza el turno con el nuevo horario.
Sistema registra la reprogramación en el historial.
Sistema notifica al paciente.
Flujos alternativos
FA-02A: Si el nuevo horario está ocupado, el sistema informa el conflicto y no realiza el cambio. También sugiere horarios alternativos.
FA-02B: Si el turno está cancelado o atendido, el sistema informa que no puede reprogramarse.
FA-02C: Si falla la notificación, el turno se reprograma igual y deja marcada la notificación para gestión manual.
```
---

## Reflexión

El uso de Copilot permitió acelerar la generación inicial de los diagramas de actividades. Se realizó una verificación del contenido para asegurar que sea coherente y cumpla con la consinga.

Esto supone que la IA es una herramienta de apoyo muy útil, pero requiere validación y corrección por parte del desarrollador.