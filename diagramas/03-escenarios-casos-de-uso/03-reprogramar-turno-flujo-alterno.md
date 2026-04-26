# 03-reprogramar-turno-flujo-alterno

## Tabla 1: Metadatos del Escenario

| Campo | Valor |
|-------|-------|
| **Nombre Escenario** | Reprogramar Turno por Conflicto de Horario Existente |
| **Nombre Caso de Uso** | UC-02: Reprogramar Turno |
| **ID Única** | 03-CU02-FA |
| **Área** | Gestión de Turnos |
| **Actor(es)** | Secretaria (Laura), Paciente (María Rodríguez), Sistema |
| **Descripción** | La secretaria reprograma un turno cuando el paciente lo solicita, detectando conflictos y sugiriendo horarios alternativos |

## Tabla 2: Evento/Señal Activador

| Campo | Valor |
|-------|-------|
| **Activar Evento** | Paciente solicita cambio de horario por conflicto personal |
| **Identificadores e iniciadores** | Usuario: Laura (Secretaria), Timestamp: 2026-04-16 14:45, Solicitud de María Rodríguez |
| **Tipo Señal** | ☑ Usuario ☐ Sistema ☐ Externo |

## Tabla 3: Pasos Desempeñados

| Pasos desempeñados | Información para los pasos |
|--------------------|---------------------------|
| 1. Acceder a módulo "Buscar Turno" | Secretaria Laura autenticada, módulo búsqueda |
| 2. Buscar turno | Búsqueda: María Rodríguez, fecha 2026-04-18 |
| 3. Mostrar detalles | Sistema muestra: 18/04 14:00 con Dra. Patricia Garcia |
| 4. Seleccionar "Reprogramar turno" | Laura selecciona opción de reprogramación |
| 5. Proponer nuevo horario | Laura intenta cambiar a 18/04 14:15 (15 minutos después) |
| 6. Validar disponibilidad | Sistema verifica disponibilidad en el nuevo horario |
| 7. Detectar conflicto | **Sistema detecta: ya existe turno en 14:15** |
| 8. Bloquear cambio | Sistema rechaza cambio: "Horario ocupado. Turno existe en 14:15" |
| 9. Sugerir alternativas | Sistema sugiere horarios libres: 14:30, 14:45, 15:00 |
| 10. Seleccionar nuevo horario | Laura elige 15:00 AM como nueva hora |
| 11. Validar y confirmar | Sistema valida que 15:00 está libre, solicita confirmación |
| 12. Actualizar turno | Sistema cambia turno a 18/04 15:00 |
| 13. Registrar en historial | [horario_anterior:14:00, horario_nuevo:15:00, usuario:Laura, fecha_cambio:16/04 14:45] |
| 14. Enviar notificación | WhatsApp a María: "Tu turno fue reprogramado para 18/04 15:00 con Dra. Patricia Garcia" |

## Tabla 4: Condiciones de Contexto

| Elemento | Descripción |
|----------|-------------|
| **Precondiciones** | Secretaria autenticada, Turno de María Rodríguez existe y en estado "Confirmado", Turno programado para 18/04 14:00 con Dra. Patricia Garcia |
| **Poscondiciones** | Turno reprogramado a 15:00 (18/04), Horario 14:00-14:15 disponible, Historial con trazabilidad completa, Paciente notificado |
| **Suposiciones** | Conflicto de superposición detectable, Sistema siempre sugiere alternativas, WhatsApp operativo |
| **Reunir Requerimientos** | R-01: Reprogramar turno, R-02: Detectar conflictos, R-03: Sugerir horarios alternativos, R-04: Notificar |
| **Aspectos Sobresalientes** | Detección automática de conflictos, Sugerencias de horarios alternativos, Bloqueo de cambios conflictivos, Trazabilidad del cambio |
| **Prioridad** | Alta |
| **Riesgo** | Medio (requiere aprobación de alternativas) |
