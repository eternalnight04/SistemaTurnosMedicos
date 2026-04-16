# Escenario: Reprogramar Turno - Flujo Alterno

## ID
03-CU02-FA

## Nombre
Reprogramar Turno por Conflicto de Horario Existente

## Actores
- Secretaria (Laura)
- Paciente (María Rodríguez)
- Sistema de Turnos

## Precondiciones
- La secretaria Laura está autenticada en el sistema
- El turno de María Rodríguez existe y está en estado "Confirmado"
- El turno está programado para 2026-04-18 a las 14:00 con la Dra. Patricia Garcia
- María Rodríguez necesita cambiar su hora

## Flujo Principal
1. La secretaria Laura accede al módulo "Buscar Turno"
2. Busca el turno de María Rodríguez para 2026-04-18
3. Selecciona "Reprogramar turno"
4. El sistema muestra el turno actual: 18/04 14:00 con Dra. Patricia Garcia
5. La secretaria intenta cambiar a 18/04 14:15 (15 minutos después)
6. El sistema verifica disponibilidad en ese nuevo horario
7. **El sistema detecta que EXISTE OTRO TURNO en 14:15** (conflicto de superposición)
8. El sistema bloquea el cambio y muestra mensaje: "Horario ocupado. El 18/04 a las 14:15 ya existe un turno con esta profesional"
9. El sistema sugiere horarios disponibles: 14:30, 14:45, 15:00
10. La secretaria selecciona 15:00 AM como nueva hora
11. El sistema valida que 15:00 está libre
12. El sistema actualiza el turno al nuevo horario: 18/04 15:00
13. El sistema registra en historial: [horario_anterior:14:00, horario_nuevo:15:00, usuario:Laura, fecha_cambio:16/04 14:45]
14. El sistema envía WhatsApp a María: "Su turno fue reprogramado para el 18/04 a las 15:00 con la Dra. Patricia Garcia"

## Flujo Alterno
NA

## Postcondiciones
- El turno queda reprogramado a las 15:00 (18/04)
- El horario 14:00-14:15 queda disponible para otras reservas
- El historial refleja la reprogramación con trazabilidad completa
- María Rodríguez es notificada del nuevo horario
