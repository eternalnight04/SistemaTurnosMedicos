# Escenarios de Casos de Uso

- [Crear Turno - Flujo Principal](03-crear-turno-flujo-principal.md)
- [Reprogramar Turno - Flujo Alterno](03-reprogramar-turno-flujo-alterno.md)
- [Cancelar Turno - Flujo Principal](03-cancelar-turno-flujo-principal.md)
- [Autorizar Sobreturno - Flujo Principal](03-autorizar-sobreturno-flujo-principal.md)
- [Registrar Llegada del Paciente - Flujo Principal](03-registrar-llegada-flujo-principal.md)

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
