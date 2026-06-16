# Happy Path Global: creación de turno hasta llegada del paciente

## Tabla de trazabilidad (Caso de uso → Clases/métodos → Diagramas de secuencia)

- Crear turno: `Secretaria.agendarTurno()` / `Agenda.verificarDisponibilidad()` / `Turno.crearTurno()` → [05-secuencia-crear-turno-03.puml](diagramas/05-diagramas-secuencia/05-secuencia-crear-turno-03.puml)
- Reprogramar turno: `Secretaria.reprogramarTurno()` / `Turno.reprogramar()` / `Agenda.verificarDisponibilidad()` → [05-secuencia-reprogramar-turno-05.puml](diagramas/05-diagramas-secuencia/05-secuencia-reprogramar-turno-05.puml)
- Cancelar turno: `Secretaria.cancelarTurno()` / `Turno.cancelar()` / `Agenda.liberarHorario()` → [05-secuencia-cancelar-turno-02.puml](diagramas/05-diagramas-secuencia/05-secuencia-cancelar-turno-02.puml)
- Autorizar sobreturno: `Medico.autorizarSobreturno()` / `Agenda.confirmarAutorizacion()` / `Turno.crearTurno(sobreturno=true)` → [05-secuencia-autorizar-sobreturno-01.puml](diagramas/05-diagramas-secuencia/05-secuencia-autorizar-sobreturno-01.puml)
- Registrar llegada: `Secretaria.registrarLlegada()` / `Turno.registrarLlegada()` / `LlegadaPaciente.calcularDiferencia()` → [05-secuencia-registrar-llegada-04.puml](diagramas/05-diagramas-secuencia/05-secuencia-registrar-llegada-04.puml)

## Pseudocódigo orientado a objetos (flujo happy path)

class Sistema {
  agenda: Agenda
  secretaria: Secretaria
  medico: Medico

  crearTurno(pacienteId, medicoId, fechaHora, tipo) {
    if (!agenda.verificarDisponibilidad(medicoId, fechaHora.date, fechaHora.time)) {
      alternativas = agenda.sugerirHorariosAlternativos(medicoId, fechaHora.date)
      return alternativas
    }
    turno = Turno.crearTurno(fechaHora, pacienteRepository.get(pacienteId), medicoRepository.get(medicoId), sobreturno=false)
    agenda.turnos.add(turno)
    agenda.registrarEnHistorial(turno.id, "crear")
    pacienteRepository.notify(pacienteId, "Turno confirmado: " + turno.id)
    return turno
  }

  registrarLlegada(turnoId, horaReal) {
    turno = agenda.buscarTurno(turnoId)
    llegada = new LlegadaPaciente(horaReal)
    turno.registrarLlegada(horaReal)
    llegada.diferenciaMinutos = llegada.calcularDiferencia(turno.fechaHoraProgramada)
    agenda.registrarEnHistorial(turno.id, "registrar_llegada")
    medico.notifyPresencia(turno.paciente.id, turno.id)
  }
}

## Flujo completo (paso a paso)

1. Paciente solicita turno a la `Secretaria` (o por interfaz paciente).
2. `Secretaria` invoca `Agenda.verificarDisponibilidad(medicoId, fecha, hora)`.
3. Si disponible: `Agenda` crea/encarga `Turno.crearTurno(...)` y `Turno.cambiarEstado(CONFIRMADO)`.
4. `Agenda` registra la acción en historial y envía notificación al `Paciente`.
5. Día del turno: `Paciente` se presenta y la `Secretaria` ejecuta `Turno.registrarLlegada(horaReal)`.
6. `Turno` cambia estado a `PRESENTE` y `Agenda` notifica al `Medico`.
7. `Medico` atiende y puede registrar observaciones en `Turno`.

***
Los métodos y nombres usados en el pseudocódigo están alineados con las tarjetas CRC y diagramas de secuencia analizados.
