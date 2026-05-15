# 03-cancelar-turno-flujo-principal

## Tabla 1: Metadatos del Escenario

| Campo | Valor |
|-------|-------|
| **Nombre Escenario** | Cancelar Turno a Solicitud del Paciente |
| **Nombre Caso de Uso** | UC-03: Cancelar Turno |
| **ID Única** | 03-CU03-FP |
| **Área** | Gestión de Turnos |
| **Actor(es)** | Secretaria (Carlos), Paciente (Roberto López), Sistema |
| **Descripción** | La secretaria cancela un turno existente cuando el paciente lo solicita, liberando el horario |

## Tabla 2: Evento/Señal Activador

| Campo | Valor |
|-------|-------|
| **Activar Evento** | Paciente solicita cancelación de turno vía teléfono |
| **Identificadores e iniciadores** | Usuario: Carlos (Secretaria), Timestamp: 2026-04-16 10:30, Llamada telefónica de Roberto López |
| **Tipo Señal** | ☑ Usuario ☐ Sistema ☐ Externo |

## Tabla 3: Pasos Desempeñados

| Pasos desempeñados | Información para los pasos |
|--------------------|---------------------------|
| 1. Acceder a módulo "Buscar Turno" | Secretaria Carlos autenticada, módulo búsqueda |
| 2. Buscar turno | Búsqueda: Roberto López, fecha 2026-04-22 |
| 3. Mostrar detalles | Sistema muestra: turno_id:54789, Dr. Molina, 09:00 AM, estado:Confirmado |
| 4. Seleccionar "Cancelar turno" | Carlos selecciona opción de cancelación |
| 5. Solicitar motivo | Sistema pregunta: "¿Motivo de la cancelación?" |
| 6. Ingresar motivo | Carlos registra: "A pedido del paciente (llamada telefónica)" |
| 7. Confirmar acción | Sistema solicita confirmación explícita del cancelación |
| 8. Procesar cancelación | Sistema cambia estado a "Cancelado" |
| 9. Liberar horario | Horario 09:00-09:15 del 22/04 disponible para Dr. Molina |
| 10. Registrar en historial | [2026-04-16 10:30, usuario:Carlos, acción:cancelar_turno, motivo:a_pedido_del_paciente, turno_id:54789] |
| 11. Enviar notificación | WhatsApp a Roberto: "Tu turno del 22/04 09:00 AM con Dr. Molina ha sido cancelado" |
| 12. Mostrar resultado | Secretaria visualiza turno con estado "Cancelado" |

## Tabla 4: Condiciones de Contexto

| Elemento | Descripción |
|----------|-------------|
| **Precondiciones** | Secretaria autenticada, Turno de Roberto López existe y en estado "Confirmado", Turno programado para 22/04 09:00 AM con Dr. Molina |
| **Poscondiciones** | Turno con estado "Cancelado" (no eliminado, solo cambio de estado), Horario 09:00-09:15 disponible, Paciente notificado, Historial registrado |
| **Suposiciones** | Turno realmente existe en sistema, Paciente desea cancelación definitiva, WhatsApp operativo |
| **Reunir Requerimientos** | R-01: Cancelar turno, R-02: Liberar horario, R-03: Notificar al paciente |
| **Aspectos Sobresalientes** | Cancelación NO elimina turno sino cambia estado (trazabilidad), Motivo documentado, Notificación automática |
| **Prioridad** | Alta |
| **Riesgo** | Bajo |
