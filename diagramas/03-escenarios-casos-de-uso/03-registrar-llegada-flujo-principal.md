# Escenario: Registrar Llegada del Paciente - Flujo Principal

## ID
03-CU05-FP

## Nombre
Registrar Llegada de Paciente en el Día de la Cita

## Actores
- Secretaria (Carlos)
- Paciente (Diego Martínez)
- Médico (Dr. Molina)
- Sistema de Turnos

## Precondiciones
- La secretaria Carlos está autenticada en el sistema
- Es el día 2026-04-21 (día del turno)
- Existe un turno confirmado para Diego Martínez a las 10:00 AM con el Dr. Molina
- Diego Martínez acaba de llegar físicamente al consultorio

## Flujo Principal
1. Diego Martínez llega a la recepción del consultorio a las 09:58 AM
2. La secretaria Carlos accede a la agenda diaria
3. Se muestra lista de turnos para 2026-04-21 (hoy)
4. La secretaria ubica el turno: Diego Martínez - 10:00 AM - Dr. Molina - Estado:Confirmado
5. La secretaria selecciona "Registrar llegada"
6. El sistema registra automáticamente la hora real de llegada: 09:58 AM
7. El sistema cambia el estado del turno a "Presente"
8. El sistema guarda en historial: [2026-04-21 09:58, acción:registrar_llegada, hora_programada:10:00, hora_real:09:58, diferencia:-2_minutos]
9. El sistema muestra confirmación: "Llegada registrada - Paciente presente"
10. La agenda muestra el turno con estado "Presente" para que el Dr. Molina sepa que puede iniciar la atención
11. La secretaria comunica al Dr. Molina que Diego Martínez está listo

## Flujo Alterno
FA-05B: Si Diego hubiera llegado a las 10:15 (15 minutos tarde)
- El sistema igualmente registra la llegada real: 10:15 AM
- El sistema advierte: "Paciente llegó 15 minutos después de lo programado"
- El turno cambia a estado "Presente" (la diferencia horaria quedará registrada)

## Postcondiciones
- El turno queda con estado "Presente"
- El historial registra la hora exacta de llegada con timestamp (09:58:00)
- El Dr. Molina visualiza que Diego Martínez está presente y puede iniciar la consulta
- La diferencia entre hora programada (10:00) e hora real (09:58) queda documentada en la trazabilidad
