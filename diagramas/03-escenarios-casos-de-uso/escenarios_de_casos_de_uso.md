# Escenarios de Casos de Uso - Índice

## Descripción

Este directorio contiene los escenarios detallados de los 5 casos de uso principales del Sistema de Turnos Médicos. Cada escenario describe un flujo específico de interacción entre actores, precondiciones, pasos del proceso y postcondiciones.

---

## Escenarios Documentados

### 1. **Crear Turno - Flujo Principal**
- **Archivo:** [03-crear-turno-flujo-principal.md](03-crear-turno-flujo-principal.md)
- **ID:** CU-01-FP
- **Descripción:** Crear un turno de control médico exitosamente
- **Actores principales:** Secretaria, Paciente, Sistema
- **Resultado:** Turno confirmado registrado en la agenda del médico

### 2. **Reprogramar Turno - Flujo Alterno**
- **Archivo:** [03-reprogramar-turno-flujo-alterno.md](03-reprogramar-turno-flujo-alterno.md)
- **ID:** CU-02-FA
- **Descripción:** Reprogramar un turno cuando hay conflicto de horario
- **Actores principales:** Secretaria, Paciente
- **Desafío:** Manejo de conflictos de superposición de horarios
- **Resultado:** Turno reprogramado a horario disponible

### 3. **Cancelar Turno - Flujo Principal**
- **Archivo:** [03-cancelar-turno-flujo-principal.md](03-cancelar-turno-flujo-principal.md)
- **ID:** CU-03-FP
- **Descripción:** Cancelar un turno a solicitud del paciente
- **Actores principales:** Secretaria, Paciente
- **Validaciones:** Confirmación de cancelación, cambio de estado
- **Resultado:** Turno cancelado, horario liberado, paciente notificado

### 4. **Autorizar Sobreturno - Flujo Principal**
- **Archivo:** [03-autorizar-sobreturno-flujo-principal.md](03-autorizar-sobreturno-flujo-principal.md)
- **ID:** CU-04-FP
- **Descripción:** Agregar un sobreturno autorizado manualmente por el médico
- **Actores principales:** Secretaria, Médico, Paciente
- **Restricción crítica:** Solo con autorización explícita del médico presente
- **Resultado:** Sobreturno registrado con indicador especial

### 5. **Registrar Llegada del Paciente - Flujo Principal**
- **Archivo:** [03-registrar-llegada-flujo-principal.md](03-registrar-llegada-flujo-principal.md)
- **ID:** CU-05-FP
- **Descripción:** Registrar la llegada física del paciente el día del turno
- **Actores principales:** Secretaria, Paciente, Médico
- **Datos capturados:** Hora real de llegada vs hora programada
- **Resultado:** Turno en estado "Presente", listo para consulta

---

## Nomenclatura de Archivos

```
03-[nombre-caso-uso]-[tipo-flujo].md
```

Donde:
- `03-` = Identificador de actividad (Actividad Obligatoria N°3 - Análisis de Escenarios)
- `[nombre-caso-uso]` = Nombre descriptivo del caso de uso
- `[tipo-flujo]` = FP (Flujo Principal) o FA (Flujo Alterno)

---

## Relación con otros Artefactos

| Artefacto | Archivo | Relación |
|-----------|---------|----------|
| **Diagramas de Casos de Uso** | `/diagramas/02-casos-de-uso/` | Los escenarios detallan cada caso de uso representado en los diagramas |
| **Tarjetas CRC** | `/herramientas-agile/tarjetas-crc/` | Los escenarios identifican las responsabilidades de cada clase |
| **Documentación de Procesos IA** | `/ia/a2/especialista-escenarios.md` | Explica la metodología y prompts usados para generar los escenarios |

---

## Cómo Leer los Escenarios

Cada escenario sigue una estructura uniforme:

1. **ID y Nombre:** Identificación única y título descriptivo
2. **Actores:** Quiénes participan (roles, personas específicas)
3. **Precondiciones:** Estado del sistema antes de iniciar el escenario
4. **Flujo Principal:** Pasos secuenciales del proceso exitoso
5. **Flujo Alterno:** Variaciones (si existen)
6. **Postcondiciones:** Estado del sistema después de completar el escenario

---

## Metodología de Validación

Estos escenarios fueron generados usando:
- Análisis de requisitos funcionales (RF01-RF05)
- Requisitos no funcionales especiales (RNF01-05)
- Contexto real del mundo del negocio (Sistema de Turnos Médicos)
- Confirmación de trazabilidad y auditoría en cada operación
- Integración con Copilot AI Assistant para enriquecimiento de detalles

Toda modificación a estos escenarios debe mantener coherencia con los diagramas UML y tarjetas CRC.

---

**Última actualización:** 2026-04-16
**Responsable:** Natalia Carreras (Especialista en Escenarios - Rol A2)
