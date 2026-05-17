# 03-autorizar-sobreturno-flujo-principal

## Tabla 1: Metadatos del Escenario

| Campo | Valor |
|-------|-------|
| **Nombre Escenario** | Agregar Sobreturno Autorizado por el Médico |
| **Nombre Caso de Uso** | UC-04: Autorizar Sobreturno |
| **ID Única** | 03-CU04-FP |
| **Área** | Gestión de Turnos |
| **Actor(es)** | Secretaria (Laura), Médico (Dr. Molina), Paciente (Patricia Gómez), Sistema |
| **Descripción** | La secretaria crea un sobreturno fuera del horario normal cuando el médico lo autoriza para emergencias |

## Tabla 2: Evento/Señal Activador

| Campo | Valor |
|-------|-------|
| **Activar Evento** | Paciente requiere atención médica urgente fuera de horario normal |
| **Identificadores e iniciadores** | Usuario: Laura (Secretaria), Timestamp: 2026-04-16 16:20, Autorización verbal del Dr. Molina |
| **Tipo Señal** | ☑ Sistema ☐ Usuario ☑ Externo (emergencia) |

## Tabla 3: Pasos Desempeñados

| Pasos desempeñados | Información para los pasos |
|--------------------|---------------------------|
| 1. Secretaria intenta crear turno | Laura intenta crear cita para Patricia en 2026-04-16 16:30 |
| 2. Verificar horario | Sistema detecta que 16:30 **está FUERA de disponibilidad normal** (cierre a las 16:00) |
| 3. Advertencia al usuario | Sistema advierte: "¿Desea agregar un sobreturno? (Fuera de disponibilidad)" |
| 4. Secretaria confirma autorización | Laura responde: "Sí, el Dr. Molina autoriza el sobreturno" |
| 5. Solicitar confirmación explícita | Sistema pide: "⚠️ SOBRETURNO. ¿Confirma autorización médica? ¿Continuar?" |
| 6. Secretaria confirma | Laura hace click en "Sí, autorizar sobreturno" |
| 7. Registrar turno con indicador | Sistema crea turno con bandera: sobreturno = TRUE |
| 8. Asignar ID | Turno recibe turno_id:89012 |
| 9. Guardar en historial | [2026-04-16 16:20, usuario:Laura, acción:crear_sobreturno, autorizado_por:Dr_Molina, turno_id:89012, observacion:Emergency] |
| 10. Enviar notificación | WhatsApp a Patricia: "Se agendó sobreturno para HOY 16:30 con Dr. Molina (EMERGENCIA)" |
| 11. Mostrar en agenda | Secretaria visualiza turno en agenda con indicador "SOBRETURNO" en color rojo |

## Tabla 4: Condiciones de Contexto

| Elemento | Descripción |
|----------|-------------|
| **Precondiciones** | Secretaria autenticada, Dr. Molina presente físicamente en consultorio, Patricia Gómez necesita emergencia, Dr. Molina verbalmente autoriza, Algunos turnos ya confirmados en ese horario |
| **Poscondiciones** | Sobreturno registrado con indicador sobreturno=TRUE, Historial con trazabilidad de autorización, Agenda muestra diferenciación visual (rojo), NO se generan sobreturnos automáticos, Patricia Gómez atendida fuera de horario normal |
| **Suposiciones** | Dr. Molina puede atender en horario extendido, Emergencia es válida y documentada, WhatsApp operativo |
| **Reunir Requerimientos** | R-01: Crear sobreturno, R-02: Requerir autorización explícita, R-03: Indicador visual diferenciado, R-04: Trazabilidad de autorización |
| **Aspectos Sobresalientes** | Sobreturno requiere autorización explícita del médico, Solo se generan manualmente (no automático), Indicador visual diferenciado en agenda, Trazabilidad completa de autorización, Emergencia documentada |
| **Prioridad** | Alta |
| **Riesgo** | Medio (requiere validación de emergencia) |
