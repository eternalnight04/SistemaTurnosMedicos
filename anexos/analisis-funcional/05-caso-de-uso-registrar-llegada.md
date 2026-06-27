# Caso de Uso N° 05 - Registrar Llegada

---

## 1. Descripción y Trazabilidad con Requisitos Funcionales

**Actor/es:** Secretaria (Carlos), Paciente, Sistema

**Objetivo:** La secretaria registra la llegada de un paciente cuando este se presenta en el establecimiento para su turno.

**Flujo principal:**

1. Acceder al módulo "Buscar Turno".
2. Buscar turno del paciente.
3. Mostrar detalles del turno.
4. Seleccionar opción "Registrar llegada".
5. Confirmar identidad del paciente.
6. Validar que el turno exista.
7. Marcar turno como "Paciente presente".
8. Registrar hora de llegada.
9. Guardar modificación en el sistema.
10. Actualizar estado del turno.
11. Registrar en historial.
12. Mostrar confirmación.

**Requisitos funcionales que satisface:**

| ID | Requisito Funcional (texto exacto de introduccion.md) | Cómo lo satisface este caso de uso |
|----|------------------------------------------------------|-------------------------------------|
| RF01 | Gestionar turnos de pacientes. | Permite actualizar el estado del turno cuando el paciente llega. |
| RF05 | Gestionar la disponibilidad horaria de los profesionales. | Permite actualizar el estado del turno para continuar la atención. |

---

## 2. Diagrama de Casos de Uso

[Diagrama de Casos de Uso - Registrar Llegada](../../diagramas/02-casos-de-uso/05-caso-uso-registrar-llegada.png)

**Actores y relaciones:**

- Paciente → se presenta al sistema para su atención.
- Secretaria → busca el turno y registra la llegada.
- Include/Extend: incluye validar turno, registrar llegada y actualizar estado.

---

## 3. Diagrama de Actividades

[Diagrama de Actividades - Registrar Llegada](../../diagramas/04-diagramas-actividades/05-actividad-registrar-llegada-caso-uso-05.png)

**Swimlanes:** Paciente, Secretaria y Sistema.

**Decisiones clave del flujo:** Verificar existencia del turno, confirmar identidad del paciente y validar estado del turno.

---

## 4. Diagrama de Secuencia

[Diagrama de Secuencia - Registrar Llegada](../../diagramas/05-diagramas-secuencia/05-secuencia-registrar-llegada-05.png)

**Participantes:** Paciente (actor), Secretaria (actor), Sistema, Agenda:agenda, Turno:turno

**Mensajes clave:**

- informarLlegada()
- buscarTurno()
- obtenerTurno()
- marcarLlegada()
- registrarHoraLlegada()
- actualizarEstado()
- confirmarRegistro()

**Objetos temporales destruidos:** No se eliminan objetos, solo se actualiza el estado del turno.

---

## 5. Diagrama de Clases del Caso de Uso

[Diagrama de Clases - Registrar Llegada](../../diagramas/01-diagrama-clases/05-clases-registrar-llegada-05.png)

**Clases involucradas:**

| Clase | Responsabilidad (según tarjeta CRC) | Tarjeta CRC |
|-------|-------------------------------------|-------------|
| UsuarioDelSistema | Autenticar y actualizar datos | [Tarjeta CRC - UsuarioDelSistema](../../herramientas-agile/tarjetas-crc/06-tarjeta-crc-usuariodelsistema.md) |
| Paciente | Confirmar llegada | [Tarjeta CRC - Paciente](../../herramientas-agile/tarjetas-crc/01-tarjeta-crc-paciente.md) |
| Medico | Atender pacientes | [Tarjeta CRC - Medico](../../herramientas-agile/tarjetas-crc/02-tarjeta-crc-medico.md) |
| Turno | Actualizar estado del turno | [Tarjeta CRC - Turno](../../herramientas-agile/tarjetas-crc/03-tarjeta-crc-turno.md) |
| Agenda | Gestionar turnos | [Tarjeta CRC - Agenda](../../herramientas-agile/tarjetas-crc/04-tarjeta-crc-agenda.md) |
| Secretaria | Registrar llegada | [Tarjeta CRC - Secretaria](../../herramientas-agile/tarjetas-crc/05-tarjeta-crc-secretaria.md) |

**Relaciones UML:**

| Relación | Clases | Justificación |
|----------|--------|---------------|
| Herencia | UsuarioDelSistema → Paciente | Comparte estructura base del sistema |
| Herencia | UsuarioDelSistema → Secretaria | Comparte estructura base del sistema |
| Herencia | UsuarioDelSistema → Medico | Comparte estructura base del sistema |
| Asociación | Paciente → Turno | El paciente tiene un turno asignado |
| Asociación | Medico → Turno | El médico atiende turnos |
| Asociación | Secretaria → Agenda | La secretaria gestiona la agenda |
| Dependencia | Secretaria → Turno | Registra la llegada del paciente |
| Agregación | Agenda → Turno | La agenda contiene turnos |

---

## 6. Pseudocódigo

```text
INICIO Registrar Llegada

Paciente paciente = nuevo Paciente()
Secretaria secretaria = nuevo Secretaria()
Agenda agenda = nuevo Agenda()
Turno turno = nuevo Turno()

entrada = paciente.informarLlegada()

turno = agenda.buscarTurno(entrada.idTurno)

SI turno existe
    turno.marcarLlegada()
    turno.registrarHoraLlegada()
    turno.actualizarEstado("Paciente presente")

    agenda.guardarCambios(turno)

    Retornar "Llegada registrada correctamente"
SINO
    Retornar "Turno no encontrado"
FIN SI

FIN