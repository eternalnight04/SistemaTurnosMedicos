# Happy Path Global - Sistema de Turnos Médicos

## 1. Escenario Elegido

Escenario: Atención completa de un paciente desde la autenticación de una secretaria hasta la finalización de una consulta médica. Este escenario fue elegido como Happy Path Global porque atraviesa la mayor cantidad de clases del Sistema de Turnos Médicos y demuestra la colaboración entre los principales objetos del dominio durante el ciclo completo de atención.

Casos de uso involucrados: CU01 - Crear Turno, CU02 - Reprogramar Turno, CU04 - Autorizar Sobreturno y CU05 - Registrar Llegada.

Clases participantes:

UsuarioDelSistema
Secretaria
Paciente
Medico
Agenda
Turno
## 2. Pseudocódigo
INICIO Sistema de Turnos Médicos - Happy Path Global

// ============================================================
// CU01 - Crear Turno
// ============================================================

// La secretaria inicia sesión en el sistema para poder gestionar
// los turnos de los pacientes.

secre = new Secretaria(id: "SEC-001", nombre: "Laura", dni: "12345678")
accesoConcedido = secre.autenticar(password: "miPasswordSegura")

SI accesoConcedido ENTONCES

    // La secretaria registra un nuevo paciente en el sistema.

    datosPaciente = {
        nombre: "Juan García",
        dni: "30123456",
        email: "juan@mail.com"
    }

    nuevoPaciente = secre.darAltaPaciente(datos: datosPaciente)

    // Antes de crear el turno se verifica que el médico tenga
    // disponibilidad en la fecha y horario solicitados.

    medico = new Medico(matricula: "MP12345", especialidad: "Cardiología")
    agenda = new Agenda(id: "AG-001", medico: medico)

    hayDisponibilidad = agenda.verificarDisponibilidad(
        medicoId: medico.matricula,
        fecha: "2026-06-30",
        hora: "10:00"
    )

    SI hayDisponibilidad ENTONCES

        // La Agenda crea el nuevo turno para el paciente.

        nuevoTurno = agenda.crearTurno(
            fechaHora: "2026-06-30 10:00",
            paciente: nuevoPaciente,
            medico: medico,
            sobreturno: FALSO
        )

        nuevoTurno.cambiarEstado(nuevoEstado: TurnoEstado.PENDIENTE)

        // El paciente recibe la notificación y confirma
        // su asistencia al turno.

        nuevoPaciente.recibirNotificacion(
            mensaje: "Su turno ha sido asignado para el 30/06 a las 10:00"
        )

        confirmado = nuevoPaciente.confirmarTurno(turnoId: nuevoTurno.id)

        SI confirmado ENTONCES

            nuevoTurno.cambiarEstado(nuevoEstado: TurnoEstado.CONFIRMADO)

            agenda.registrarEnHistorial(
                turnoId: nuevoTurno.id,
                descripcion: "Turno confirmado por el paciente"
            )

        FIN SI

    FIN SI

FIN SI

// ============================================================
// CU02 - Reprogramar Turno
// ============================================================

// El paciente solicita modificar el horario de su turno.
// Se verifica la disponibilidad del nuevo horario.

disponibleNuevoHorario = agenda.verificarDisponibilidad(
    medicoId: medico.matricula,
    fecha: "2026-06-30",
    hora: "14:00"
)

SI NO disponibleNuevoHorario ENTONCES

    alternativas = agenda.sugerirHorariosAlternativos(
        medicoId: medico.matricula,
        fecha: "2026-06-30"
    )

    nuevaFechaHora = alternativas[0]

SINO

    nuevaFechaHora = "2026-06-30 14:00"

FIN SI

nuevoTurno.reprogramar(nuevaFechaHora: nuevaFechaHora)

nuevoTurno.cambiarEstado(nuevoEstado: TurnoEstado.REPROGRAMADO)

agenda.registrarEnHistorial(
    turnoId: nuevoTurno.id,
    descripcion: "Turno reprogramado al " + nuevaFechaHora
)

nuevoPaciente.recibirNotificacion(
    mensaje: "Su turno fue reprogramado para las " + nuevaFechaHora
)

// ============================================================
// CU05 - Registrar Llegada
// ============================================================

// El día de la consulta el paciente llega al consultorio.
// El sistema registra su llegada y el médico realiza la atención.

nuevoTurno.registrarLlegada(horaReal: "2026-06-30 13:50")

SI nuevoTurno.presente ENTONCES

    nuevoTurno.cambiarEstado(nuevoEstado: TurnoEstado.PRESENTE)

FIN SI

agendaDiaria = medico.consultarAgenda(fecha: "2026-06-30")

medico.registrarObservacion(
    turnoId: nuevoTurno.id,
    observacion: "Paciente presenta presión arterial normal"
)

nuevoTurno.cambiarEstado(nuevoEstado: TurnoEstado.REALIZADO)

agenda.registrarEnHistorial(
    turnoId: nuevoTurno.id,
    descripcion: "Atención médica completada"
)

// ============================================================
// CU04 - Autorizar Sobreturno
// ============================================================

// Como escenario complementario, un paciente de urgencia solicita
// un sobreturno que debe ser autorizado por el médico.

pacienteUrgencia = new Paciente(
    dni: "31987654",
    nombre: "María López"
)

autorizado = medico.autorizarSobreturno(
    solicitudId: "SOL-001"
)

SI autorizado ENTONCES

    sobreturno = agenda.crearTurno(
        fechaHora: "2026-06-30 15:00",
        paciente: pacienteUrgencia,
        medico: medico,
        sobreturno: VERDADERO
    )

    sobreturno.cambiarEstado(
        nuevoEstado: TurnoEstado.CONFIRMADO
    )

FIN SI

// Estado final del sistema.

Retornar "Consulta médica finalizada y turno registrado correctamente."

FIN

## 3. Trazabilidad del Pseudocódigo

| Bloque     | Caso de uso    | Clases involucradas  | Diagrama de secuencia de  referencia |
| -- | --------------------------- | ------------------------------------------- | --------------------------------------------------------------------------- |
| Autenticación, alta del paciente y creación del turno | CU01 - Crear Turno   | Secretaria, Paciente, Medico, Agenda, Turno | [Diagrama de Secuencia - Crear Turno](../../diagramas/05-diagramas-secuencia/05-secuencia-crear-turno-01.png)         |
| Reprogramación del turno                              | CU02 - Reprogramar Turno    | Paciente, Agenda, Turno   | [Diagrama de Secuencia - Reprogramar Turno](../../diagramas/05-diagramas-secuencia/05-secuencia-reprogramar-turno-02.png)
   |
| Registro de llegada y atención médica                 | CU05 - Registrar Llegada    | Paciente, Turno, Medico, Agenda             | [Diagrama de Secuencia - Registrar Llegada](../../diagramas/05-diagramas-secuencia/05-secuencia-registrar-llegada-05.png)    |
| Autorización de sobreturno                            | CU04 - Autorizar Sobreturno | Medico, Agenda, Paciente, Turno             | [Diagrama de Secuencia - Autorizar Sobreturno](../../diagramas/05-diagramas-secuencia/05-secuencia-autorizar-sobreturno-04.png) |
