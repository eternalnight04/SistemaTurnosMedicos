# 03-registrar-llegada-flujo-principal

## Tabla 1: Metadatos del Escenario

| Campo | Valor |
|-------|-------|
| **Nombre Escenario** | Registrar Llegada de Paciente en el Día de la Cita |
| **Nombre Caso de Uso** | UC-05: Registrar Llegada Paciente |
| **ID Única** | 03-CU05-FP |
| **Área** | Gestión de Turnos |
| **Actor(es)** | Secretaria (Carlos), Paciente (Diego Martínez), Médico (Dr. Molina), Sistema |
| **Descripción** | La secretaria registra la llegada real del paciente en el consultorio, cambiando estado a "Presente" |

## Tabla 2: Evento/Señal Activador

| Campo | Valor |
|-------|-------|
| **Activar Evento** | Paciente se presenta en la recepción del consultorio |
| **Identificadores e iniciadores** | Usuario: Carlos (Secretaria), Timestamp: 2026-04-21 09:58 AM, Arribo físico de Diego Martínez |
| **Tipo Señal** | ☑ Usuario ☐ Sistema ☐ Externo |

## Tabla 3: Pasos Desempeñados

| Pasos desempeñados | Información para los pasos |
|--------------------|---------------------------|
| 1. Paciente llega a recepción | Diego Martínez se presenta en consultorio a las 09:58 AM |
| 2. Acceder a agenda diaria | Secretaria Carlos abre agenda del día 2026-04-21 |
| 3. Mostrar turnos del día | Sistema lista todos los turnos programados para hoy |
| 4. Ubicar turno del paciente | Carlos localiza: Diego Martínez - 10:00 AM - Dr. Molina - Estado: Confirmado |
| 5. Seleccionar "Registrar llegada" | Carlos selecciona opción de llegada para Diego |
| 6. Registrar hora real | Sistema registra automáticamente hora exacta: 09:58 AM |
| 7. Cambiar estado del turno | Sistema cambia estado de "Confirmado" a "Presente" |
| 8. Guardar en historial | [2026-04-21 09:58, acción:registrar_llegada, hora_programada:10:00, hora_real:09:58, diferencia:-2_minutos] |
| 9. Mostrar confirmación | Sistema muestra: "Llegada registrada - Paciente presente" |
| 10. Actualizar agenda | Dr. Molina ve turno con estado "Presente", puede iniciar consulta |
| 11. Comunicar al médico | Secretaria informa al Dr. Molina que Diego está listo |

## Tabla 4: Condiciones de Contexto

| Elemento | Descripción |
|----------|-------------|
| **Precondiciones** | Secretaria autenticada, Es el día 2026-04-21 (día del turno), Turno confirmado para Diego a las 10:00 AM con Dr. Molina, Diego se presenta físicamente |
| **Poscondiciones** | Turno con estado "Presente", Historial registra hora exacta de llegada (09:58 AM), Dr. Molina visualiza disponibilidad del paciente, Diferencia temporal documentada (-2 minutos) |
| **Suposiciones** | Reloj del sistema es preciso, Diego es la persona correcta del turno, Dr. Molina está disponible |
| **Reunir Requerimientos** | R-01: Registrar llegada, R-02: Cambiar estado a Presente, R-03: Documentar hora real |
| **Aspectos Sobresalientes** | Registro automático de hora real con precisión, Detección de diferencia temporal (adelanto/atraso), Notificación automática al médico, Trazabilidad completa |
| **Prioridad** | Alta |
| **Riesgo** | Bajo |
