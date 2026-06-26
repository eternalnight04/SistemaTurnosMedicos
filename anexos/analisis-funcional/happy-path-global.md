// =========================================================
// HAPPY PATH GLOBAL - SISTEMA DE TURNOS MÉDICOS
// Escenario: Atención médica completa con reprogramación
// =========================================================

// 1. AUTENTICACIÓN DE LA SECRETARIA
Secretaria secretaria = new Secretaria("SEC-001", "Laura", "12345678")
boolean acceso = secretaria.autenticar("password123")

SI (acceso == VERDADERO) ENTONCES
    ESCRIBIR "Secretaria Laura ha iniciado sesión"
FIN SI

// 2. CREACIÓN DE TURNO (CU01)
// La secretaria registra un nuevo turno para un paciente
Paciente paciente = new Paciente("PAC-001", "Juan García", "30123456")
Medico medico = new Medico("MED-001", "Dr. Molina", "Cardiología")
Agenda agenda = new Agenda("AG-001", medico)

// Verificar disponibilidad del médico
boolean disponible = agenda.verificarDisponibilidad("MED-001", "2026-06-30", "10:00")

SI (disponible == VERDADERO) ENTONCES
    // Crear el turno
    Turno turno = agenda.crearTurno("2026-06-30 10:00", paciente, medico, FALSO)
    turno.cambiarEstado(TurnoEstado.CONFIRMADO)
    
    // Registrar en historial y notificar
    auditoria.guardarEvento(turno.id, "Turno creado y confirmado")
    paciente.recibirNotificacion("Su turno ha sido confirmado para el 30/06 a las 10:00")
    
    ESCRIBIR "Turno creado: " + turno.id + " - Estado: CONFIRMADO"
FIN SI

// 3. REPROGRAMACIÓN DEL TURNO (CU02)
// El paciente solicita cambiar el horario
DateTime nuevaFechaHora = "2026-06-30 14:00"

// Verificar si hay conflicto en el nuevo horario
boolean hayConflicto = !agenda.verificarDisponibilidad("MED-001", "2026-06-30", "14:00")

SI (hayConflicto == VERDADERO) ENTONCES
    // Buscar horarios alternativos
    Lista<DateTime> alternativas = agenda.sugerirHorariosAlternativos("MED-001", "2026-06-30")
    nuevaFechaHora = alternativas[0] // Seleccionar primera alternativa disponible
FIN SI

// Reprogramar el turno
boolean reprogramado = turno.reprogramar(nuevaFechaHora)

SI (reprogramado == VERDADERO) ENTONCES
    turno.cambiarEstado(TurnoEstado.REPROGRAMADO)
    auditoria.guardarEvento(turno.id, "Turno reprogramado al " + nuevaFechaHora)
    paciente.recibirNotificacion("Su turno fue reprogramado para las 14:00")
    
    ESCRIBIR "Turno reprogramado exitosamente"
FIN SI

// 4. REGISTRO DE LLEGADA DEL PACIENTE (CU05)
// El día del turno, el paciente llega al consultorio
DateTime horaRealLlegada = "2026-06-30 13:50"

turno.registrarLlegada(horaRealLlegada)

// El sistema calcula si llegó a tiempo
SI (turno.presente == VERDADERO) ENTONCES
    turno.cambiarEstado(TurnoEstado.PRESENTE)
    ESCRIBIR "Paciente presente. Diferencia: " + turno.diferenciaMinutos + " minutos"
SINO
    ESCRIBIR "Paciente ausente o llegó tarde"
FIN SI

// 5. ATENCIÓN MÉDICA Y CIERRE DEL TURNO
// El médico consulta su agenda del día
Lista<Turno> agendaDiaria = medico.consultarAgenda("2026-06-30")

// El médico atiende al paciente y registra observaciones
medico.registrarObservacion(turno.id, "Paciente presenta presión arterial normal. Se mantiene tratamiento.")

// Marcar el turno como realizado
turno.cambiarEstado(TurnoEstado.REALIZADO)
auditoria.guardarEvento(turno.id, "Turno realizado - Atención completada")

ESCRIBIR "Atención finalizada. Turno " + turno.id + " marcado como REALIZADO"

// 6. AUTORIZACIÓN DE SOBRETURNO (CU04) - Escenario alternativo
// Llega un paciente con urgencia y se necesita un sobreturno
Paciente pacienteUrgencia = new Paciente("PAC-002", "María López", "31987654")

// El médico debe autorizar el sobreturno
boolean autorizado = medico.autorizarSobreturno("SOLICITUD-001")

SI (autorizado == VERDADERO) ENTONCES
    Turno sobreturno = agenda.crearTurno("2026-06-30 15:00", pacienteUrgencia, medico, VERDADERO)
    sobreturno.cambiarEstado(TurnoEstado.CONFIRMADO)
    
    ESCRIBIR "Sobreturno autorizado y creado: " + sobreturno.id
FIN SI


| Paso | Clase | Método | Origen (CRC/Diagrama/CU) |
|---|---|---|---|
| 1. Autenticación | Secretaria | autenticar(password) | CRC UsuarioDelSistema |
| 2. Crear Turno | Agenda | crearTurno(fecha, paciente, medico, sobreturno) | CRC Agenda / CU01 |
| 2. Verificar disponibilidad | Agenda | verificarDisponibilidad(medicoId, fecha, hora) | CRC Agenda / CU01 |
| 2. Cambiar estado | Turno | cambiarEstado(nuevoEstado) | CRC Turno / CU01 |
| 2. Notificar | Paciente | recibirNotificacion(mensaje) | CRC Paciente / CU01 |
| 3. Reprogramar | Turno | reprogramar(nuevaFechaHora) | CRC Turno / CU02 |
| 3. Sugerir alternativas | Agenda | sugerirHorariosAlternativos(medicoId, fecha) | CRC Agenda / CU02 |
| 4. Registrar llegada | Turno | registrarLlegada(horaReal) | CRC Turno / CU05 |
| 5. Consultar agenda | Medico | consultarAgenda(fecha) | CRC Medico |
| 5. Registrar observación | Medico | registrarObservacion(turnoId, observacion) | CRC Medico |
| 6. Autorizar sobreturno | Medico | autorizarSobreturno(solicitudId) | CRC Medico / CU04 |

