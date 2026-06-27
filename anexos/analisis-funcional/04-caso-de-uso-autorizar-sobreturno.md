# Caso de Uso N° 04 - Autorizar Sobreturno

---

## 1. Descripción y Trazabilidad con Requisitos Funcionales

**Actor/es:** Secretaria, Paciente, Médico, Sistema

**Objetivo:** La secretaria autoriza un sobreturno cuando no hay disponibilidad en la agenda normal o se requiere una excepción para atención médica.

**Flujo principal:**

1. Acceder al módulo “Gestión de Turnos”.
2. Buscar disponibilidad del médico.
3. Detectar falta de turnos disponibles o necesidad de excepción.
4. Seleccionar opción “Autorizar sobreturno”.
5. Ingresar datos del paciente.
6. Ingresar médico asignado.
7. Ingresar motivo del sobreturno.
8. Validar disponibilidad especial del médico.
9. Crear registro de sobreturno.
10. Asignar fecha y hora del sobreturno.
11. Guardar sobreturno en el sistema.
12. Actualizar agenda del médico.
13. Notificar confirmación de autorización.

**Requisitos funcionales que satisface:**

| ID | Requisito Funcional | Cómo lo satisface este caso de uso |
|----|---------------------|-------------------------------------|
| RF01 | Gestionar turnos de pacientes. | Permite crear un turno excepcional (sobreturno) para el paciente. |
| RF05 | Gestionar la disponibilidad horaria de los profesionales. | Permite validar y modificar la disponibilidad del médico para aceptar el sobreturno. |

---

## 2. Diagrama de Casos de Uso

[Diagrama de Casos de Uso - Autorizar Sobreturno](../../diagramas/02-casos-de-uso/04-caso-uso-autorizar-sobreturno.png)

**Actores y relaciones:**

- Paciente → recibe el sobreturno autorizado.
- Secretaria → gestiona y autoriza el sobreturno.
- Médico → valida disponibilidad.
- Include/Extend: incluye verificar disponibilidad, crear sobreturno y actualizar agenda.

---

## 3. Diagrama de Actividades

[Diagrama de Actividades - Autorizar Sobreturno](../../diagramas/04-diagramas-actividades/04-actividad-autorizar-sobreturno.png)

**Swimlanes:** Secretaria, Sistema, Médico, Paciente.

**Decisiones clave del flujo:**

- Verificar disponibilidad del médico.
- Validar datos del paciente.
- Confirmar motivo del sobreturno.
- Autorizar o rechazar sobreturno.

---

## 4. Diagrama de Secuencia

[Diagrama de Secuencia - Autorizar Sobreturno](../../diagramas/05-diagramas-secuencia/04-secuencia-autorizar-sobreturno.png)

**Participantes:** Secretaria, Paciente, Médico, Sistema, Agenda:agenda, Sobreturno:sobreturno

**Mensajes clave:**

- solicitarSobreturno()
- verificarDisponibilidad()
- tieneDisponibilidad()
- crearSobreturno()
- registrarSobreturno()
- actualizarAgenda()
- confirmarAutorizacion()

**Objetos temporales destruidos:** No se eliminan objetos, solo se crea y registra el sobreturno.

---

## 5. Diagrama de Clases del Caso de Uso

[Diagrama de Clases - Autorizar Sobreturno](../../diagramas/01-diagrama-clases/04-clases-autorizar-sobreturno.png)

**Clases involucradas:**

| Clase | Responsabilidad (según tarjeta CRC) | Tarjeta CRC |
|-------|-------------------------------------|-------------|
| UsuarioDelSistema | Base común de usuarios del sistema | [Tarjeta CRC - UsuarioDelSistema](../../herramientas-agile/tarjetas-crc/06-tarjeta-crc-usuariodelsistema.md) |
| Paciente | Solicitar atención | [Tarjeta CRC - Paciente](../../herramientas-agile/tarjetas-crc/01-tarjeta-crc-paciente.md) |
| Medico | Validar disponibilidad | [Tarjeta CRC - Medico](../../herramientas-agile/tarjetas-crc/02-tarjeta-crc-medico.md) |
| Secretaria | Autorizar sobreturnos | [Tarjeta CRC - Secretaria](../../herramientas-agile/tarjetas-crc/05-tarjeta-crc-secretaria.md) |
| Agenda | Gestionar disponibilidad | [Tarjeta CRC - Agenda](../../herramientas-agile/tarjetas-crc/04-tarjeta-crc-agenda.md) |
| Auditoria | Registrar cambios | [Tarjeta CRC - Auditoria](../../herramientas-agile/tarjetas-crc/08-tarjeta-crc-auditoria.md) |

**Relaciones UML:**

| Relación | Clases | Justificación |
|----------|--------|---------------|
| Herencia | UsuarioDelSistema → Paciente | Estructura común del sistema |
| Herencia | UsuarioDelSistema → Secretaria | Estructura común del sistema |
| Herencia | UsuarioDelSistema → Medico | Estructura común del sistema |
| Asociación | Paciente → Turno | El paciente recibe el sobreturno |
| Asociación | Medico → Turno | El médico autoriza el sobreturno |
| Asociación | Secretaria → Agenda | Gestiona la agenda de turnos |
| Dependencia | Secretaria → Turno | Crea el sobreturno |
| Agregación | Agenda → Turno | La agenda contiene sobreturnos |
| Asociación | Auditoria → Agenda | Auditoria guarda los cambios realizados en Agenda |


---

## 6. Pseudocódigo

```

INICIO

Secretaria solicita sobreturno (paciente, fecha, hora)

SI Agenda.intentarCrearTurno(fecha, hora, paciente) == NO DISPONIBLE EN HORARIO

    MOSTRAR "Advertencia: sobreturno"

    Solicitar autorización al Médico

    SI Medico.autorizarSobreturno(turno) == TRUE

        Agenda.crearTurno(paciente, medico, sobreturno = TRUE)
        Auditoria.guardarEvento(usuario = secretaria, autorizadoPor = medico)
        Turno.asignarSobreturno(sobreturno=true)
        Turno.cambiarEstado("Confirmado")

        MOSTRAR "Sobreturno confirmado"

    SINO

        MOSTRAR "Sobreturno rechazado por el médico"

FIN SI

FIN

```