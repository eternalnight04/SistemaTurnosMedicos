# Escenario: Autorizar Sobreturno - Flujo Principal

## ID
03-CU04-FP

## Nombre
Agregar Sobreturno Autorizado por el Médico

## Actores
- Secretaria (Laura)
- Médico (Dr. Molina)
- Paciente (Patricia Gómez)
- Sistema de Turnos

## Precondiciones
- La secretaria Laura está autenticada en el sistema
- El Dr. Molina está presente físicamente en el consultorio
- Patricia Gómez tiene una emergencia y necesita ser atendida fuera del horario normal
- El Dr. Molina verbalmente autoriza agregar un sobreturno para Patricia
- Para ese horario ya existen otros turnos confirmados

## Flujo Principal
1. La secretaria Laura intenta crear un turno para Patricia Gómez en 2026-04-16 a las 16:30
2. El sistema detecta que este horario está FUERA de la disponibilidad normal del Dr. Molina (cierra a las 16:00)
3. El sistema advierte: "El horario 16:30 está fuera de disponibilidad. ¿Desea agregar un sobreturno?"
4. Laura responde: "Sí, el Dr. Molina autoriza el sobreturno"
5. El sistema pide confirmación explícita: "⚠️ Está a punto de crear un SOBRETURNO. Conforme que el médico lo autorizó. ¿Continuar?"
6. Laura confirma haciendo click en "Sí, autorizar sobreturno"
7. El sistema registra el turno con indicador "sobreturno = TRUE"
8. El sistema guarda en historial: [2026-04-16 16:20, usuario:Laura, acción:crear_sobreturno, autorizado_por:Dr_Molina, turno_id:89012, observacion:Emergency]
9. El sistema envía WhatsApp a Patricia: "Se le ha agendado un sobreturno para POY a las 16:30 con el Dr. Molina (EMERGENCIA)"
10. La secretaria visualiza el turno en la agenda con indicador "SOBRETURNO" en color rojo

## Flujo Alterno
NA

## Postcondiciones
- El sobreturno queda registrado con su indicador "sobreturno = TRUE"
- El historial deja trazabilidad de que fue autorizado manualmente por el Dr. Molina
- La agenda muestra visualmente el sobreturno diferenciado del resto
- NO se generaron sobreturnos automáticos (solo por autorización explícita)
- Patricia Gómez es atendida en horario fuera de la disponibilidad normal
