# Modelador de Diagramas de Casos de Uso

## Objetivo

Generar diagramas de casos de uso del Sistema de Turnos Médicos utilizando PlantUML, a partir del análisis de los requerimientos definidos en la Actividad Obligatoria N°1.

---

## Prompt utilizado

Se utilizó Copilot en modo agente dentro de VS Code con el siguiente enfoque:

```
Generar diagramas de casos de uso en PlantUML para un sistema de turnos médicos, considerando actores como Paciente, Secretaria y Médico. Incluir relaciones de asociación, <<include>> y <<extend>> cuando corresponda.
```

---

## Archivos de contexto utilizados

- anexos/introduccion.md
- Definiciones de casos de uso de la Actividad N°1

---

## Resultado generado por IA

Copilot generó estructuras base de diagramas de casos de uso, incluyendo actores y relaciones iniciales.

---

## Ajustes y correcciones realizadas

Se realizaron modificaciones manuales sobre el contenido generado por IA:

- Se corrigieron actores mal asignados
- Se agregaron relaciones <<include>> para reflejar dependencias obligatorias
- Se incorporaron relaciones <<extend>> en casos opcionales
- Se mejoró la división de responsabilidades entre casos de uso
- Se ajustaron nombres para mayor claridad semántica
- Se agregó el límite del sistema (rectangle) para mayor claridad conceptual

---

## Reflexión

El uso de Copilot permitió acelerar la generación inicial de los diagramas, pero fue necesario realizar ajustes para asegurar la coherencia con el dominio del problema y los requerimientos definidos.

Esto evidencia que la IA es una herramienta de apoyo, pero requiere validación y corrección por parte del desarrollador.