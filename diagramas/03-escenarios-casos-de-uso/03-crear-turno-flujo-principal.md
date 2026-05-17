# 03-crear-turno-flujo-principal

## Tabla 1: Metadatos del Escenario

| Campo | Valor |
|-------|-------|
| **Nombre Escenario** | Crear Turno de Control Médico - Caso Exitoso |
| **Nombre Caso de Uso** | UC-01: Crear Turno |
| **ID Única** | 03-CU01-FP |
| **Área** | Gestión de Turnos |
| **Actor(es)** | Secretaria (Laura), Paciente (Juan García), Sistema |
| **Descripción** | La secretaria registra un nuevo turno de control médico en el sistema cuando un paciente solicita cita con el médico |

## Tabla 2: Evento/Señal Activador

| Campo | Valor |
|-------|-------|
| **Activar Evento** | Secretaria inicia proceso de crear nuevo turno |
| **Identificadores e iniciadores** | Usuario: Laura (Secretaria), Timestamp: 2026-04-16 14:30, Hora sistema |
| **Tipo Señal** | ☑ Sistema ☐ Usuario ☐ Externo |

## Tabla 3: Pasos Desempeñados

| Pasos desempeñados | Información para los pasos |
|--------------------|---------------------------|
| 1. Acceder a módulo "Nuevo Turno" | Secretaria Laura autenticada, accede a interfaz de creación |
| 2. Buscar paciente en base de datos | Se busca y selecciona "Juan García" del sistema |
| 3. Seleccionar profesional | Dr. Molina seleccionado como médico responsable |
| 4. Seleccionar fecha | 2026-04-21 (martes próximo) |
| 5. Seleccionar hora | 10:00 AM, duración: 15 minutos (tipo: Control) |
| 6. Validar disponibilidad | Sistema verifica que 10:00-10:15 está libre en agenda Dr. Molina |
| 7. Verificar conflictos | Sistema verifica que NO existe otro turno en ese horario |
| 8. Registrar turno | Sistema crea turno con estado "Confirmado", ID: 12345 |
| 9. Guardar en historial | Registro: [2026-04-16 14:30, usuario:Laura, acción:crear_turno, turno_id:12345] |
| 10. Enviar notificación | WhatsApp a Juan García: "Turno confirmado para 21/04 10:00 AM con Dr. Molina" |
| 11. Mostrar confirmación | Secretaria visualiza turno creado en agenda del Dr. Molina |

## Tabla 4: Condiciones de Contexto

| Elemento | Descripción |
|----------|-------------|
| **Precondiciones** | Secretaria autenticada, Paciente existe en sistema, Dr. Molina tiene disponibilidad en horario 10:00 AM |
| **Poscondiciones** | Turno en estado "Confirmado", Paciente notificado vía WhatsApp, Historial registrado con trazabilidad completa, Horario 10:00-10:15 del 21/04 no disponible |
| **Suposiciones** | La hora seleccionada está dentro de agenda normal del médico, WhatsApp está operativo |
| **Reunir Requerimientos** | R-01: Crear turno, R-02: Validar disponibilidad, R-03: Enviar notificación |
| **Aspectos Sobresalientes** | Notificación automática al paciente, Validación de disponibilidad en tiempo real, Trazabilidad completa |
| **Prioridad** | Alta |
| **Riesgo** | Bajo (flujo exitoso estándar) |
