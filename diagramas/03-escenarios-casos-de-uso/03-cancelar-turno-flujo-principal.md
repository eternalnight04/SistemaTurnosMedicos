# Escenario: Cancelar Turno - Flujo Principal

## ID
03-CU03-FP

## Nombre
Cancelar Turno a Solicitud del Paciente

## Actores
- Secretaria (Carlos)
- Paciente (Roberto López)
- Sistema de Turnos

## Precondiciones
- La secretaria Carlos está autenticada en el sistema
- El turno de Roberto López existe y está en estado "Confirmado"
- El turno está programado para 2026-04-22 a las 09:00 con el Dr. Molina
- Roberto llamó por teléfono pidiendo cancelar el turno

## Flujo Principal
1. La secretaria Carlos accede al módulo "Buscar Turno"
2. Busca el turno de Roberto López para 2026-04-22
3. Se muestra: turno_id:54789, paciente:Roberto López, doctor:Dr. Molina, fecha:22/04, hora:09:00, estado:Confirmado
4. Carlos selecciona "Cancelar turno"
5. El sistema solicita: "¿Motivo de la cancelación?"
6. Carlos ingresa: "A pedido del paciente (llamada telefónica)"
7. El sistema solicita confirmación: "¿Está seguro de que desea cancelar este turno?"
8. Carlos confirma haciendo click en "Sí, cancelar"
9. El sistema cambia el estado del turno a "Cancelado"
10. El sistema libera el horario 09:00-09:15 del 22/04 para el Dr. Molina
11. El sistema registra en historial: [2026-04-16 10:30, usuario:Carlos, acción:cancelar_turno, motivo:a_pedido_del_paciente, turno_id:54789]
12. El sistema envía WhatsApp a Roberto: "Su turno del 22/04 a las 09:00 con el Dr. Molina ha sido cancelado"
13. La secretaria ve el turno con estado "Cancelado" en la pantalla

## Flujo Alterno
NA

## Postcondiciones
- El turno queda con estado "Cancelado" (no se elimina del sistema, solo muda de estado)
- El horario 09:00-09:15 del Dr. Molina en 22/04 queda disponible para nuevas reservas
- Roberto López es notificado de la cancelación
- El historial registra la cancelación con motivo y persona responsable (trazabilidad)
