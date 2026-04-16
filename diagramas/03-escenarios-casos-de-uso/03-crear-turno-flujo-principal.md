# Escenario: Crear Turno - Flujo Principal

## ID
03-CU01-FP

## Nombre
Crear Turno de Control Médico - Caso Exitoso

## Actores
- Secretaria (Laura)
- Paciente (Juan García)
- Sistema de Turnos

## Precondiciones
- La secretaria Laura está autenticada en el sistema
- El paciente Juan García existe en el sistema
- El Dr. Molina tiene disponibilidad en su agenda para el próximo martes 10:00 AM

## Flujo Principal
1. La secretaria Laura accede al módulo "Nuevo Turno"
2. Busca al paciente "Juan García" en la base de datos
3. Selecciona al Dr. Molina como profesional
4. Selecciona la fecha: 2026-04-21 (martes próximo)
5. Selecciona la hora: 10:00 AM
6. Selecciona tipo de consulta: "Control" (duración: 15 minutos)
7. El sistema verifica que el horario 10:00-10:15 está dentro de disponibilidad del Dr. Molina
8. El sistema verifica que NO existe otro turno en ese horario
9. El sistema registra el turno con estado "Confirmado"
10. El sistema guarda en el historial: [2026-04-16 14:30, usuario:Laura, acción:crear_turno, turno_id:12345]
11. El sistema envía WhatsApp al paciente: "Su turno está confirmado para el martes 21/04 a las 10:00 AM con el Dr. Molina"
12. La secretaria visualiza el turno creado en la agenda

## Flujo Alterno
No hay desviaciones en este caso - todo funciona según lo previsto

## Postcondiciones
- El turno queda registrado como "Confirmado" en la agenda del Dr. Molina
- El paciente Juan García recibe notificación de confirmación por WhatsApp
- El historial registra la creación con trazabilidad completa (fecha, hora, usuario, ID del turno)
- El horario 10:00-10:15 del Dr. Molina el 21/04 ya no está disponible para otros pacientes
